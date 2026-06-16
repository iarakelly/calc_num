import numpy as np
import matplotlib.pyplot as plt

# Pontos fornecidos
x = np.array([0, 1, 2, 3])
y = np.array([2.0, 3.7, 7.4, 20.1])

# Funções-base
phi1 = np.ones(len(x))
phi2 = np.exp(x)

# Matriz A
A = np.column_stack((phi1, phi2))

# Equações normais
ATA = A.T @ A
ATy = A.T @ y

# Resolve o sistema
coef = np.linalg.solve(ATA, ATy)

a = coef[0]
b = coef[1]

print(f"f(x) = {a:.4f} + {b:.4f}e^x")

# Plotagem
x_plot = np.linspace(0, 3, 100)

y_aprox = a + b*np.exp(x_plot)

plt.scatter(x, y, label="Pontos")
plt.plot(x_plot, y_aprox, label="Aproximação")

plt.legend()
plt.grid()
plt.show()