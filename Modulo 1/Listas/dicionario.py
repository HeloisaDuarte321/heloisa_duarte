# Dicionários usam o conceito de chave valor

alunos = {
    'Aurora':'Excel Avançado',
    'Fabio':'Robótica',
    'Heloisa':'Excel Avançado',
    'Kauan':'Programa',
}

print(alunos)



for i in alunos:
    nome = input(str('Nome do aluno: '))
    if nome in alunos:
        print (alunos[nome])
    else:
        print('Não existe')

