def square(x):
  '''
  x: int or float.
  '''
  return x**2

def fourth_power(x):
    '''
    x: int or float.
    '''
    return square(x)**2

print('square:')
print('5 squared is: ' + str(square(5)))
print('fourth_power:')
print('3 to the fourth power is ' + str(fourth_power(3)))
print('\n')