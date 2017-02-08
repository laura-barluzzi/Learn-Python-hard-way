# formula 100 - 20 * 4 + 20 / 2 * 8 --> 80 = 80

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b):
    return a / b
    
# creating variable for each operation
x = multiply(20, 4)
y = divide(20, 2)
z = multiply(y, 8)
w = add(x, z)
u = subtract(100, w)

print """ The result of the following equation: 
100 - 20 * 4 + 20 / 2 * 8 
is: 
%d""" % (u)

# by aggregating all functions

result = subtract(100, add(multiply(20, 4), multiply(divide(20, 2),8)))

print """ The result of the following equation: 
100 - 20 * 4 + 20 / 2 * 8 
is: 
%d""" % (result)
