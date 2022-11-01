#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza
#Obs: programa tem que funcionar pra qualquer tamanho de string.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() #split - pega nome inteiro e vai fatiar, dividir em pedaços separados por espaço
#print(nome[0]) #nome 0 vai ser o primeiro nome
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))
#len(nome) vou saber quantas posições tem nome
#Vai me mostrar o nome na posição len de nome -> (nome[len(nome) - 1]



