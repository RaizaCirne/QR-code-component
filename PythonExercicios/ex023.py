#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: Digite um número: 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
#Tentar fazer como string e matematicamente: Tem as duas possibilidades, ver qual é melhor.

#Resolução 01 - com string - Dá problema se colocar números com menos de 4 digítos
num = int(input('Digite um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena : {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

#Resolução 02 - matematicamente
num = int(input('Digite um número: '))
u = num // 1 % 10 #Fazer divisão inteira do número por 1 e fazer módulo de 10, ou seja, divido o numero por 10 e pego o resto da divisão que é o que sobrou, que é a unidade
d = num // 10 % 10 #Dividir por 10 e pegar o resto
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena : {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
