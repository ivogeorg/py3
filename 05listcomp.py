# a map is not directly printable, only sequences (lists, tuples) and iterables
squares1 = list(map(lambda x: x**2, range(10)))
print(squares1, ' ')

# 0.
# readability
squares2 = [x**2 for x in range(10)]
print(squares2, ' ')

# 1.
# succinctness
# note: tuple expressions have to be in parentheses [(x, y) for ...]
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# is equivalent to
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

