def recur_power(base, exp):
  if exp == 0:
    return 1
  elif exp == 1:
    return base
  else: 
    return base * recur_power(base, exp - 1)

print('recur_power:')
base = 3
exp = 4
print('using recur_power ' + str(base) + ' to the ' + str(exp) + ' power is ' + str(recur_power(base, exp)))
base = 5
exp = 5
print('using recur_power ' + str(base) + ' to the ' + str(exp) + ' power is ' + str(recur_power(base, exp)))