import unittest

def gcdIter(a, b):
  if a >= b:
    inc = b
  else:
    inc = a
  while inc > 0:
    if a % inc == 0 and b % inc == 0: 
      return inc
    else: 
      inc -= 1
  return 1
        

class gcdIterTest(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter(1, 3), 1)

class gcdIterTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter(6, 3), 3)

class gcdIterTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter(21, 49), 7)

class gcdIterTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter(9, 7), 1)

class gcdIterTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter(9, 0), 1)