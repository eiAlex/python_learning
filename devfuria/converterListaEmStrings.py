# -*- encoding utf-8 -*- 

#para converter uma lista em string 
lista = ["Elemento1", "Elemento2", "Elemento3"]
var = ",".join(lista)
print(var)

#para converter uma lista de inteiros 
listaInteiros = [100, 200, 300]
print(str(listaInteiros))

#remover colchetes da lista 
print(str(lista).strip('[]'))