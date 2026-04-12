import numpy as np


def f(x):
    return 1/np.sqrt(400 - x**2) + 1/np.sqrt(900 - x**2) - 0.125

#2. newton method

def df(x):
    return   x / (400 - x**2)**(1.5) + x / (900 - x**2)**(1.5)

def newthon_method(x, precision):

    while True:
        if x >= 20:
            x = 19.9

        next_x = x - (f(x)/ (df(x))) # calc next x

        #stopped if
        if abs(f(x)) < precision:
            print(f"The root is approximately: {next_x:.2f}") 
            break

        x = next_x

newthon_method(15, 0.0001)