#Crie um programa que leia um número inteiro e mostre na tela se ela é PAR ou ÍMPAR.
número = int(input('Me diga um número qualquer: '))
resultado = número % 2 # Todoo número par vai dar resultado 0. Todoo número ímpar vai dar resultado 1
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))
#O resto da divisão de qualquer número par por 2 é zero
#O resto da divisão de qualquer número ímpar por 2 é igual a 1