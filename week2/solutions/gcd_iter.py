def gcd_iter(a, b):
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

print('gcd_iter:')
a = 4
b = 5
print('the gcd of ' + str(a) + ' and ' + str(b) + ' is: ' + str(gcd_iter(a, b)))
a = 3
b = 9
print('the gcd of ' + str(a) + ' and ' + str(b) + ' is: ' + str(gcd_iter(a, b)))
a = 10
b = 8
print('the gcd of ' + str(a) + ' and ' + str(b) + ' is: ' + str(gcd_iter(a, b)))
print('\n')