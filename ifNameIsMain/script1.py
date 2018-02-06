"""
Example of using:
if __name__ == '__main__' (I'll refer to this as the "clause")

This script will have some functions that can be used directly by calling this script with system arguments OR by
passing variables from another function. The contents of the script included within the clause will only be run
if script1 is called directly, otherwise __name__ != __main__, so the contents of the clause will not run, but we will
still have access to the functions in script1.
"""

import sys

""" FUNCTIONS """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

""" MAIN """
def main(a, b):
    # Make a list of all functions
    functions = (add, subtract, multiply, divide)
    # Make a list of names associated with each function
    names = ('add', 'subtract', 'multiply', 'divide')
    # Make a list of symbols associated with each function
    symbols = ('+', '-', '*', '/')

    # Zip will make combination of one element from each list in order
    # Ex. On first loop:
    #| func = add
    #| name = 'add'
    #| symbol = '+'
    for func, name, symbol in zip(functions, names, symbols):
        print("Let's %s %s!" % (name, ' and '.join([str(a), str(b)])))
        result = func(a, b)
        print('%d %s %d = %.2f' % (a, symbol, b, result))
        print()

    # What is the current value of __name__?
    print('Here is the contents of the variable __name__: %s' % __name__)


if __name__ == '__main__':

    welcome = """
    Welcome to the arithmetic machine!
    Pass two variables with a space between each one and we'll do some shit to them
    
    USAGE: python script1.py <Some number> <another number (or the same!)>
    EX: python script1.py 4 10
    """
    # Print welcome message
    print(welcome)

    # Accept system arguments
    if len(sys.argv) != 3:
        print('ERROR: Two numbers and two numbers only!')
        sys.exit()
    a, b = sys.argv[1:]
    # Convert to integers
    a = int(a)
    b = int(b)
    print()
    print('Alright, your numbers are %s' % ' and '.join([str(a), str(b)]))
    print("Let's run the main function in script1")
    input('Press enter to continue')
    print()
    main(a, b)

