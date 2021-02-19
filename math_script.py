"""
A script to perform basic math operations on two numbers.
"""
x = float(input('Enter your first number: '))
y = float(input('Enter your second number: '))

print('{} plus {} is {}'.format(x, y, x+y))
print('{} minus {} is {}'.format(x, y, x-y))
print('{} times {} is {}'.format(x, y, x*y))

if y!=0:
	print('{} divided by {} is {}'.format(x, y, x/y))
else:
	print("Oops! Can't divide by zero.")