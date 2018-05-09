import unittest

def isIn(char, aStr):
  if len(aStr) == 0:
    return False
  elif len(aStr) == 1:
    return char == aStr[0]
  elif char > aStr[int(len(aStr)/2)]:
    print(aStr[int(len(aStr)/2):])
    return isIn(char, aStr[int(len(aStr)/2):])
  elif char < aStr[int(len(aStr)/2)]:
    print(aStr[0 : int(len(aStr)/2)])
    return isIn(char, aStr[0 : int(len(aStr)/2)])

class isInTestZ(unittest.TestCase):
  def test(self):
    self.assertEqual(isIn('z', 'abz'), True)

class isInTestA(unittest.TestCase):
  def test(self):
    self.assertEqual(isIn('a', 'abc'), True)