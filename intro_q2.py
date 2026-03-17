import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=0, stop=10, num=100)
y = np.sin(x)

#plt.yticks([1,0,-1]) #marcação do eixo y
#plt.axhline(y=0, color='black', linewidth=1) #marcação do eixo x

plt.subplots_adjust(hspace=0.3)
plt.subplot(4,1, 1)
plt.plot(x, y, label='Function whitout noise') #plotagem da função
plt.legend(fontsize='small') #legenda
plt.savefig('figure.png')

noise = np.random.normal(loc=0, scale=0.1, size=len(x)) #geração de ruído
#esta pegando cada ponto da curva anterior e gerando um intervalo normal, com media 0 e desvio padrão 1
y_noise = y + noise #adição do ruído à função


plt.subplot(4, 1,2)
plt.plot(x, y_noise, label='Function whit noise') 
plt.legend(fontsize='small') #legenda
plt.savefig('figure.png')


y_conv= np.convolve(y_noise, np.ones(10)/10, 
mode='same') #convolução da função com ruído

plt.subplot(4,1,3)
plt.plot(x, y_conv, label='smooth ')
plt.legend(fontsize='small') #legenda
plt.savefig('figure.png')

err_abs = np.abs(y - y_conv) #erro absoluto
plt.subplot(4,1,4)
plt.plot(x, err_abs, label='absolute error')
plt.legend(fontsize='small') #legenda
plt.savefig('figure.png')

plt.subplots_adjust(hspace=1.5)