'''

Crie um aplicativo que permite a entrada na balada apenas para adultos

'''

print ('### BEM VINDO A BOATE TCHUTCHUCA ###')

idade = int(input('\nInforme sua idade: '))

if idade <= 10:
    print ('Mamãe ta chamando você para trocar a fralda')
elif idade <= 14:
    print ('Você tem a idade do meu filho, pode entrar não man')
elif idade <= 17:
    print ('Ano que vem você volta, fechou?')
else:
    'Pode entrar meu guerreiro'