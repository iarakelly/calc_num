x = 1
n = 2

#for i in range(5):
    #x = x+(n-x*x)/(2*x)

    #print(f'Valor final: {x}') 

while(abs(x*x-n)>0.01):
    x = x+(n-x*x)/(2*x)
    print(x)
    