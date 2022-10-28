#Faça um programa que leia um ângulo qualquer e mostre na tela no valor do seno, cosseno e tangente desse ângulo.

#Resolução em aula 01:
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo)) #Convertendo o ângulo digitado para radianos, pegar o ângulo convertido e calcular o seno dele.
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

#Resolução em aula 02:
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

'''
#Eixo vertical: senos
#Eixo horizontal: cossenos
#Projeções: projeção em pé do seno e deitado do cosseno

De acordo com o manual do python.org:
math.sin( x ) retorna o seno de x radianos.
math.cos( x ) retorna o cosseno de x radianos.
math.tan( x ) retorna a tangente de x radianos.
Por isso tenho que converter cada um deles para radiano com math.radians (x)
No caso da resolução 2 tiramos o math, pois sempre que importo dessa maneira (from math import radians, sin, cos, tan) não preciso referenciar o módulo.
'''