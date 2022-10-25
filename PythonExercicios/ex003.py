#Desafio 003
# Crie um programa que leia dois números e mostre a soma entre eles

#1ª Estratégia - incorreta
# O código não funciona, pois o + não está servindo como adição, mas como concatenação
# Mesmo que eu digite um número no input o valor é considerado uma string

n1 = (input('Digite um número: '))
n2 = (input('Digite mais um número: '))
s = (n1 + n2)
print('A soma vale', s)


#2ª Estratégia - correta -> Adicionando o tipo primitivo int

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = (n1 + n2)
print('A soma entre os números {} e {} vale {}'.format(n1, n2, s))

#Comentários sobre o código:

#Linha 16: n1 é a variável que recebe o input / tudo o que está dentro do int vai ser considerado como número inteiro
#Linha 17: Atribuimos o resultado desse input para a variável n2 / tudo o que está dentro do int vai ser considerado como número inteiro
#Vamos receber dois valores que serão armazenados na variável n1 e n2 respectivamente
#Linha 18: Colocamos as variáveis n1 + n2 dentro da variável s que representa a soma
#Lnha 18: A variável s recebe a soma entre n1 e n2
#Linha 19: print que é o comando para escrever na tela / {} Essas chaves é uma máscara que vai ser substituída pelo método da própria string / O s dentro do format é o que vai ser substituído e ser colocado na máscara {}

# Exemplo de números inteiros
# int -> 7, -4, 0, 9875
