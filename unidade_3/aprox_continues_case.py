import numpy as np
import matplotlib.pyplot as plt

def gauss_jordan(M):
    n = M.shape[0]

    for i in range(n):

        pivot_row = i + np.argmax(abs(M[i:, i]))
        M[[i, pivot_row]] = M[[pivot_row, i]]

        if M[i, i] == 0:
            return None

        M[i] = M[i] / M[i, i]

        for j in range(n):
            if i != j:
                M[j] = M[j] - M[j, i] * M[i]

    return M[:, -1]


#funcao a ser aproximada ln(x+1)
#aproximar por g(x)=ax²+bx+c

#funcoes bases phi1 = 1, phi2 = x e phi3 =x^2

#integrais
A = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
], dtype=float)

#Ax = b, integral de f(x)phi_i

B = np.array([
    2*np.log(2)-1,
    1/4,
    (2/3)*np.log(2)-5/18
])


M = np.hstack((A, B.reshape(-1,1))) #concatena
coef = gauss_jordan(M)

a, b, c = coef

print(f"g(x) = {a:.5f} + {b:.5f}x {c:+.5f}x²")

x = np.linspace(0,1,1000)

f = np.log(x+1)
g = a + b*x + c*x**2

plt.plot(x,f,label='ln(x+1)')
plt.plot(x,g,label='Aproximação')
plt.grid()
plt.legend()
plt.savefig("unidade_3/aprox_continues_case.png")
plt.show()

