# usuário informa o nome
nome = input('Informe o sue nome completo: ')

#separa as palavras do nome e capitula
nome_lista = nome.split(' ')

#capitular as palavras do nome
for i in range(len(nome_lista)):
    nome_lista[i] = nome_lista[i].capitalize()
    
#junta o nome em uma variável
nome_completo = ' '.join(nome_lista)

#exibe na tela
print(nome_completo)