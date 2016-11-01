from collections import deque

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
    print(line, end='')


# 2.
# running average with deque
