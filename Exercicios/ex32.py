a = int(input('Qual ano você quer analisar?'))
if (a%4==0 and a%100!=0) or (a%400==0):
    print('O ano {} e bissexto'.format(a))
else:
    print('O ano {} não e bissexto'.format(a))
