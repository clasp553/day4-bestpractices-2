"""
A collection of simple math operations
----
for two given values a and b:
simple_add returns their sum
simple_sub returns their difference
simple_mult returns their product
simple_div returs their quotient;

for given values a0, a1, a2 and a factor x:
poly_first returns a linear function a0 + a1^x
poly_second returns a quadratic function a0+a1x+a2x^2
"""

def simple_add(a,b):
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
