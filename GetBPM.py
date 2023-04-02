import librosa

def getBPMLibrosa(f, target, range):
    y, sr = librosa.load(f, sr=None)
    beatinfo = librosa.beat.tempo(y=y, sr=sr)
    bpm = beatinfo[0]
    return keepBPMInRange(bpm, target, range), sr

def getBPMLibrosaTrim(f):
    return getBPMLibrosaTweak(f, 33.0, 3.33)


def getBPMLibrosaTweak(f, offset, duration, target, range):
    y, sr = librosa.load(f, sr=None, offset=offset, duration=duration)
    beatinfo = librosa.beat.tempo(y=y, sr=sr)
    bpm = beatinfo[0]
    return keepBPMInRange(bpm, target, range), sr

def keepBPMInRange(bpm, target, range):
    if bpm < target - range:
        while bpm < target - range:
            bpm *= 2.0

    if bpm > target + range:
        while bpm > target + range:
            bpm /= 2.0

    return bpm

