import librosa
import ffmpy
import DirScanner

dir_to_scan = "testfiles"
scanner = DirScanner.DirScanner()
files = scanner.scan(dir_to_scan)
outdir = "processed"

target_bpm = 111.0

for f in files:
    print(f)
    y, sr = librosa.load(f, sr=None)
    beatinfo = librosa.beat.tempo(y)
    bpm = beatinfo[0]
    modifier = target_bpm / bpm
    new_bpm = bpm * modifier
    print(str(bpm) + " -- " + str(modifier) + " -- " + str(new_bpm))
    new_path = f.replace(dir_to_scan, outdir)
    
    new_sr = modifier * sr
    print("resampling to " + str(new_sr))
    # ffmpeg -y -i input_video_path -i logo_path -filter_complex "[0:a]volume=volume=6dB:precision=fixed[a];[0:v]eq=gamma=1.5:saturation=1.3[bg];[bg][1:0]overlay=main_w-(overlay_w + 10):10,format=yuvj420p[v]" -map "[v]" -map "[a]" output_video_path

    # ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-filter:a", "asetrate=" + str(new_sr)]}) #timestretch
    setrate_filter = "[a]asetrate=" + str(new_sr) + "[b]"
    resample_filter = "[b]aresample=44100"
    ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-y", "-filter_complex:a", setrate_filter + ", " + resample_filter]})
    ff.run()