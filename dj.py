import librosa
import DirScanner

scanner = DirScanner.DirScanner()
files = scanner.scan("testfiles")

for f in files:
    y, sr = librosa.load(f)
    beatinfo = librosa.beat.tempo(y)
    print(beatinfo)