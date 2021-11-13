d=float(input('Por Quantos dias você alugou o carro?'))
km=float(input('Quantos Km você rodou com o carro?'))
p= ((d*60)+(km*0.15))
print('Pague R$ {:.2f}'.format(p))
