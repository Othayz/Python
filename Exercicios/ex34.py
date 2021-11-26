salario = float(input('Qual o seu sálario? R$:'))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario*10/100)
print('Seu sálario com aumento passa de R$:{} para R$:{}'.format(salario,novo))
