"""
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s.
This function should sum the area and square of the perimeter of the regular polygon.
The function returns the sum, rounded to 4 decimal places.
"""

import math

def polysum(n, s):
  area = (0.25*n*s**2)/(math.tan(math.pi/n))
  perimeter = n * s
  return round(area + perimeter**2, 4)

print('polysum:')
n = 4
s = 3
print('polysum of a polygon with ' + str(n) + ' sides of ' + str(s) + ' length is ' + str(polysum(n, s)))
n = 5
s = 6
print('polysum of a polygon with ' + str(n) + ' sides of ' + str(s) + ' length is ' + str(polysum(n, s)))
print('\n')