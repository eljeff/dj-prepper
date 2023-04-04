import ffmpy
import DirScanner
import GetBPM
import os

dir_to_scan = "process"
scanner = DirScanner.DirScanner()
files = scanner.scan(dir_to_scan, "*.mp3")
outdir = "processed"

target_bpm = 111.0

for f in files:
    print("processing " + f)

    name_components = os.path.splitext(f)
    path_with_bpm = name_components[0] + "-" + str(target_bpm).replace(".", "_") + "bpm" + name_components[1]
    bpm, sr = GetBPM.getBPMLibrosa(f, 120.0, 50.0)

    modifier = target_bpm / bpm
    new_bpm = bpm * modifier

    print(str(bpm) + " -- " + str(modifier) + " -- " + str(new_bpm))
    new_path = path_with_bpm.replace(dir_to_scan, outdir)
    
    new_sr = modifier * sr
    print("resampling to " + str(new_sr))
    print("saving to " + new_path)

    # ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-filter:a", "asetrate=" + str(new_sr)]}) #timestretch
    setrate_filter = "[a]asetrate=" + str(new_sr) + "[b]"
    resample_filter = "[b]aresample=44100"
    ff = ffmpy.FFmpeg(inputs={f: None}, outputs={new_path: ["-y", "-filter_complex:a", setrate_filter + ", " + resample_filter]})
    ff.run()