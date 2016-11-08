'''
PYTHON CLASSES (from 3.5.1 tutorial):

Compared with other programming languages, Python’s class mechanism adds classes with a minimum of new syntax and
semantics. It is a mixture of the class mechanisms found in C++ and Modula-3.

Python classes provide all the standard features of Object Oriented Programming:
 - the class inheritance mechanism allows multiple base classes,
 - a derived class can override any methods of its base class or classes, and
 - a method can call the method of a base class with the same name.

Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic
nature of Python: they are created at runtime, and can be modified further after creation.

In C++ terminology,
 - normally class members (including the data members) are public (except see below Private Variables), and
 - all member functions are virtual.

As in Modula-3,
 - there are no shorthands for referencing the object’s members from its methods:
 - the method function is declared with an explicit first argument representing the object, which is provided
   implicitly by the call.

As in Smalltalk,
 - classes themselves are objects. This provides semantics for importing and renaming.

Unlike C++ and Modula-3,
 - built-in types can be used as base classes for extension by the user.

Also, like in C++,
 - most built-in operators with special syntax (arithmetic operators, subscripting etc.) can be redefined for class
   instances.
'''

# 0.
# scope example
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    # doesn't change the current scope binding
    do_local()
    print("After local assignment:", spam)
    # changes the current (outer) scope binding
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    # changes the global scope binding
    do_global()
    print("After global assignment:", spam)

# no global scope binding for 'spam'
try:
    print("In global scope:", spam)
except NameError:
    print("No global scope binding for 'spam'")

scope_test()
print("In global scope:", spam)

