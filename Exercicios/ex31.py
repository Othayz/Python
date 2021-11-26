d = float(input('Quantos km tem seu trajeto?'))
if d <= 200:
    print('Você pagara R${} pela passagem!'.format(d*0.50))
else:
    print('Você pagara R${} pela passagem!'.format(d*0.45))
print('BOA VIAGEM!')
