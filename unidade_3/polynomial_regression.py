import numpy as np
import matplotlib.pyplot as plt

def gauss_jordan(M):
    n = M.shape[0]
    # Matriz aumentada [A|b]
    for i in range(n):
        # Pivotamento parcial: busca o maior elemento na coluna para reduzir erros
        pivot_row = i + np.argmax(abs(M[i:, i]))
        M[[i, pivot_row]] = M[[pivot_row, i]]
        
        if M[i, i] == 0:
            return None # Matriz singular
        
        # Normaliza a linha do pivô para que o pivô seja 1
        M[i] = M[i] / M[i, i]
        
        # Elimina os outros elementos da coluna i (acima e abaixo do pivô)
        for j in range(n):
            if i != j:
                M[j] = M[j] - M[j, i] * M[i]
    
    return M[:, -1]

x = np.sort(np.random.randint(0, 100, 100))

y = 2*x**2 - 3*x + 5 + np.random.normal(0, 1200, len(x))

#aproximar de uma função p(x)=ax^2+bx+c

#Todos os somatõrios

sum_x4 = sum(xi**4 for xi in x)
sum_x3 = sum(xi**3 for xi in x)
sum_x2 = sum(xi**2 for xi in x)

sum_x = sum(xi for xi in x)
sum_y = sum(yi for yi in y)


sum_xy = sum(xi*yi for xi, yi in zip(x, y))
sum_x2y = sum((xi**2)*yi for xi, yi in zip(x, y))

n = len(x)

#Ac=B

A = np.array([
    [sum_x4, sum_x3, sum_x2],
    [sum_x3, sum_x2, sum_x ],
    [sum_x2, sum_x , n  ]
])

B = np.array([
    sum_x2y,
    sum_xy,
    sum_y
])


#matriz aumentada

M = np.hstack((A, B.reshape(-1,1)))

coef = gauss_jordan(M)

a = coef[0]
b = coef[1]
c = coef[2]

print(f"p(x) = {a:.4f}x² + {b:.4f}x + {c:.4f}")

y_reg = a*x**2 + b*x + c

plt.scatter(x, y, label="Dados")
plt.plot(x, y_reg, label="Regressão")

plt.legend()
plt.savefig("unidade_3/polynomial_regression.png")
plt.show()