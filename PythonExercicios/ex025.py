#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#OBS: pode ter silva em qualquer lugar - o resultado é True ou False

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

