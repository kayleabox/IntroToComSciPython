def iter_power(base, exp):
  if exp == 0:
    return 1
  num = base
  for x in range(exp - 1):
    num *= base
  return num