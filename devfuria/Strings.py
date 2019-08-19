# -*- coding utf-8 -*-
# no python tudo é objeto e uma string é denominada STR

#Type
# <class 'str'> 

#Como uma str é um vetor podemos acessar seus elementos por indexs

print("python"[0])
print("python"[1])
print("python"[2])
print("python"[3])
print("python"[4])
print("python"[5])

# porem não é possivel alterar o valor de um atributo inserido no index 
palavra = 'cas'
#pavra[4] ='a'
# TypeError: 'str' object does not support item assignment

#Strigns são objetos interáveis 

for letras in "palavra":
    print(letras)

# É possivel fatiar Strings (pois elas são vetores)
palavra = "AZURE"
print(palavra[2:4])

#Para concatenar Strings se utiliza o "+""
txt = "Microsoft " + palavra
print(txt)

#É possivel pesquisar dentro de Strings
print('a' in 'abc')
print('d' in 'abc')

print('a' not in 'abc')
print('d' not in 'abc')

#Mostrar tamanho de uma string 
print(len("Abacate"))

# Caixa alta
print("banana".upper())

#caixa baixa
print("ABACAXI".lower())

#conversão de STR, no python todos objetos são cast de conversão
num = 12345
print(type(num))
print(type(str(num)))

#Checando se a string possui apenas letras 
print("AbCDwe".isalpha())
print("ABc12E".isalpha())
print("AbXsd2+=w123,%".isalnum())

# Para retirar espaços no inicio da string
print("   A lua cheia".strip())

#juntar elementos da String
elementos = "abc"
print("-".join(elementos))

#É possivel fazer join em lista 
ListaNome = ["Alex", "Alessandra", "Lucia"]
print(" * ".join(ListaNome))

#O Split é um separador inverso do join
s = "n o m e"
print(s.split())
print(s.split("  "))