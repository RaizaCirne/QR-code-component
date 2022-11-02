#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
# Regra: Cada um desses segmentos tem que ser menor do que a soma do comprimento dos outros dois
# O r1 tem que ser menor do que a soma dos outros dois
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FOMAR tringulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

