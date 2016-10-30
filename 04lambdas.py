# 0.
# lambdas - returning functions
def make_incrementor(n):
    return lambda x: x + n

inc = make_incrementor(13)

print(inc(4))
print(inc(50))

# 1.
# lambdas - passing a small function
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pair: pair[1])
print(pairs)
