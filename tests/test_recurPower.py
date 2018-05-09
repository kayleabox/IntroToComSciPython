import unittest

def recurPower(base, exp):
  if exp == 0:
    return 1
  elif exp == 1:
    return base
  else: 
    return base * recurPower(base, exp - 1)

class recurPowerTestSquare(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower(2, 2), 4)

class recurPowerTestCube(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower(3, 3), 27)

class recurPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower(2, 4), 16)

class recurPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower(2.5, 5), 97.65625)

class recurPowerTest0(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower(2.5, 0), 1)

class recurPowerTestFirst(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower(2.5, 1), 2.5)