import unittest

def gcdRecur(a, b):
  if b == 0:
    return a
  else:
    return gcdRecur(abs(b), abs(a % b))


class gcdRecurTest(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur(0, 2), 2)

class gcdRecurTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur(6, 2), 2)

class gcdRecurTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur(5, 13), 1)

class gcdRecurTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur(49, 21), 7)

class gcdRecurTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur(4, 0), 4)

class gcdRecurTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur(49, -21), 7)