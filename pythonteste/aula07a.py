'''#Exemplo 01
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

#Exemplo 02 -> Espaços
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
#Explicação código 02
#Linha 7: {:20} Ele escreveu o nome em 20 espaços

#Exemplo 03 -> Espaços a direita
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))
#Explicação código 03
#Linha 13: {:>20}   Com o sinal de maior fiz alinhamento do nome a direita em 20 espaços

#Exemplo 04 -> Epaços a esquerda
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))
#Explicação código 04
#Linha 19: Nome alinhado a esquerda dentro do espaço

#Exemplo 05 -> Espaço centralizado
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))
#Explicação código 05
#Linha 25: nome fica centralizado em 20 espaços

#Exemplo 06 -> Espaço, centralização e sinais de igual
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
#Explicação código 06
#Linha 31: nome em 20 espaços, centralizado e colocando iguais em volta

# OPERADORES ARITMÉTICOS
n1 = int(input('Um valor '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))

#OBS: Não usamos mais uma variável pra soma
#OBS1: Se for usar com variável é porque provavelmente você vai precisar desse resultado depois
#OBS2: Só quero pegar os números e somar, essa soma não vai servir pra mais nada, a não ser mostrar na tela.'''

#COM VARIÁVEL SOMA, MULTIPLICAÇÃO, DIVISÃO, DIVISÃO INTEIRA E EXPONENCIAÇÃO
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1/n2
di = n1//n2
e = n1**2
print('A soma é {},\n o produto é {} e a \n divisão é {:.3f}'.format(s,m,d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di,e))