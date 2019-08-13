# -*- coding: utf-8 -*-

#listas são sequências mutáveis  tambem conhecidos  como vetores

lista = [1,2,3,4]

lista2 = [5,6,7]

lista.extend(lista2)

print(len(lista))

print(lista.reverse())

print(lista.sort())

print(lista[2])

print(lista[2:4])

print(max(lista))

print(lista * 2)