# -*- encoding: utf-8 -*- 

# a palavra reservada  "def" define uma função utilizando da palavra "pass" podedmos cria uma função inutil

def funcao():
    pass

# para criar um função com retorno 
def funcao2():
    return "Teste função"

print(funcao2())

#função com parâmetros 
def juntar(parte1, parte2):
    return parte1 + " " + parte2

print(juntar("Texto","Teste"))

#função de soma 
def soma(num1, num2):
    return num1 + num2

print(soma(2,2))

#pode-se juntar duas funções chamando as variaveis 
print(soma(num1 = 1, num2 =1))

