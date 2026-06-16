import numpy as np
import matplotlib.pyplot as plt

# intervalo
a_int = 0
b_int = 1

# muitos pontos para aproximar as integrais
x = np.linspace(a_int, b_int, 10000)

# função original
f = np.exp(x)

# funções base
phi1 = np.ones_like(x)
phi2 = x

# integrais aproximadas pela regra do trapézio
A11 = np.trapz(phi1*phi1, x)
A12 = np.trapz(phi1*phi2, x)
A22 = np.trapz(phi2*phi2, x)

B1 = np.trapz(f*phi1, x)
B2 = np.trapz(f*phi2, x)

A = np.array([
    [A11, A12],
    [A12, A22]
])

B = np.array([
    B1,
    B2
])

coef = np.linalg.solve(A, B)

a = coef[0]
b = coef[1]

print(f"p(x) = {a:.6f} + {b:.6f}x")


p = a + b*x

plt.plot(x, f, label="e^x")
plt.plot(x, p, label="Aproximação Linear")

plt.legend()
plt.grid()
plt.show()