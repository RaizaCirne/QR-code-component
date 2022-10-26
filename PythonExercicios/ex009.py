#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

''''#Minha Resolução 01:
n = int(input('Digite um número: '))
t1 = n*1
t2 = n*2
t3 = n*3
t4 = n*4
t5 = n*5
t6 = n*6
t7 = n*7
t8 = n*8
t9 = n*9
t10 = n*10
print(' {}x1 = {} \n {}x2 = {} \n {}x3 = {} \n {}x4 = {} \n {}x5 = {} \n {}x6 = {} \n {}x7 = {} \n {}x8 = {} \n {}x9 = {} \n {}x10 = {}'.format(n,t1,n,t2,n,t3,n,t4,n,t5,n,t6,n,t7,n,t8,n,t9,n,t10))

#Minha Resolução 02:
n = int(input('Digite um número: '))
print(' {}x1 = {} \n {}x2 = {} \n {}x3 = {} \n {}x4 = {} \n {}x5 = {} \n {}x6 = {} \n {}x7 = {} \n {}x8 = {} \n {}x9 = {} \n {}x10 = {}'.format(n,(n*1),n,(n*2),n,(n*3),n,(n*4),n,(n*5),n,(n*6),n,(n*7),n,(n*8),n,(n*9),n,(n*10)))'''

#Resolução em aula:
num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*12) #print('-'*12) serve para escrever o traço 12 vezes. Replicar string


