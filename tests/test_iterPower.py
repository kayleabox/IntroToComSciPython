import unittest

def iterPower(base, exp):
  if exp == 0:
    return 1
  num = base
  for x in range(exp - 1):
    num *= base
  return num

class iterPowerTestSquare(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower(2, 2), 4)

class iterPowerTestCube(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower(3, 3), 27)

class iterPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower(2, 4), 16)

class iterPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower(2.5, 5), 97.65625)

class iterPowerTest0(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower(2.5, 0), 1)

class iterPowerTestFirst(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower(2.5, 1), 2.5)