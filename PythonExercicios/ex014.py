#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

'''#Minha Resolução:
c = float(input('Informe a temperatura em ºC: '))
f = (9 * c) / 5 + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(c, f))

#Resolução em aula 01:
c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(c, f))'''

#Resolução em aula 02:
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(c, f))

#Comentários sobre o código:
#Multiplicação e divisão tem a mesma ordem de precedência
#Em uma expressão acontece quem vem primeiro
#Nesse caso específico não precisa de parêntes como está na Resolução em aula 01
#A ordem de precedência dessa expressão f = 9 * c / 5 + 32 é a ordem que os operadores aparecem
#É bom utilizar os parênteses porque fica mais fácil de ler a expressão
#Você diz exatamente o que quer que aconteça primeiro


