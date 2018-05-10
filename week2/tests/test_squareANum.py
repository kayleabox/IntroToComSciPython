import unittest
import os
import sys
import solutions.squareANum as squareANum

class squareANumTest(unittest.TestCase):
    def test(self):
        self.assertEqual(squareANum.square(3), 9)
