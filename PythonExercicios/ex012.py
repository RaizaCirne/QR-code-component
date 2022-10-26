#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Minha Resolução:
valor = float(input('Qual é o preço do produto? R$ '))
vf = valor - (0.05 * valor)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor,vf))

#Resolução em aula:
preço = float(input('Qual é o preço do produto? R$ '))              #Li o preço
novo = preço - (preço * 5 / 100)                                    #O novo preço vai ser o preço menos 5 porcento do preço
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f} '.format(preço,novo))

#Cálculo de porcentagem - TREINO:
# Quanto é 5% de 10?    10*5/100   == 0.5
# Quanto é 25% de 200?  200*25/100 == 50.0
# Quanto é 15% de 350?  350*15/100 == 52.5
# Quanto é 3% de 45?    45*3/100   == 1.35
# Quanto é 5% de 548?   548*5/100  == 27.24
# Quanto é 45% de 950?  950*45/100 == 427.5
# Quanto é 30% de 234?  234*30/100 == 70.2
# Quanto é 12% de 579?  579*12/100 == 69.48
# Quanto é 7% de 820?   820*7/100  == 57.4
# Quanto é 24% de 498?  498*24/100 == 119.52