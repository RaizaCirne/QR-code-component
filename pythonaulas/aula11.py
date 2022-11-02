# Cores no Terminal
# Padão ANSI (escape sequence)
# \033[style; texto; backm -> Para representar cores em Python

'''print('\033[31mOlá, Mundo!')
print('\033[31;43mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7:30mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('Os valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m!!!'.format(a, b))

#Usando outras maneiras 01

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))'''

#Usando outras maneiras 02 - criação de lista de cores - dicionário
nome = 'Guanabara'
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

#DESAFIO: Colocar cores em todos os exercícios


