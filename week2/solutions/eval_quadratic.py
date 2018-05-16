def eval_quadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b * x + c

print('eval_quadratic:')
print('2x^2 + 3x + 4 where x = 5 is: ' + str(eval_quadratic(2, 3, 4, 5)))
print('\n')