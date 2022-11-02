#Exemplo 01:
frase = 'Curso em Vídeo Python'
print(frase)
#Comentários:
#Linha 3: Vai aparecer a frase na tela

#Exemplo 02 - Fatiar
frase = 'Curso em Vídeo Python'
print(frase[3])
#Comentários:
#Linha 9:
# - frase[3] é a 4ª letra, ou seja, letra s.

#Exemplo 03:
frase = 'Curso em Vídeo Python'
print(frase[3:13])
#Comentários:
#Linha 16:
# - [3:13] Vai da 4ª letra até a letra 13 que vai até o nº 12, que é a 13ª letra (conta com espaços)

#Exemplo 04:
frase = 'Curso em Vídeo Python'
print(frase[:13])
#Comentários:
#Linha 23:
# [:13] - Vai do início até a letra 12

#Exemplo 05:
frase = 'Curso em Vídeo Python'
print(frase[13:])
#Comentários
#Linha 30:
# [13:] Vai do 13 até o final

#Exemplo 06:
frase = 'Curso em Vídeo Python'
print(frase[1:15])
#Comentários
#Linha 37:
# [1:15] Vai da letra 1 à 15, eliminando o 15 e lê a letra 14.

#Exemplo 07:
frase = 'Curso em Vídeo Python'
print(frase[1:15:2])
#Comentários
#Linha 44:
# [1:15:2] Vai da letra 1 à 15, eliminando o 15 e lê a letra 14 e pula de 2 em 2.

#Exemplo 08:
frase = 'Curso em Vídeo Python'
print(frase[1::2])
#Comentários
#Linha 51:
# [1::2] - Vai da letra 1 até o final, pois o :: no meio não sabe o final, mas pula de 2 em 2

#Exemplo 09:
frase = 'Curso em Vídeo Python'
print(frase[::2])
#Comentários:
#Linha 58:
# [::2] Não sei o início nem o final - Mostra a string inteira pulando de 2 em 2.

#Exemplo 10: Para printar na tela textos grandes usar 3 aspas """ no início e no fim do texto.
print("""Welcome! Are you completely new to programming? If not then we presume you will be looking for information
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
It's also easy for beginners to use and learn, so jump in!""")

#Exemplo 11: Tudo no python é objeto
frase = 'Curso em Vídeo Python'
print(frase.count('o'))
#Comentários
#Linha 72: frase.count('o') mandei contar contas vezes aparece a letra o minúsculo.

#Exemplo 12: Tudo no python é objeto
frase = 'Curso em Vídeo Python'
print(frase.count('O'))
#Comentários
#Linha 78: frase.count('o') mandei contar contas vezes aparece a letra O MAIÚSCULO.
#OBS: Não tem O MAIÚSCULO na frase.

#Exemplo 13: Tudo no python é objeto
frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))
#Comentários
#Linha 85:
# frase.upper().count('O') significa pegar a frase, jogar pra MAIÚSCULO e contar quantas vezes tem O MAIÚSCULO.

#Exemplo 14:
frase = '   Curso em Vídeo Python   '
print(len(frase))
#Comentários
#Linha 92:
# len(frase) - Função interna len() pra ver qual é o tamanho da frase - ISSO É MUITO ÚTIL
# Se colocar espaços no início e final da frase ele aumenta o lanf '   Curso em Vídeo Python   '

#Exemplo 15:
frase = '   Curso em Vídeo Python   '
print(len(frase.strip()))
#Comentários
#Linha 100:
# strip() remove espaços indesejados

#Exemplo 16:
frase = '   Curso em Vídeo Python   '
print(frase.replace('Python', 'Android'))
#Comentários
#Linha 107:
# replace() Trocar Python por Android

#Exemplo 17:
frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)
#Comentários
#OBS: Uma string em seus microelementos é imutável,
# a não ser que eu utilize uma função de transformação de string e faça uma ATRIBUIÇÃO.

#Exemplo 18:
frase = 'Curso em Vídeo Python'
print('Curso' in frase)
#Comentários
#Linha 122:
#print('Curso' in frase) - Verificar se a palavra Curso está dentro da frase

#Exemplo 19:
frase = 'Curso em Vídeo Python'
print(frase.find('Curso'))
#Comentários
#Linha 129:
# find() Verifica a posição da frase 'Curso'.

#Exemplo 20:
frase = 'Curso em Vídeo Python'
print(frase.find('Vídeo'))
#Comentários
#Linha 136:
# find() Verifica a posição da frase 'Vídeo'.

#Exemplo 21:
frase = 'Curso em Vídeo Python'
print(frase.find('vídeo'))
#Comentários
#Linha 143:
# find() Verifica a posição da frase 'vídeo', mas não existe vídeo com o v minúsculo na frase, então fica -1.

#Exemplo 22:
frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))
#Comentários
#Linha 150:
# #Comentários
# #Linha 150:
#find() Verifica a posição da frase 'vídeo', mas não existe vídeo com o v minúsculo na frase.
#Consigo jogar a frase 'vídeo' pra minúsculo com lower()
#frase.lower().find('vídeo')

#Exemplo 23:
frase = 'Curso em Vídeo Python'
print(frase.split())
#Comentários
#Linha 161:
#frase.split() - Escreve na tela a frase splitada - Cria uma lista

#OUTRA FORMA
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido)

#OUTRA FORMA
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])
#print(dividido[0] mostra o primeiro item da lista.

#OUTRA FORMA
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])
#print(dividido[2][3]) Pega o segundo item da lista e mostre a letra 3.





