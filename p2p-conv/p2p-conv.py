#!/bin/python3

import os
import argparse
import shutil

from ffmpy import FFmpeg

def convert(file, indir, outdir, quality):
  print('Converting:', file)

  infile  = os.path.join(os.path.abspath(indir), file)
  outfile = os.path.join(os.path.abspath(outdir), file.replace('.wav', '.ogg'))

  ff = FFmpeg(
    inputs={infile: None},
    outputs={outfile: [
      '-codec:a', 'libvorbis',
      '-qscale:a', str(quality),
      '-y'
    ]}
  )

  print(ff.cmd)
  ff.run()

def directory_type(x):
  x = str(x)

  if not os.path.isdir(x):
    raise argparse.ArgumentTypeError('Provided path is not a directory.')

  return x

def quality_type(x):
  x = int(x)

  if x < 0:
    raise argparse.ArgumentTypeError('Minimum quality is 0.')
  elif x > 10:
    raise argparse.ArgumentTypeError('Maximum quality is 10.')

  return x

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Backup directory and convert WAV files to OGG.')
  parser.add_argument('directory',
                      metavar='DIRECTORY',
                      type=directory_type,
                      help='directory to be processed')
  parser.add_argument('-o',
                      '--output',
                      dest='output',
                      metavar='O',
                      type=str,
                      default = 'backup',
                      help='output directory')
  parser.add_argument('-q',
                      '--quality',
                      dest='quality',
                      metavar='N',
                      type=quality_type,
                      default=5,
                      help='OGG compression quality [0 - 10]')

  args = parser.parse_args()

  print('Copying directory structure...')
  if os.path.exists(args.output):
    print('Removing', args.output, '...')
    shutil.rmtree(args.output, ignore_errors=True)

  shutil.copytree(args.directory, args.output, ignore=shutil.ignore_patterns('*.wav'))

  print('Converting WAV files...')
  for root, dirs, files in os.walk(args.directory):
    for file in files:
      if file.endswith('.wav'):
        convert(file, root, args.output, args.quality)
