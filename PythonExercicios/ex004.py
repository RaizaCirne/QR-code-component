#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite algo: ')
print('Você digitou: {} '.format(a))
print('O tipo primitivo desse valor é {} '.format(type(a)))
print('Só tem espaços? {} '.format(a.isspace()))
print('É um número? {} '.format(a.isnumeric()))
print('É alfabético? {} '.format(a.isalpha()))
print('É alfanumérico {} '.format(a.isalnum()))
print('Está em maiúsculas? {} '.format(a.isupper()))
print('Está em minúsculas? {} '.format(a.islower()))
print('Está capitalizada? {} '.format(a.istitle()))

#Comentários sobre o Código
#Linha 4: Tipo primitivo vai ser sempre str, pois a função input retorna sempre uma string independente do tipo
#Linha 6: Posso testar mesmo sendo uma string se o que foi digitado pode ser um número, por exemlo.
#OBS: Nesse código o "a." é sempre o que chamamos de objeto
#OBS2: Todoo objeto tem características e realiza funcionalidade / Temos atributos e métodos.
#OBS3: Como tem parênteses em cada um deles, estamos trabalhando método.
#OBS4: Todoo objeto string tem esses métodos -> isspace(); a.isnumeric(); a.isalpha() e etc.