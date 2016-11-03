# miscellaneous string formatting

# 0.
# tables w/ justification
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end= " ")
    print(repr(x*x*x).rjust(4))

# or, equivalently
if __name__ == '__main__':
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 1.
# fill numerics with leading zeros
print(repr(-3.14).zfill(5))
print(repr(-3.14).zfill(7))
print(repr(-3.14).zfill(9))

# also
print('-3.14'.zfill(5))
print('-3.14'.zfill(7))
print('-3.14'.zfill(9))

# 2.
# using '.format()'
print('We are the {} who say {}.'.format('spacepeople', '"Hail to the commets!"'))

print('{0} and {1}'.format('Earth', 'Mars'))
print('{1} and {0}'.format('Earth', 'Mars'))

print('The terminator over {land_form} was {adjective}.'.format(
    land_form='Acidalia Planitia', adjective='stunning'
))

import math
print('The value of pi is approximately {0:.3f}'.format(math.pi))
print('The value of pi is approximately {:.5f}'.format(math.pi))
print('The value of pi is approximately {0:.13f}'.format(math.pi))

# let's play with planets
near_planets = {
    'Mercury': 2440,
    'Venus': 6052,
    'Earth': 6378,
    'Mars': 3397
}

# this is a dictionary: notice the unpredictable order of the elements!
for planet, radius in near_planets.items():
    print('{0:10} ==> {1:10d}'.format(planet, radius))
for planet, radius in near_planets.items():
    print('{0:7} ==> {1:4d}'.format(planet, radius))

# dictionary with [] key access (pass dict)
print('The radii of the 4 Solar System planets nearest to the Sun are as follows: '
      'Mercury: {0[Mercury]:d}, '
      'Venus: {0[Venus]:d}, '
      'Earth: {0[Earth]:d}, '
      'Mars: {0[Mars]:d}.'.format(near_planets))

# dictionary with keyword access (pass **dict)
print('The radii of the 4 Solar System planets nearest to the Sun are as follows: '
      'Mercury: {Mercury:d}, '
      'Venus: {Venus:d}, '
      'Earth: {Earth:d}, '
      'Mars: {Mars:d}.'.format(**near_planets))

# currently defined variables with vars()
print(vars())

# NOTE: need to make a copy if we want to iterate
# as the dictionary will change during iteration
local_vars = dict(vars())
# or
# local_vars = vars().copy()
for var, val in local_vars.items():
    print('{0:20s} ==> {1:200s}'.format(var, repr(val)))

