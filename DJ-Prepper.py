import ffmpy
import DirScanner
import GetBPM
import os

target_bpm = 111.0
pattern_match = "*.mp3"
timestretch_enable = False
indir = "process"
outdir = "processed"

scanner = DirScanner.DirScanner()
files = scanner.scan(indir, pattern_match)

for f in files:
    print("processing " + f)

    name_components = os.path.splitext(f)
    path_with_bpm = name_components[0] + "-" + str(target_bpm).replace(".", "_") + "bpm" + name_components[1]
    bpm, sr = GetBPM.getBPMLibrosa(f, target_bpm)

    modifier = target_bpm / bpm
    new_sr = modifier * sr

    print(str(bpm) + " -- " + str(modifier) + " -- " + str(new_sr))
    new_path = path_with_bpm.replace(indir, outdir)
    
    print("saving to " + new_path)

    if timestretch_enable:
        print("timestretching to " + str(new_sr))
        ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-filter:a", "asetrate=" + str(new_sr)]}) #timestretch
    else:
        print("resampling to " + str(new_sr))
        setrate_filter = "[a]asetrate=" + str(new_sr) + "[b]"
        resample_filter = "[b]aresample=44100"
        ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-y", "-filter_complex:a", setrate_filter + ", " + resample_filter]})

    ff.run()