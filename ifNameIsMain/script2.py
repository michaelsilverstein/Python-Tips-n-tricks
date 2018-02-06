"""
A continuation of the example of how to use: if __name__ == '__main__'

Here we will import script1, meaning that we will be able to use functions from script1. Because we have included the
"if __name__=='__main__'" clause in script1, the contents of that condition will not run when we will call functions
from script1 from script2. Without the clause, script1 would attempt to run on import
"""

import script1

print("Let's use some functions from script1")
print()
a = input('Enter a value for a: ')
b = input('Enter a value for b: ')

a = int(a)
b = int(b)

# Let's borrow some of the functions from script1
functions = (script1.subtract, script1.multiply)
symbols = ('-', '*')
print()
print("Let's use the subtract and multiply functions from script1")
input('Press enter to continue')
for function, symbol in zip(functions, symbols):
    r = function(a, b)
    print('%d %s %d = %.2f' % (a, symbol, b, r))
    print()

print("Now let's use the main function in script1")
input('Press enter to continue')
print()
script1.main(a, b)
print('Look familiar? Just like when we called scrip1 directly! Now with the values passed from script2.')
print()
input('Press enter to continue')
msg = """
Notice that at no point was the welcome message from script1 or any part of the "clause" executed.
Most importantly notice that the name of __name__ does not equal __main__. 
This is what happens when one script is called from another.
"""
print(msg)

