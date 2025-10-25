import time

print ('SISTEMA DE PAGAMENTO DE COMISSÃO PARA VENDEDORES\n')

# Input vai receber o nome do vendedor
# Essa informação vna variável "vendedor"
vendedor = input('Nome do vendedor: ')
#Valor da meta
meta = 5000
#porcentagem de comissão
comissao = 0.03
FaturamentoVendedor = float(input('Faturamento de Maio: '))

print ('Carregando...')

time.sleep(5)

if FaturamentoVendedor >= meta:


    ValorComissao = FaturamentoVendedor * comissao
    ResultadoFinal = ValorComissao + FaturamentoVendedor
    print (f'\nVendedor: {vendedor}\nFaturamento: R${FaturamentoVendedor}\nPagar Comissão: {ValorComissao}\n\nResultado Final: {ResultadoFinal}')

else:

    print (f'\n{vendedor} não atingiu a meta. \n Favor se esforce mais em Junho')

time.sleep (2)
print('\nObrigado por utilizar nosso aplicativo.\nBy Projeto Fabrica de Programadores')