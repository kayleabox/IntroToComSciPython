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