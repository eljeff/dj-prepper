import librosa

def getBPMLibrosa(f, target):
    y, sr = librosa.load(f, sr=None)
    beatinfo = librosa.beat.tempo(y=y, sr=sr)
    bpm = beatinfo[0]
    return keepBPMInRangeScale(bpm, target), sr

def getBPMLibrosaTweak(f, offset, duration, target, range):
    y, sr = librosa.load(f, sr=None, offset=offset, duration=duration)
    beatinfo = librosa.beat.tempo(y=y, sr=sr)
    bpm = beatinfo[0]
    return keepBPMInRange(bpm, target, range), sr

def keepBPMInRange(bpm, target, range):
    lower_limit = target - range
    upper_limit = target + range
    return keepBPMInRange(bpm, lower_limit, upper_limit)

def keepBPMInRangeScale(bpm, target):
    lower_limit = target * 0.75
    upper_limit = target * 1.25
    return keepBPMInRange(bpm, lower_limit, upper_limit)

def keepBPMInRange(bpm, lowerLimit, upperLimit):
    if bpm < lowerLimit:
        while bpm < lowerLimit:
            bpm *= 2.0

    if bpm > upperLimit:
        while bpm > upperLimit:
            bpm /= 2.0

    return bpm

