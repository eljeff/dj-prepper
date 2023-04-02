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
    y, sr = librosa.load(f)
    beatinfo = librosa.beat.tempo(y)
    bpm = beatinfo[0]
    modifier = target_bpm / bpm
    new_bpm = bpm * modifier
    print(str(bpm) + " -- " + str(modifier) + " -- " + str(new_bpm))
    new_path = f.replace(dir_to_scan, outdir)
    
    ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-filter:a", "atempo=" + str(modifier)]})
    ff.run()