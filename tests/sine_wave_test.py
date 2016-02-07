from unittest import TestCase
from sine_wave import SineWave
from time import sleep


class SineWaveTest(TestCase):

    def test_constructor(self):
        self.assertTrue(True)

    def test_data_generation(self):
        sw = SineWave(1, 1)
        data = []

        for i in range(0, 10):
            data.append(sw.data)
            sleep(0.1)

        self.assertAlmostEqual(2.86102294921875e-06, data[0][0], delta=0.01)
        self.assertAlmostEqual(1.7976337357066685e-05, data[0][1], delta=0.01)
        self.assertAlmostEqual(0.9344489574432373, data[9][0], delta=0.01)
        self.assertAlmostEqual(-0.40032304800732454, data[9][1], delta=0.01)

