def gcd_recur(a, b):
  if b == 0:
    return a
  else:
    return gcd_recur(abs(b), abs(a % b))

print('gcd_recur:')
a = 4
b = 5
print('the gcd of ' + str(a) + ' and ' + str(b) + ' is: ' + str(gcd_recur(a, b)))
a = 3
b = 9
print('the gcd of ' + str(a) + ' and ' + str(b) + ' is: ' + str(gcd_recur(a, b)))
a = 10
b = 8
print('the gcd of ' + str(a) + ' and ' + str(b) + ' is: ' + str(gcd_recur(a, b)))