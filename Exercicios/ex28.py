from random import  randrange 
from time import sleep
n = randrange(6)
print('-=-'*20)
print('Olá, bem vindo ao jogo da adivinhação!\ntente adivinhar em qual número eu estou pensando...\ndica: eu pensei em um número entre 0 e 5')
u=int(input('Em qual número eu pensei?'))
print('PROCESSANDO....')
sleep(5)
print('Eu pensei no número {}'.format(n))
if n==u:
    print('Parabéns você acertou em cheio uau!')
else:
    print('Que pena você errou!')
print('Quer jogar mais uma rodada?')
print('-=-'*20)
