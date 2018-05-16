def is_in(char, aStr):
  if len(aStr) == 0:
    return False
  elif len(aStr) == 1:
    return char == aStr[0]
  elif char > aStr[len(aStr)//2]:
    return is_in(char, aStr[len(aStr)//2:])
  elif char < aStr[len(aStr)//2]:
    return is_in(char, aStr[0 : len(aStr)//2])
  return char == aStr[len(aStr)//2]

print('is_in:')
print('x is in fghklnz: ' + str(is_in('x', 'fghklnz')))
print('n is in fghklnz: ' + str(is_in('n', 'fghklnz')))
print('\n')