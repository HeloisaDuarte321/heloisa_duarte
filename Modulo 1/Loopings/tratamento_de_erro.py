try:

    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    conta = n1 / n2

    print (f'Resultado de {n1} divido por {n2} = {conta}\n')

except ZeroDivisionError:
    print('Irmão, se ta de sacanagem né?')
except ValueError:
    print ('Não... Não é possível')