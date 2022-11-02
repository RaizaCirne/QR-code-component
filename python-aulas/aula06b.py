#Exemplo 01
n = float(input('Digite um valor: '))
print(n)
#Explicação sobre o códido do exemplo 01:
#Linha 3: O resultado aparece como ponto flutuante por causa do tipo primitivo float


#Exemplo 02
n = str(input('Digite um valor: '))
print(type(n))
#Explicação sobre o códido do exemplo 02:
#Linha 10: O resultado aparece como string, por causa do tipo primitivo str
#OBS: Sem o str já seria string, pois é o padrão.


#Exemplo 03
n = bool(input('Digite um valor: '))
print(type(n))
#Explicação sobre o códido do exemplo 03:
#Linha 18: O resultado parece como boleano, por causa do tipo primitivo bool

#Exemplo 04
n = bool(input('Digite um valor: '))
print(n)
#Explicação sobre o códido do exemplo 04:
#Linha 24: O resultado parece como True, por causa do tipo primitivo bool.
#O valor boleano só aceita verdadeiro e falso.
# Se eu só der enter e não digitar valor nenhum, ele vai me retornar False

#Exemplo 05
n = input('Digite um valor: ')
print(type(n))
#Explicação sobre o códido do exemplo 05:
#Linha 32: Independente do valor digitado será uma string

#Exemplo 06
n = input('Digite algo: ')
print(n.isalnum())
#Explicação sobre o códido do exemplo 06:
#Linha 39: Dentro do print queremos saber se o n é um número.
#Linha 37: Se eu digitar 3 ele vai retornar True (é numérico)
#Linha 37: Se eu digitar Oi ele vai retornar False (Não é numérico)
#Linha 37: Se eu digitar 3a ele vai retornar False (Não é numérico)
#Linha 38: O isalnum() vai dizer se é possível converter esse valor digitado em um número com o tipo primitivo int antes dele.

#Exemplo 07
n = input('Digite algo: ')
print(n.isalpha())
#Explicação sobre o códido do exemplo 07:
#Linha 48: isalpha() vai dizer se é letra.
#Linha 47: Se eu digitar www ele vai retornar True (É letra)
#Linha 47: Se eu digitar 123 ele vai retornar False (Não é letra. Tem somente números)
#Linha 47: Se eu digitar 3a ele vai retornar False (Ele não é alpha, é alpha numérico)

#Exemplo 08
n = input('Digite algo: ')
print(n.isalnum())
#Explicação sobre o códido do exemplo 08:
#Linha57: isalnum() vai dizer se é alpha numérico
#Linha56: Se eu digitar Oi ele vai retornar True (Ele é alfabético e numérico)
#Linha56: Se eu digitar 3a ele vai retornar True (Ele é alfabético e numérico)
#Linha56: Se eu digitar 7 ele vai retornar True (Ele é alpha numérico)
#Linha56: Se eu digitar "espaço" ele vai retornar False (Não é alpha numérico)

#Exemplo 09
n = input('Digite algo: ')
print(n.isupper())
#Explicação sobre o códido do exemplo 09:
#Linha67: isupper() vai dizer se são apenas letras maiúsculas
#Linha66: Se eu digitar Oi ele vai retornar False (Tem letra maiúscula e minúscula)
#Linha66: Se eu digitar OI ele vai retornar True (Apenas letra maiúscula)

#OBSERVAÇÕES: Quando lemos apenas com input o tipo vai ser sempre string. Se formos converte-lo pra outra coisa a história muda