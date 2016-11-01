# 0.
# creation
s = {'baby', 'face', 'doll', 'house', 'angel', 'smile', 'baby', 'angel'}
print(s)

t = set()
print(t)

# 1.
# set operations
a = set('abracadabra')
b = set('alacazam')

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# 2.
# set comprehensions
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

