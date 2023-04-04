# dj-prepper
Python program to make audio files all the same bpm. 
  The idea being, you prep your files, then you can lay out a mix quickly in something like audacity


## arguments (set these in DJ-Prepper.py):


**target_bpm:** the bpm to match all files to

**pattern_match:** pattern match to search for files in 'dir_to_scan' 

**timestretch_enable:** enable timestretching (no pitch change), default is false to resample (changes pitch like a record)

**indir:** name of the directory to look for files (simplest is to not change this, and put your files in 'process' folder

**outdir:** name of the directory to save output. recommended to leave this as is
