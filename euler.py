import numpy as np
import matplotlib.pyplot as plt

#função original
def f_real(x):
    return x * np.cos(x) + 1

#derivada conhecida (f'(x))
def df(x):
    return np.cos(x) - x * np.sin(x)

x0, y0 = 0, 1        # Ponto inicial conhecido f(0) = 1
x_final = 6          # Fim do intervalo
h = 0.5              # Tamanho do passo (pode diminuir para aumentar a precisão)

# Listas para armazenar os pontos estimados
x_euler = [x0]
y_euler = [y0]

# Loop do Método de Euler
x_atual = x0
y_atual = y0

while x_atual < x_final:
    # Calcula a inclinação no ponto atual
    inclinacao = df(x_atual)
    
    # Próximo y = y atual + passo * derivada
    y_proximo = y_atual + h * inclinacao
    x_proximo = x_atual + h
    
    # Armazena os resultados
    x_euler.append(x_proximo)
    y_euler.append(y_proximo)
    
    # Atualiza para a próxima iteração
    x_atual = x_proximo
    y_atual = y_proximo

# Preparação dos dados para o gráfico da função real (curva suave)
x_curva = np.linspace(0, 6, 100)
y_curva = f_real(x_curva)

plt.figure(figsize=(10, 6))
plt.plot(x_curva, y_curva, label='Função Real: $x \cdot \cos(x) + 1$', color='blue', linewidth=2)
plt.plot(x_euler, y_euler, 'ro-', label=f'Estimativa Euler (h={h})', markersize=5)

plt.title('Método de Euler vs Função Real')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()