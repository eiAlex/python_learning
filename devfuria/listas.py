#Uma lista (list) é uma sequêcia ou coleção ordenada de valofres, estes que  formam uma lista são chamados de elementos ou itens. 
#Lista são similares a strings, que são uma sequência de caracteres no entando bem diferente.



listaAnimains = ["Cachorro", "Gato", "Pato", "Galinha"]

#imprimir um elemento em uma determinada
print(listaAnimains[3])

#mostrar o tamanho da lista,
print(len(listaAnimains))

#mostrar uma lista
print(listaAnimains)

#podemos criar uma lista vazia
listaVazia = []

#precorrendo una lista (list looping)
for animais in listaAnimains:
    print(animais)

#percorrendo a lista numerada
for index, animais in enumerate(listaAnimains):
    print (index, animais)

#Uma lista pode ser copiada para outra 
lista_b = listaAnimains[:]
print(lista_b)

#duas lista podem ser juntadas
lista_c = listaAnimains + lista_b + listaVazia
print(lista_c)

#adicionando elementos a uma lista
#um elemento
lista_c.append("Rato")

#definido um index
lista_c.insert(0,"Barata")
print(lista_c)

#Remover um elemento 
lista_c.remove("Barata")
print(lista_c)

#Remove ultimo elemento da list
lista_c.pop()
print(lista_c)

#remove um elemento pleo index
del(lista_c[2])
print(lista_c)

#ordenar uma lista 
lista_c.sort()
print(lista_c)

#ordenar a lista como sorted
print(sorted(listaAnimains))
