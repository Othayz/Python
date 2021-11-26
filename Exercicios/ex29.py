v = float(input('Qual a sua velocidade?'))
m = (v-80)*7
if v > 80:
    print('Você ultrapassou o limete da via e foi multado em R${:.2f}'.format(m))
else:
    print('Você esta dentro do limite da via, tenha um bom dia!')
    
