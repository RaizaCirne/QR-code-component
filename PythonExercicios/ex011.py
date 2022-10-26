#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.

#Minha Resolução:
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura * largura
q = area / 2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m² '.format(largura,altura, area))
print('Para pintar essa parede você precisará de {}l de tinta.'.format(q))

#Resolução em aula:
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta '.format(tinta))