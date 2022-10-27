#Faça um programa que leia o comprimento do cateto oposo e do cateto adjacente de um triâncgulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

#Quanto temos um triangulo retangulo temos: cateto oposto, cateto adjacente, angulo de 90 graus e hipotenusa
#Princípio matemárico:
#O quadrado da hipotenusa é igual a soma do quadrado dos catetos

#Resolução em aula 01 - sem importação:
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)#hipotenusa é a raíz quadrada da soma do quadrado dos catetos
print('A hipotenusa vai medir {:.2f}'.format(hi))

#Resolução em aula 02 - com importação da classe math
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#hypot é um método dentro do módulo math para calcular hipotenusa que fica math.hypot(co,ca), se for fazer com from tirar o math. fica hypot(co.ca)
#Como estou usando só um método que é o hypot, posso importar da seguinte forma: from math import hypot
