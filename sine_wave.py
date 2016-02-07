#!/usr/bin/env python
import math
import time


class SineWave(object):

    def __init__(self, amplitude, frequency):
        self._start_time = time.time()
        self._amplitude = amplitude
        self._frequency = frequency
        self._current_time = None

    @property
    def data(self):
        now = time.time()
        self._current_time = now - self._start_time
        return self._current_time, self._harmonic()

    def _harmonic(self):
        return self._amplitude * math.sin(2 * math.pi * self._frequency * self._current_time)






