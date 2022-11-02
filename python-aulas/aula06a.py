#Exemplo
n1 = int(input('Digite um valor: '))
print(type(n1))

# O tipo primitivo de uma variável deve ser especificada
#Linha 2: int() estou convertendo tudo o que está dentro dele para o tipo primitivo int que é inteiro
#Linha 3: type() mostra o tipo primitivo do valor atribuído a variável n1

# Exemplo do ex003 da pasta PythonExercicios

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
#print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma vale entre {} e {} vale {}'.format(n1, n2, s))

#Comentários sobre o código

#Linha 15: Usando máscaras para deixar o código mais simples

