#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
#mostra quantos Dólares ela pode comprar
#Considere US$1,00 = R$3,27

#Minha Resolução 01:
di = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = di / 3.27
print('Com R${} você pode comprar U${:.2f} '.format(di,dolar))

#Minha Resolução 02:
di = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Com R${} você pode comprar U${:.2f} '.format(di, di/3.27))

#Resolução em aula:
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))

#DESAFIO 01: FAZER COM COTAÇÃO DO DÓLAR ATUAL
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolarhoje = float(input('Qual é a cotação do dólar hoje? U$ '))
dolar = real / dolarhoje
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real,dolar))

#DESAFIO 02: CONVERTER DE REAL PARA EURO - EURO EM 26/10/2022
real =float(input('Quanto dinheiro você tem na carteira? R$ '))
euro = real / 5.41
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real,euro))
