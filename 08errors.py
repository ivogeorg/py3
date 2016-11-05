# errors and exceptions

# 0.
# a sampling of built-in exceptions
# all end no 'Error'
try:
    print(10 * (1/0))
    print(4 + spam*3)
    print('2' + 2)
except (ZeroDivisionError, NameError, TypeError) as inst:
    print(type(inst))  # the exception instance
    # note the trailing comma disambiguating a
    # 1-tuple from an expression in parentheses
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,

# 1.
# handling
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# 2.
# re-raising
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# 3.
# else clause
# NOTE: need to execute file as script with a file argument
for arg in sys.argv[1:]:
    if __name__ == '__main__':
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

# 4.
# exception arguments
if __name__ == '__main__':
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                             # but may be overridden in exception subclasses
        x, y = inst.args     # unpack args
        print('x =', x)
        print('y =', y)

# 5.
# exceptions caught from any call depth
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# 6.
# raising
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # if want to know about the exception but
    # don't intend to handle it...
    # raise

# 7.
# user-defined module exception hierarchy
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# 8.
# cleanup actions with finally (always executed)
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print('Caught it!')
finally:
    print('Goodbye, world!')

# the whole 9 yards! :)
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

print(divide(2, 1))
print(divide(2, 0))
# unhandled exception...
#print(divide("2", "1"))

# 9.
# classes with predefined cleanup actions => use 'with'
with open("json.txt") as f:
    for line in f:
        print(line, end="")
