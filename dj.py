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

    bpm, sr = GetBPM.getBPMLibrosa(f, 120.0, 50.0)

    modifier = target_bpm / bpm
    new_bpm = bpm * modifier

    print(str(bpm) + " -- " + str(modifier) + " -- " + str(new_bpm))
    new_path = f.replace(dir_to_scan, outdir)
    
    new_sr = modifier * sr
    print("resampling1 to " + str(new_sr))

    # ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-filter:a", "asetrate=" + str(new_sr)]}) #timestretch
    setrate_filter = "[a]asetrate=" + str(new_sr) + "[b]"
    resample_filter = "[b]aresample=44100"
    ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-y", "-filter_complex:a", setrate_filter + ", " + resample_filter]})
    ff.run()