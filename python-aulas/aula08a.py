#Ler um número e calcular a raíz quadrada desse número

#Exemplo 01 - Importando todas as funcionalidades com import math
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raíz quadrada de {} é igual a {:.2f}'.format(num, raiz))
#É possível calcular a raíz quadrada fazendo um expoente pra 1/2, mas vamos calcular importanto um módulo.
#Linha 2: Importanto o módulo math
#Linha 3: Pedindo um número ao usuário
#Linha 4: Criando variável raiz
#Linha 4: variável raiz recebe math.sqrt(num), que é a raíz quadrada do número digitado pelo usuário
#OBS: Poderia arrendondar pra cima o resultado com math.ceil(raiz) dentro do .formt no lugar que estaria apenas raiz da máscara na linha 5
#OBS: Poderia arrendondar pra baixo o resultado com math.floor(raiz) dentro do .formt no lugar que estaria apenas raiz da máscara na linha 5

#Exemplo 02 - Importando apenas uma funcionalidade com from math import sqrt
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz quadrada de {} é igual a {:.2f}'.format(num, floor(raiz)))
#Linha 18: Fazer a importação de uma funcionalidade, já traz o método direto pra pasta, não precisa usar math.sqrt(num), posso colocar apenas sqrt(num)

#Exemplo 03 - Funcionalidade do módulo random com random.random()
import random
num = random.random()
print(num)
#Linha 24: Importando biblioteca random
#Linha 25:  random.random() o computador me dá um número aleatório
#Linha 26:  Mostra número na tela
#Ao executar o computador gera o número 0.39210399040282606
#Gera esse número pois o método random da classe random gera um número float, real aleátorio entre zero e um

#Exemplo 04 - Funcionalidade do módulo random com random.randint()
import random
num = random.randint(1, 10)
print(num)
#Linha 35: randint(1, 10) para randomizar número inteiro de 1 até 10
# Com num = random.randint(1, 10) o computador vai chutando valores de 1 até 10