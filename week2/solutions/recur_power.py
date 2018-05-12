def recur_power(base, exp):
  if exp == 0:
    return 1
  elif exp == 1:
    return base
  else: 
    return base * recur_power(base, exp - 1)