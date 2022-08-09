<<<<<<< HEAD
import math
import numpy as np
import matplotlib.pyplot as plt

a = float(input("digite o termo A da equação "))
b = float(input("digite o termo B da equação "))
c = float(input("digite o termo c da equação "))

delta= b**2 - (4*a*c)

d = (-(b) + math.sqrt(delta) ) / 2*a
e = (-(b) - math.sqrt(delta) ) / 2*a

print("X1 é igual {} e X2 é igual a {} e delta é igual a {} ".format(d,e, delta))



eixo_x = []
eixo_y = []
zero = []

variacao = abs(d - e)
if variacao < 3:
    variacao = 3
print(variacao)

for x in np.arange(d - variacao, e + variacao, variacao / 100):
    y= a * (x ** 2 ) + b * (x) + c
    eixo_x.append(x)
    eixo_y.append(y)
    zero.append(0.0)
plt.plot(eixo_x,eixo_y,color="blue")
plt.plot(eixo_x,zero,color="black")
=======
import math
import numpy as np
import matplotlib.pyplot as plt

a = float(input("digite o termo A da equação "))
b = float(input("digite o termo B da equação "))
c = float(input("digite o termo c da equação "))

delta= b**2 - (4*a*c)

d = (-(b) + math.sqrt(delta) ) / 2*a
e = (-(b) - math.sqrt(delta) ) / 2*a

print("X1 é igual {} e X2 é igual a {} e delta é igual a {} ".format(d,e, delta))



eixo_x = []
eixo_y = []
zero = []

variacao = abs(d - e)
if variacao < 3:
    variacao = 3
print(variacao)

for x in np.arange(d - variacao, e + variacao, variacao / 100):
    y= a * (x ** 2 ) + b * (x) + c
    eixo_x.append(x)
    eixo_y.append(y)
    zero.append(0.0)
plt.plot(eixo_x,eixo_y,color="blue")
plt.plot(eixo_x,zero,color="black")
>>>>>>> 012c43aa5a6c37e2c2eaa713eb3481e76bdce1cd
plt.show()