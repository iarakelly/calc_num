import numpy as np
import sys

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
    
    # A solução está na última coluna
    return M[:, -1]

def calcular_residuo(A_orig, b_orig, x):
    # r = b - Ax
    return b_orig - np.dot(A_orig, x)

# --- Fluxo Principal ---
if len(sys.argv) < 2:
    print("Uso: python esc.py m1.in")
    sys.exit(1)

with open(sys.argv[1]) as arq:
    lines = arq.readlines()

# n é o primeiro valor do arquivo
n = int(lines[0].strip())
# Matriz aumentada completa do arquivo
dados = np.array([[float(x) for x in line.split()] for line in lines[1:]])

# Separamos A e b originais para o refinamento
A_orig = dados[:, :n]
b_orig = dados[:, n]

# 1. Primeira solução com Gauss-Jordan
M_copy = dados.copy()
x_inicial = gauss_jordan(M_copy)

# 2. Refinamento Iterativo
# Calculamos o resíduo: r = b - Ax
residuo = calcular_residuo(A_orig, b_orig, x_inicial)

# Resolvemos o sistema A * d = r para achar a correção 'd'
# Criamos uma nova matriz aumentada [A | residuo]
M_refinamento = np.hstack((A_orig.copy(), residuo.reshape(-1, 1)))
d = gauss_jordan(M_refinamento)

# Nova solução: x_novo = x_antigo + d
x_final = x_inicial + d

# --- Análise de Impacto ---
norma_inicial = np.linalg.norm(residuo)
residuo_final = calcular_residuo(A_orig, b_orig, x_final)
norma_final = np.linalg.norm(residuo_final)

print(f"Solução inicial: {x_inicial}")
print(f"Solução após refinamento: {x_final}")
print("-" * 30)
print(f"Norma do Resíduo Inicial: {norma_inicial:.2e}")
print(f"Norma do Resíduo Final:   {norma_final:.2e}")
print(f"Melhoria: {((norma_inicial - norma_final) / norma_inicial * 100):.4f}%")