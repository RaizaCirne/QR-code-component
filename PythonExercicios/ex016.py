#Crie um programa que leia um número Real qualquer pelo teclado e mostre a sua porção inteira
#Dica: Olhar todas as funções que tem dentro da classe do módulo math

#Minha Resolução:
from math import trunc

num = float(input('Digite um número: '))
i = trunc(num)
print('O número {} tem a parte inteira {}'.format(num, i))

#FORMAS DE RESOLUÇÃO

#Resolução em aula 01:
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

#Resolução em aula 02:
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

#Usei a função int que é a parte inteira do número
#int(num) mostra na tela a parte inteira do número digitado pelo usuário



