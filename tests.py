import unittest

from geodistance import Geodistance

class GeodistanceTestCase(unittest.TestCase):
    def setUp(self):
        self.length = Geodistance()

    def test_1(self):
        result = self.length.distance(33.93911, 67.709953,41.153332, 20.168331)
        self.assertEqual(result, 4214)

    def test_2(self):
        result = self.length.distance(40.069099, 45.038189, 12.226079, -69.060087)
        self.assertEqual(result, 11089)

    def test_3(self):
        result = self.length.distance(-11.202692, 17.873887, 47.516231, 14.550072)
        self.assertEqual(result, 6537)

    def test_4(self):
        result = self.length.distance(56.130366, -106.346771, 46.818188, 8.227512)
        self.assertEqual(result, 7056)
