#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

#Minha resolução
m = float(input('Digite o tamanho em metros: '))
cm = m * 100
mm = m * 1000
print('O valor em metros é {}, em centímetros é {} e em milímetros é {}'.format(m, cm,mm))


#Resolução em aula:
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponte a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

#DESAFIO: FAZER TODAS AS MEDIDAS

#Minha resolução 01: metros em km, hm, dam, dm, cm e mm
m = float(input('Uma distância em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('A medida de {} corresponde a \n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(m,km,hm,dam,dm,cm,mm))

#Minha Resolução 02:
m = float(input('Uma distância em metros: '))
print('A medida de {} corresponde a \n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(m,(m/1000),(m/100),(m/10),(m*10),(m*100),(m*1000)))
