#-*- coding:utf-8 -*-

print("Hello, World!")

# no python as variaveis são criadas no momento que são instanciadas
idade = 125
nome = "Alex"
sobrenome = 'Junio'

print(nome,sobrenome,idade)

# no python não existe um modo de comentarios multlinha mas tem um jeito 
"""
Este bem estranho digasse de passagem1
Desde Python irá ignorar strings literais que não são atribuídos a uma variável,
 você pode adicionar uma cadeia de linhas múltiplas (três aspas) no seu código, 
 e colocá-lo comentar dentro dele:

"""
#atribuindo valor a multiplas variáveis em uma linha 
x,y,z = 'uni', 'duni','thê'
print(x,y,z)

#É possível  atribuir um mesmo valor a diversas variáveis
d= 'Salamémingué'
a =b =c = d

print(a,b,c)



exit()