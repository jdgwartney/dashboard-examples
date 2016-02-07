#!/usr/bin/env python
from sine_wave import SineWave
import time
import json
import sys


class SineWavePlugin(object):

    def __init__(self):
        self._sine_wave = None
        self._config = None
        self._waves = []

    def _init(self):
        with open('param.json') as f:
            self._config = json.load(f)
            for item in self._config['items']:
                self._waves.append(SineWave(item['source'], item['amplitude'], item['frequency']))

    def _output_measurements(self):
        now = int(time.time())
        for wave in self._waves:
            print("{0} {1} {2} {3}".format("SINE_WAVE_AMPLITUDE", wave.name, wave.data[1], now))
            sys.stdout.flush()
            time.sleep(1)

    def run(self):
        self._init()
        while True:
            self._output_measurements()

if __name__ == "__main__":
    w = SineWavePlugin()
    w.run()
