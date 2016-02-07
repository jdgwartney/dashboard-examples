#!/usr/bin/env python
from sine_wave import SineWave
import time
import json
import sys
from threading import Thread, Lock

# global flag indicating threads should terminate
terminate = False

# Critical section to serialize access to standard out and
# avoid interleaved output
lock = Lock()


def output_measurements(item):
    """
    Thread function for outputing measurements
    """
    global terminate
    sw = SineWave(item['name'], float(item['amplitude']), float(item['frequency']))
    poll = item['sample'] / 1000.0
    while True:
        if terminate:
            break
        now = int(time.time())
        with lock:
            print("{0} {1} {2} {3}".format("SINE_WAVE_AMPLITUDE", sw.name, sw.data[1], now))
            sys.stdout.flush()
        time.sleep(poll)


class SineWavePlugin(object):
    def __init__(self):
        pass

    def _init(self):
        """
        Initialize the plugin by reading param.json and spawning
        a thread for each of the configuration items
        """
        with open('param.json') as f:
            parameters = json.load(f)
            for item in parameters['items']:
                t = Thread(target=output_measurements, args=(item,))
                t.start()

    def run(self):
        """
        Method to start the plugin
        """
        global terminate
        self._init()
        while True:
            try:
                if terminate:
                    break
                time.sleep(0.1)
            except KeyboardInterrupt:
                terminate = True


if __name__ == "__main__":
    w = SineWavePlugin()
    w.run()
