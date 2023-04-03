# audioreporter-py

Simple python script that takes command line filepath arguments and reports the bitrate-sample rate of the file. Works with any filetype ffmpeg supports, including `.wav` `.mp3` and `.aiff`.

Useful for quickly identifying audio file details during projects, or in a folder of many similar files.

### Example usage
`python3 reporter.py audiofile.wav` for a file in the same directory

`python3 reporter.py ~/music/audiofile.wav` or `python3 reporter.py C:\music\audiofile.wav` for a file in other directories

Alternatively `./reporter.py audiofile.wav` can also be used on unix-like machines

Dependencies
 - Python 3
 - Pydub
 - ffprobe (from ffmpeg)