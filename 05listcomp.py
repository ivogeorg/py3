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

# 2.
# flatten a list with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# unravel left to right (outer to inner)
vec = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]]
print([num for outer in vec for inner in outer for num in inner])

# 3.
# nested list comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# the first list comp is evaluated in the context of the following 'for'
print([[row[i] for row in matrix] for i in range(4)])
# a list of LISTS
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# elegantly equivalent to the above is
print(list(zip(*matrix)))

# notice that this is a list of TUPLES! (zip produces tuples)
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
