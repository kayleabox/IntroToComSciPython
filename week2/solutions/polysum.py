"""
A regular polygon has number_sides number of sides. Each side has length length_side.

The area of a regular polygon is: 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s.
This function should sum the area and square of the perimeter of the regular polygon.
The function returns the sum, rounded to 4 decimal places.
"""

import math

def polysum(number_sides, length_side):
  area = (0.25*number_sides*length_side**2)/(math.tan(math.pi/number_sides))
  perimeter = number_sides * length_side
  return round(area + perimeter**2, 4)

print('polysum:')
number_sides = 4
length_side = 3
print('polysum of a polygon with ' + str(number_sides) + ' sides of ' + str(length_side) + ' length is ' + str(polysum(number_sides, length_side)))
number_sides = 5
length_side = 6
print('polysum of a polygon with ' + str(number_sides) + ' sides of ' + str(length_side) + ' length is ' + str(polysum(number_sides, length_side)))
print('\n')