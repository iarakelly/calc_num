import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=0, stop=10, num=100)
y = np.sin(x)

plt.yticks([1,0,-1]) #marcação do eixo y
plt.axhline(y=0, color='black', linewidth=1) #marcação do eixo x
plt.plot(x, y, label='Function whitout noise') #plotagem da função
plt.legend() #legenda
plt.savefig('nonoise.png')

noise = np.random.normal(loc=0, scale=0.1, size=len(x)) #geração de ruído
#esta pegando cada ponto da curva anterior e gerando um intervalo normal, com media 0 e desvio padrão 1
y_noise = y + noise #adição do ruído à função

plt.plot(x, y_noise, label='Function whit noise')
plt.legend() #legenda
plt.savefig('withnoise.png')


y_conv= np.convolve(y_noise, np.ones(10)/10, mode='same') #convolução da função com ruído
plt.plot(x, y_conv, label='smooth ')
plt.legend() #legenda
plt.savefig('test1.png')

err_abs = np.abs(y - y_conv) #erro absoluto
plt.plot(x, err_abs, label='absolute error')
plt.legend() #legenda
plt.savefig('test2.png')