# -*- coding utf-8 -*- 

dic = {1:'Janeiro', 2: 'Fevereiro', 3: 'Março'}

print(len(dic))

print(dic.items())

print(dic.values())

print(dic.keys())

dic1 = {4:'Abril', 5: 'Maio'}

dic.update(dic1)

print("Valores: %s" %dic)