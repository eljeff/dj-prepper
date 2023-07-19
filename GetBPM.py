import librosa

def getBPMLibrosa(f, target):
    file_duration = librosa.get_duration(filename=f)
    offset = 60
    duration = 60
    if file_duration < (offset + duration):
        offset = 0
        duration = file_duration

    y, sr = librosa.load(f, sr=None, mono=True, offset=offset, duration=duration)
    beatinfo = librosa.beat.tempo(y=y, sr=sr, start_bpm=int(target), hop_length=64)
    bpm = beatinfo[0]
    print("guessed bpm " + str(bpm))
    
    return keepBPMInRangeScale(bpm, target), sr

#offset and duration in seconds
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

