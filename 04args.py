# 0.
# default arguments evaluated only once
# this matters when they are mutable objects, like a list
# even flagged by the front end
def f(a, L=[]):
    L.append(a) # append more efficient than +
    return L

print(f(1))
print(f(2))
print(f(3))

# 1.
# preventing the default being shared across calls
def g(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(g(1))
print(g(2))
print(g(3))

# 2.
# formal, positional, and keyword parameters
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger",                             # matches kind
           "It's very runny, sir.",                 # pos (tuple)
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",              # kw (dict)
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 3.
# variading paratemer lists
def concat(*args, sep = '/'):
    return sep.join(args)

print(concat('andy', 'murray', 'kills', 'at', 'wimbledon'))
print(concat('andy', 'murray', 'kills', 'at', 'wimbledon', sep = '-'))

# 4.
# unpacking
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

