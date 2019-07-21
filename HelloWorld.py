#-*- coding:utf-8 -*-

print("Hello, World!")

# no python as variaveis são criadas no momento que são instanciadas
idade = 125
nome = "Alex {}"
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


#desta forma é possível criar strings com sequencias de caractesre
textoSa = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(textoSa)

#como na maioria das linguagens de programção as strings no python são vetores

trabalhoComSTR = ' Essa frase é um vetor'

print("terceira possição do vetor =>" ,trabalhoComSTR[3])



#pegar os valores entre as string

print("Vetores entre as str" ,trabalhoComSTR[2:5])

#retira os espaços do inicio string

print(trabalhoComSTR.strip())

# retorna o complimento da string

print(len(trabalhoComSTR))

#retorna tudo em minusculo
print(trabalhoComSTR.lower())

# retorna tudo em maiusculo 
print(trabalhoComSTR.upper())

#retorna a substituição de strings 
print(trabalhoComSTR.replace("E","V"))

#divide a string no meio suprimindo o elemento divisor
print(trabalhoComSTR.split("é"))

#divide a string em linhas 
print(textoSa.splitlines())

#para inserir numeros em string 
print(nome.format(idade))

#trabalho com STR formate
quantidade = 200
item = "Mel solis"
preco = 10.20

print("A quandidade é: {}, do {} tem o preço de {}".format(quantidade,item,preco))


#Operadores Aritimeticos 

#soma
print(1+2)
#subtração
print(1-2)
#divisão 
print(1/2)
#multiplicação
print(1*2)
#modulo
print(1%2)
#exponeciação
print(1**2)
#parte inteira da divisão
print(81//9)

#operadores de atribuição

x1 = 5
print(x1)
x1+=5
print(x1)
x1-=5
print(x1)
x1*=5
print(x1)
x1 /=5
print(x1)
x1%=5
print(x1)
x1+=5
print(x1)
x1**=5
print(x1)
bool(x1)
x1&=5
print(x1)





exit()