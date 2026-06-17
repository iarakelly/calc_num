import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
], dtype=float)

B = np.array([
    2*np.log(2)-1,
    1/4,
    (2/3)*np.log(2)-5/18
])

coef = np.linalg.solve(A, B)

a, b, c = coef

print(f"g(x) = {a:.5f} + {b:.5f}x {c:+.5f}x²")

x = np.linspace(0,1,1000)

f = np.log(x+1)
g = a + b*x + c*x**2

plt.plot(x,f,label='ln(x+1)')
plt.plot(x,g,label='aproximação')
plt.grid()
plt.legend()
plt.show()