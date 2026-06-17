import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20)

y = 2 + 3*np.log(x+1) - 0.5*x + np.random.normal(0, 0.5, len(x))

plt.scatter(x,y)
plt.show()

A = np.column_stack([
    np.ones(len(x)),
    np.log(x+1),
    x
])

M = np.hstack((ATA, ATy.reshape(-1,1)))

coef = gauss_jordan(M.copy())

a = coef[0]
b = coef[1]
c = coef[2]

print(f"g(x) = {a:.4f} + {b:.4f}ln(x+1) + {c:.4f}x")

x_plot = np.linspace(min(x), max(x), 1000)

y_aprox = a + b*np.log(x_plot+1) + c*x_plot

plt.scatter(x, y, label="Pontos")
plt.plot(x_plot, y_aprox, label="Aproximação")

plt.legend()
plt.grid()
plt.show()