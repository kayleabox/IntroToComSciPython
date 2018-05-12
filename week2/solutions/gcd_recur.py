def gcd_recur(a, b):
  if b == 0:
    return a
  else:
    return gcd_recur(abs(b), abs(a % b))

