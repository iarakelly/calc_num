import numpy as np

# f(x) = x^4 − 2.36343x^3 − 18.1163x^2 + 20.7595x + 58.8273
def f(x):
    return x**4 - 2.36343*(x**3) - 18.1163*(x**2) + 20.7595*x + 58.8273

# Derivada para o método de Newton
def df(x):
    return 4*(x**3) - 7.09029*(x**2) - 36.2326*x + 20.7595

#Método da Bisseção
def bissecao(a, b, erro):
    print(f"\n--- Bisseção em [{a}, {b}] ---")
    it = 0
    while True:
        m = (a + b) / 2
        print(f"Iteração {it}: x = {m:.6f}, f(x) = {f(m):.6f}")
        
        if abs(f(m)) < erro:
            return m
        
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        it += 1

#Método de Newton-Raphson
def newton(x0, erro):
    print(f"\n--- Newton-Raphson (x0 = {x0}) ---")
    x = x0
    it = 0
    while True:
        #f(x)/df(x).
        x_next = x - f(x) / df(x)
        print(f"Iteração {it}: x = {x_next:.6f}, f(x) = {f(x_next):.6f}")
        
        if abs(f(x_next)) < erro:
            return x_next
        x = x_next
        it += 1

#Método da Secante
def secante(x0, x1, erro):
    print(f"\n--- Secante (x0={x0}, x1={x1}) ---")
    it = 0
    while True:
        f_x0 = f(x0)
        f_x1 = f(x1)
        x_next = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        
        print(f"Iteração {it}: x = {x_next:.6f}, f(x) = {f(x_next):.6f}")
        
        if abs(f(x_next)) < erro:
            return x_next
        
        x0, x1 = x1, x_next
        it += 1

#Método da Regula Falsi (Falsa Posição)
def regula_falsi(a, b, erro):
    print(f"\n--- Regula Falsi em [{a}, {b}] ---")
    it = 0
    while True:
        f_a = f(a)
        f_b = f(b)
        x = (a * f_b - b * f_a) / (f_b - f_a)
        
        print(f"Iteração {it}: x = {x:.6f}, f(x) = {f(x):.6f}")
        
        if abs(f(x)) < erro:
            return x
        
        if f_a * f(x) < 0:
            b = x
        else:
            a = x
        it += 1


precision = 0.001

# Com base no gráfico da função, as raízes estão aproximadamente em:
# x ≈ -3.2, x ≈ -1.5, x ≈ 2.5, x ≈ 4.6

r1 = bissecao(-4, -3, precision)
r2 = newton(-1, precision)
r3 = secante(2, 3, precision)
r4 = regula_falsi(4, 5, precision)

print("\n" + "="*42)
print(f"Raízes encontradas: \n{r1:.4f}\n{r2:.4f}\n{r3:.4f}\n{r4:.4f}")