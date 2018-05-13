def iter_power(base, exp):
  if exp == 0:
    return 1
  
  num = base
  for x in range(exp - 1):
    num *= base
  return num

print('iter_power:')
base = 3
exp = 4
print('using iter_power ' + str(base) + ' to the ' + str(exp) + ' power is ' + str(iter_power(base, exp)))
base = 5
exp = 5
print('using iter_power ' + str(base) + ' to the ' + str(exp) + ' power is ' + str(iter_power(base, exp)))