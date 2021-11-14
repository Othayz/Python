from math import hypot
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
print('Com o cateto oposto de {} e o cateto adjacente de {} a hipotenusa e de {:.2f}'.format(co,ca, hypot(co,ca)))
