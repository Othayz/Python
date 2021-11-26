print('Escreva 3 números e eu vou te dizer qual e o maior e qual e o menor!')
n1 = int(input('Número 1:  '))
n2 = int(input('Número 2:  '))
n3 = int(input('Número 3:  '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor número é {}\ne o maior é {}'.format(menor,maior))
