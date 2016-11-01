from collections import deque
from itertools import islice

# double-ended queues
# pronounced like 'deck'

# 0.
# lists are inefficient as queues, so use collections.deque
d = deque(['Kili', 'Fili', 'Oin', 'Gloin', 'Bifur', 'Bofur'])
d.append('Thorin')
print(d.popleft())
print(d.popleft())
print(d.popleft())
print(d.popleft())

# 1.
# tail functionality with deque
def tail(filename, n=10):
    with open(filename) as f:
        return deque(f, n)

for line in tail('04args.py', n=5):
    print(line, end='')

for line in tail('04args.py'):
    print(line, end="")


# 2.
# running average with deque
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(islice(it, n-1))
    print("Deque init:", d)
    d.appendleft(0)
    print("Deque appendleft(0):", d)
    s = sum(d)
    print("Sum init:", s)
    for elem in it:
        print("Elem", elem)
        s += elem - d.popleft()
        print("Sum:", s)
        print("Deque:", d)
        d.append(elem)
        print("Deque append elem:", d)
        print("Yield s/n:", s/n)
        yield s / n


if __name__ == '__main__':
    for mav in moving_average([40, 30, 50, 46, 39, 44]):
        print(mav)


# 3.
# deque slicing and deletion
def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

d = deque(['Kili', 'Fili', 'Oin', 'Gloin', 'Bifur', 'Bofur'])
print(d)
delete_nth(d, 3)
print(d)

