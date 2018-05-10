def isIn(char, aStr):
  if len(aStr) == 0:
    return False
  elif len(aStr) == 1:
    return char == aStr[0]
  elif char > aStr[len(aStr)//2]:
    return isIn(char, aStr[len(aStr)//2:])
  elif char < aStr[len(aStr)//2]:
    return isIn(char, aStr[0 : len(aStr)//2])
  return char == aStr[len(aStr)//2]