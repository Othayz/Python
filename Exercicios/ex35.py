print('Escreva o valor de 3 retas e eu direi se eles formam ou não um triãngulo!')
print(80*'=')
r1 = float(input('Escreva o valor da primeira reta:  '))
r2 = float(input('Escrava o valor da secunda reta:   '))
r3 = float(input('Escreva o valor da terceira reta   '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triãngulo!')
print(80*'=')
