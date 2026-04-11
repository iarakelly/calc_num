import numpy as np

 #𝑓(𝑥) = 𝑥4 − 2.36343𝑥3 − 18.1163𝑥2 + 20.7595𝑥 + 58.8273
def f(x):
    return x**4 - 2.36343*x**3 - 18.1163*x**2 + 20.7595*x + 58.8273

 # stopped critter: |xn+1 - xn| < 0.5

#1. bissection method
def bissection_method(a, b, precision):
    #step one: check the sign of f(a) and f(b)
    # Base case: if f(a) and f(b) have the same sign, then there is no root in the interval [a, b]
    if abs(b - a) < precision:
        print("The root is approximately: ", (a + b) / 2)
        return (a + b) / 2

    m = (a+b)/2
    f_a = f(a)
    f_b = f(b)
    f_m = f(m) 

    if f_a *f_m < 0: #[a,m]
        b = m
        return bissection_method(a, b, precision)
    else:
        a = m
        return bissection_method(a, b, precision)
    
precision = 0.0001
bissection_method(-2, 3, precision) #obs: if the inteval is too large, the method can not working 

#2. newton method

def df(x):
    return 4*x**3 - 7.09029*x**2 - 36.2326*x + 20.7595

    #transform in recurssion function after
def newthon_method(x, precision):

    while True:
    
        next_x = x - (f(x)/ df(f(x))) # calc next x

        #stopped if
        if abs(next_x -x) < precision:
            print("The root is approximately: ", next_x) 
            break

        x = next_x

newthon_method(-2, precision)

#3. secant method

def secant_method(a, b, precision):

    while True:
    
        next_x = a - ( ( f(a)/ ((f(a)-f(b))/(a-b)) ) ) # calc next x

        #stopped if
        if abs(next_x -b) < precision:
            print("The root is approximately: ", next_x) 
            break

        a, b = b, next_x


secant_method(-2, 3, precision)

#4. false position method

def false_position_method(a, b, precision):
        
    if f(a) * f(b) >= 0:
        return None
    
    while True:
        next_x = a - ( ( f(a)/ ((f(a)-f(b))/(a-b)) ) ) # calc next x

        #stopped if
        if abs(f(next_x)) < precision:
            print("The root is approximately: ", next_x)
            break 
        if f(a) * f(next_x) < 0:
            b = next_x  #left
        else:
            a = next_x  # right

false_position_method(-2, 5, precision)
