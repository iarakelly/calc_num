
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

    if f_a *f_m < 0:
        a = m
        return bissection_method(a, b, precision)
    else:
        b = m
        return bissection_method(a, b, precision)
precision = 0.5
bissection_method(-40, 34, precision)