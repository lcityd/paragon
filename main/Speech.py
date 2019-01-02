#!/usr/bin/python
# ==============================================================================
# Copyright 2018 The Paragon Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


__about__ = '''
******************************************
  SPEECH ENGINE
******************************************
'''
import random
import os
import string
import pygame
import talkey
from pygame import mixer
import sys
import subprocess

n=1
#def say(rand,n,mixer)
def produce():
    sys.path.append('../lib/tacotron-tts/')
    import argparse
    import os
    import re
    from hparams import hparams, hparams_debug_string
    from synthesizer import Synthesizer
    import subprocess

    x = open("../lib/tacotron-tts/text.txt", "r+")
    x = str(x.readline())
    sentences = [
        x
    ]


    def get_output_base_path(checkpoint_path):
      base_dir = os.path.dirname(checkpoint_path)
      m = re.compile(r'.*?\.ckpt\-([0-9]+)').match(checkpoint_path)
      name = 'eval-%d' % int(m.group(1)) if m else 'eval'
      return os.path.join(base_dir, name)


    def run_eval(args):
      print(hparams_debug_string())
      synth = Synthesizer()
      synth.load(args.checkpoint)
      base_path = get_output_base_path(args.checkpoint)
      for i, text in enumerate(sentences):
        path = '%s-%d.wav' % (base_path, i)
        print('Synthesizing: %s' % path)
        with open(path, 'wb') as f:
          f.write(synth.synthesize(text))


    def main():
      parser = argparse.ArgumentParser()
      parser.add_argument('--checkpoint', default='../lib/tacotron-tts/model.ckpt')
      parser.add_argument('--hparams', default='',
        help='Hyperparameter overrides as a comma-separated list of name=value pairs')
      args = parser.parse_args()
      os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
      hparams.parse(args.hparams)
      run_eval(args)


    if __name__ == '__main__':
      main()
      import pygame
      pygame.mixer.init()
      pygame.mixer.music.load("../lib/tacotron-tts/eval-0.wav")
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy() == True:
        continue

def say(rand,n,mixer):
    file = open("../lib/tacotron-tts/text.txt", "w")
    rand = ''.join(rand)
    file.write(rand)
    file.close()
    #neat little trick where you can call specific elements in the console, and call specific elements outside as well.
    subprocess.call("python3 Speech.py", shell=True)


if __name__ == "__main__":
    print(__about__)
    produce()
