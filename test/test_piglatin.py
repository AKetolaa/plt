import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_for_phrase(self):
        str = PigLatin("hello world")
        test
        self.assertEquals("hello world",str )
