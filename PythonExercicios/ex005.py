# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

# Minha resolução:
n = int(input('Digite um número: '))
s = n + 1
sub = n - 1
print('O número é {}, o seu sucessor é {} e o seu antecessor é {}'.format(n,s,sub))
#Comentários do código:
# Uei 3 variáveis
#OBS: Se precisarmos do sucessor e antecessor mais pra frente o ideal é guardar uma variável.


# Resolução em aula:
n = int(input('Digite um número: '))
print('Analisando o valor {}, se antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
#Comentários do código:
# Usei uma variável só, pois só vamos mostrar o resultado e vai acabar o programa
# Quanto menos variáveis, mais memória no dispositivo
# O objetivo não é só economizar memória.
# Se mais pra frente no programa eu precisasse do antecessor e sucessor para alguma coisa, eu seria obrigada a criar as variáveis para eles.


