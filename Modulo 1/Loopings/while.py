# Laço de repetição while (enquanto)

# Exemplo 1
# Enquanto o número não for "0" continye o laço
'''
numero = None

while numero != 0:
    numero = int(input('Digite um número: '))

print('\nObrigado por nada\n')
'''

while True:
    idade = int(input('Informe sua idade: '))
    if idade >= 18:
        print ('\nSeja bem vindo uhauhauahuah\n')
        print ('Vamos jogar !!!\n')
        continue
    else:
        print ('\nnananinannaumrapaiz...\n')
        print ('Vai colocar as fraldas filho\n')
        break

print ('Obrigado por usar nossos sistemas')