import librosa
import ffmpy
import DirScanner
import GetBPM
# from pyAudioAnalysis import audioBasicIO
# from pyAudioAnalysis import ShortTermFeatures
# from pyAudioAnalysis import MidTermFeatures

dir_to_scan = "testfiles"
scanner = DirScanner.DirScanner()
files = scanner.scan(dir_to_scan)
outdir = "processed"

target_bpm = 111.0

for f in files:
    print("processing " + f)
    # [Fs, signal] = audioBasicIO.read_audio_file(f)
    # signal = signal[:,0]
    # signal_len = len(signal)
    # len_of_song = signal_len / Fs
    # # Window Size in mseconds
    # windowSize_in_ms = 50
    # windowSize_in_s = windowSize_in_ms/1000
    # # Window Size in Samples
    # windowSize_in_samples = Fs * (windowSize_in_ms / 1000) #divide by 1000 to turn to seconds
    # print("Window Size (samples): ",windowSize_in_samples)

    # # Window Step in mseconds
    # wStep_in_ms = 25
    # # Window Step in Samples
    # wStep_in_samples = Fs * (wStep_in_ms / 1000) #divide by 1000 to turn to seconds
    # print("Window Step in Samples: ", wStep_in_samples) 
    
    # # Oversampling Percentage
    # oversampling_Percentage = (wStep_in_ms / windowSize_in_ms) * 100
    # print("Oversampling Percentage (overlap of windows): ",oversampling_Percentage)

    # # Total Number of Windows in Signal
    # total_number_windows = signal_len / windowSize_in_samples
    # print("Total Number of Windows in Signal: ",total_number_windows)

    # # Total number of feature samples produced (windows/size * total windows)
    # feature_samples_points_total_cal = int(total_number_windows * (windowSize_in_ms/wStep_in_ms))
    # print("Calculated Total of Points Produced per Short Term Feature: ",feature_samples_points_total_cal)

    # # Extract features and their names. Each index has its own vector of features. The total number should be the same
    # # as the calculated total of points produced per feature.
    # Features_shortTerm, feature_names = ShortTermFeatures.feature_extraction(signal, Fs, windowSize_in_samples, wStep_in_samples)

    # # Exact Number of points in the Features
    # feature_samples_points_total_exact = len(Features_shortTerm[0])
    # print("Exact Total of Points Produced per Short Term Feature: ",feature_samples_points_total_exact)

    # # Mid-window (in seconds)
    # mid_window_seconds = int(1 * Fs)

    # # Mid-step (in seconds)
    # mid_step_seconds = int(1 * Fs)

    # # MID FEATURE Extraction
    # Features_midTerm, short_Features_ignore, mid_feature_names = MidTermFeatures.mid_feature_extraction(signal,Fs,mid_window_seconds,mid_step_seconds,windowSize_in_samples,wStep_in_samples)

    # # Exact Mid-Term Feature Total Number of Points
    # midTerm_features_total_points = len(Features_midTerm)
    # print("Exact Mid-Term Total Number of Feature Points: ",midTerm_features_total_points)

    # # Beats per min
    # # The Tempo of music determins the speed at which it is played (measured in BPM)
    # bpm,confidence_ratio = MidTermFeatures.beat_extraction(Features_shortTerm,1)
    # print("Beats per Minute (bpm): ",bpm)
    # print("Confidence ratio for BPM: ", confidence_ratio)

    bpm1, sr1 = GetBPM.getBPMLibrosa(f, 120., 50.0)

    modifier1 = target_bpm / bpm1
    new_bpm1 = bpm1 * modifier1

    print(str(bpm1) + " -- " + str(modifier1) + " -- " + str(new_bpm1))
    new_path = f.replace(dir_to_scan, outdir)
    
    new_sr1 = modifier1 * sr1
    print("resampling1 to " + str(new_sr1))
    # ffmpeg -y -i input_video_path -i logo_path -filter_complex "[0:a]volume=volume=6dB:precision=fixed[a];[0:v]eq=gamma=1.5:saturation=1.3[bg];[bg][1:0]overlay=main_w-(overlay_w + 10):10,format=yuvj420p[v]" -map "[v]" -map "[a]" output_video_path

    # ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-filter:a", "asetrate=" + str(new_sr)]}) #timestretch
    setrate_filter = "[a]asetrate=" + str(new_sr1) + "[b]"
    resample_filter = "[b]aresample=44100"
    ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-y", "-filter_complex:a", setrate_filter + ", " + resample_filter]})
    ff.run()