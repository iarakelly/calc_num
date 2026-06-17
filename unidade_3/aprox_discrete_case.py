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

#Gerando um intervalo de números para os pontos

x = np.arange(0, 50)

#Funçao para espalhar os pontos (com ruído)
y = 2 + 3*np.log(x+1) - 0.5*x + np.random.normal(0, 0.5, len(x))

#queremos aproximar de g(x)=a+bln(x+1)+cx

#funcoes base 1,ln(x+1),x

A = np.column_stack([
    np.ones(len(x)),
    np.log(x+1),
    x
])

#multiplica pela transposta (.T) e multiplica pela matriz (@)
#Ax = y
ATA = A.T @ A 
ATy = A.T @ y

#Ax = y

M = np.hstack((ATA, ATy.reshape(-1,1))) #concatena

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
plt.savefig("unidade_3/aprox_discrete_case.png")
plt.show()