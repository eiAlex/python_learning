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