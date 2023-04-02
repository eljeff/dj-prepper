import librosa
import DirScanner

scanner = DirScanner.DirScanner()
files = scanner.scan("testfiles")

target_bpm = 111.0

for f in files:
    y, sr = librosa.load(f)
    beatinfo = librosa.beat.tempo(y)
    bpm = beatinfo[0]
    modifier = target_bpm / bpm
    new_bpm = bpm * modifier
    print(str(bpm) + " -- " + str(modifier) + " -- " + str(new_bpm))