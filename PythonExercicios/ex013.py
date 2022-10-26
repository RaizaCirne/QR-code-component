#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#Minha Resolução
s = float(input('Salário atual R$ '))
novo = s + (s*15/100)
print('O salário do funcionário é R${:.2f} e com 15% de aumento passou a ser R${:.2f} '.format(s,novo))

#Resolução em aula:
salário = float(input('Qual é o salário do Funcionário? R$ '))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário,novo))

#DESAFIO: Ler o preço de um produto e calcular qual é o preço dele com desconto para pagamento a vista e com aumento para parcelado.
#Pagando a vista tem 10% de desconto
#Parcelado tem 8% de aumento
preço = float(input('Digite o preço do produto R$ '))
vista = preço - (preço * 10 / 100)
print('Pagando a vista o produto de {:.2f} terá 10% de desconto e você irá pagar {:.1f}'.format(preço,vista))
parcelado = preço + (preço * 8 / 100)
print('Pagando o produto de {:.2f} parcelado você terá um aumento de 8% e irá pagar {:.2f}'.format(preço,parcelado))
