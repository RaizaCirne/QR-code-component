#Exemplo 01- Estrutura condicional simples - if
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!') #Esse print só acontece se o nome for Gustavo
print('Bom dia, {}!'.format(nome))

#Exemplo 02 - Estrutura condicional composta - if - else
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!') #Esse print só acontece se o nome for Gustavo
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

#Exemplo 03
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

#USANDO if SIMPLIFICADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!')