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

numInt = 10 # numero inteiro
numFloat = 10.2 # numéro de pornto flutuante
numComplex = 1j # numéro complexo onda a parte imaginaria é representada por j
variSTR = 'String'

#conversões são feitas utilizando cast

convertFloar = float(numInt)
convertInt = int(numFloat)
convetComplex = complex(numComplex)

# importa um lib randam e gera um numéro randomico entre 1 e 10 
import random
numRandom = random.randrange(1,10) 

print (numRandom)

exit()