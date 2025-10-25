# Tupla
# Tuplas são listas IMUTÁVEIS (não altera)
import time

comida = ('sushi', 'macarrão', 'lasanha' , 'chocolate')

#print(comida)


'''# laço de repetição for
for i in comida:
    print(i)

print()

#laço for com range
# range (primeiro,último,saltos)
# teste: contador 1 até 10

for contagem in range(10,-1,-2):
    print(contagem)
    time.sleep(1)'''

# listas
# listas podem ser manipuladas
# criar listas com []

carros = ['Fusca', 'Montana', 'Marea', 'Onix Plus']

'''for estoque in carros:
    print(estoque)
    time.sleep(0.5)

carros.append('BMW\n') # append insere novo objeto na lista
print()

for estoque in carros:
    print(estoque)
    time.sleep(0.5)

print(carros[1]) #Localiza um objeto na lista via posição na matriz'''

carros.remove('Marea') # Remove o objeto informado da lista

print (carros[1])