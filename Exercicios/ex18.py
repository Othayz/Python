from math import cos, sin, tan, radians
ângulo = int(input('Digite o Ângulo desejado!'))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {},\n possui o cossseno de {:.2f} \ne seno de {:.2f}\n e a tangente de {:.2f}'.format(ângulo,seno,cosseno,tangente))

