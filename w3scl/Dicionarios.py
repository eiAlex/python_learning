# -*- coding utf-8 -*- 

dic = {1:'Janeiro', 2: 'Fevereiro', 3: 'Março'}

print(len(dic))

print(dic.items())

print(dic.values())

print(dic.keys())

dic1 = {4:'Abril', 5: 'Maio'}

dic.update(dic1)

print("Valores: %s" %dic)

for i in dic:
    if dic[i] == dic[5]:
        dic1 = {6:'junho', 7: 'Julho'}

print(dic1)

dict_cadastro =  {"joao":18,"maria":15, "Alex":15}

contatos_lista = {('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')}

dict_lista = dict(contatos_lista)


print(type(dict_lista))

print(dict_lista)

for i in dict_lista:
    if dict_lista[i] == dict_lista['Ana']:
        print(i)
    else:
        print(1)