import librosa

def getBPMLibrosa(f):
    y, sr = librosa.load(f, sr=None)
    beatinfo = librosa.beat.tempo(y=y, sr=sr)
    bpm = beatinfo[0] #round(beatinfo[0], 2)
    return bpm, sr

def getBPMLibrosaTrim(f):
    return getBPMLibrosaTweak(f, 33.0, 3.33)


def getBPMLibrosaTweak(f, offset, duration, target, range):
    y, sr = librosa.load(f, sr=None, offset=offset, duration=duration)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    # librosa.feature.tempogram
    beatinfo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    bpm = beatinfo[0] #round(beatinfo[0], 2)
    while bpm < target - range:
        bpm *= 2
    while bpm > target + range:
        bpm /= 2
    return bpm, sr

