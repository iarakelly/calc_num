import numpy as np
import matplotlib.pyplot as plt

x = [10, 7, 3, 12, 1]
y = [15, 13, 9, 5, 2]

plt.scatter(x, y, color="red", label="pontos")

sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum(xi**2 for xi in x)
sum_xy = sum(xi*yi for xi, yi in zip(x, y))
n = len(x)


a = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
b = (sum_y - a*sum_x) / n

print(f"sum_x: {sum_x}, sum_y: {sum_y}, sum_x2: {sum_x2}, sum_xy: {sum_xy}")    

print(f"y = {a:.4f}x + {b:.4f}")

reg_linear = [a * xi + b for xi in x]

# 3. Plotar o gráfico e exibir
plt.plot(x, reg_linear, color='blue', label=' y = 0.4648x + 5.7324')
plt.title("Gráfico da Função Linear")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.legend()

plt.show()