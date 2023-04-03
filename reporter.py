#! /usr/bin/env python3
# v1.0
import sys
from pydub import AudioSegment

# checks if argument is present quits otherwise
if len(sys.argv) < 2:
    print("needs a file")
    exit()
elif len(sys.argv) > 2:
    print("too many args")
    exit()


file_path = sys.argv[1]

# opens file
try:
    audio_file = AudioSegment.from_file(file_path)
except Exception:
    print("invalid file")
    exit()

# prints file details
sr = str(audio_file.frame_rate)
br = str(audio_file.sample_width * 8)
print(sr + "hz - sample rate ")
print(br + "bit - bit rate")
# TODO return the encoding type
