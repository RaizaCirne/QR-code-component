#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Minha resolução:
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O número é {}, seu dobro é {}, seu triplo é {} e sua raíz quadrada é {:.3f} '.format(n,d,t,r))

#Resolução em aula:
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n** (1/2)
print('O dobro de {} vale {}'.format(n,d))
print('O triplo de {} vale {}.\nA raíz quadrada de {} é igual a {:.2f} '.format(n, t, n, r))

#Resolução em aula de outras possibilidades:

# Possibilidade 01
n = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(n,(n*2)))
print('O triplo de {} vale {}.\nA raíz quadrada de {} é igual a {:.2f} '.format(n, (n*3), n, (n**(1/2))))

# Possibilidade 02 - Raíz quadrada com a função de pow
n = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(n,(n*2)))
print('O triplo de {} vale {}.\nA raíz quadrada de {} é igual a {:.2f} '.format(n, (n*3), n, pow(n, (1/2))))
