# p2p-conv

## Building p2p-conv

1. Install [_FFMPG_](https://www.ffmpeg.org/) and add it to _%PATH%_.
2. Install [_Python_](https://www.python.org/downloads/windows/) and add it to _%PATH%_.
3. Install requirements `python -m pip install -r requirements.txt`.
4. Create executable `python -m PyInstaller --onefile p2p-conv.py`.

## Using p2p-conv

1. Just read help from `./p2p-conv.py --help` ;)
2. Just in case:

```
usage: p2p-conv.py [-h] [-o O] [-q N] DIRECTORY

Backup directory and convert WAV files to OGG.

positional arguments:
  DIRECTORY          directory to be processed

optional arguments:
  -h, --help         show this help message and exit
  -o O, --output O   output directory
  -q N, --quality N  OGG compression quality [0 - 10]
```
