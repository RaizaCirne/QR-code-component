#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

#Minha Resolução
dias = int(input('Quantos dias alugados? '))
km = float(input('Quandos km rodados? '))
valor = (60*dias) + (0.15*km)
print('O total a pagar é de R${:.2f}'.format(valor))

#Resolução em aula:
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

#Sempre que tiver um problema dividir em pequenas tarefas:
#1º - Descobrir o preço a pagar sabendo que o carro custa R$60 por dia (dias * 60)
#2º - Descobrir o preço a pagar sabendo que são R$0.15 por km rodado (km * 0.15)
#3º - Fazer a soma do resultado entre eles.

#1º Realizar primeira tarefa e fazer teste
# Se der errado o primeiro problema, já saberá que o erro está ali
#Criar pequenos módulos de funcionamento dentro do código