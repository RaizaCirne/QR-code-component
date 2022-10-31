#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúscylas
#O nome com todas minúsculas.
#Quantas letras ao todoo (sem considerar espaços)
#Quantas letras tem o primeiro nome.

#Resolução em aula:

nome = str(input('Digite seu nome completo: ')).strip() #Vai eliminar espaços antes e depois do nome
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))#Verifica quantidade de letras com o espaço menos o contador de espaços.
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() #split gera uma lista cim todas as palavras de uma cadeia de caractere
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))