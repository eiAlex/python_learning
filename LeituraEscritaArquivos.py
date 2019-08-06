# -*- coding:utf-8 -*- 

#manipulação de arquivos é muito importante para qualquer liguagem de programação
#No python a função open() tem dois parâmetros; filename ; e modo
# Dos modos existem 4 
# r - de read - abre um aquivo e modo leitura, caso o arquivo não exista uma exeção é disparada
# a - de append - abre um aquivo ou cria um caso não exista para anexar informção
# w - de write - abre um arquivo sobreescrevendo ou cria um caso não exista para adicionar informção
# x - de create - cria um arquivo, retorna erro caso o arquivo exista

#também pode-se especificar  se o  arquivo a ser manuseado é modo binario ou texto
# t -  texto 
# b - binario

#leitura de um arquivo
f = open("demofile.txt","r")
print(f.read())

#imprimir os 5 primeiros itens da string carregada 
print(f.read(5))

#Realizar print de linhas separadas
print(f.readline())
print(f.readline())
print(f.readlines())

# Fechar o arquivo aberto 

f.close()

# Escrever um arquivo 

a = open("testefile.txt", "w")
a.write("Now the file has more content!")
a.close()

arquivo = open("arquivo.txt", "w")

arquivo.write("Essa é a primeira linha escrita por nós. \n")
arquivo.write("Essa é a nossa segunda linha.")
arquivo.write("Essa deveria ser a terceira linha porém ainda é a segunda. \n")
arquivo.write("Essa sim é a terceira.")

arquivo.close()

#lendo aqrquivo criado 

txt  = open("Arquivo.txt", "r")
txt1 = txt.read()
txt.close()

print(txt1)

#Excluir um arquivo
#para excluir um arquivo, deve-se importar o modulo OS, executar o método os.remove():

import os
os.remove("Arquivo.txt")

# verifica se o arquivo existe 

print(os.path.exists("Arquivo.txt"))

# criar uma pasta 
os.mkdir("Pasta")

# Remove uma pasta 
os.rmdir("Pasta")