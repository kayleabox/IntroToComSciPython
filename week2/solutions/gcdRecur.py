def gcdRecur(a, b):
  if b == 0:
    return a
  else:
    return gcdRecur(abs(b), abs(a % b))

