# -*- encodinf: utf-8 -*- 

#Dicionários são coleçõe, com mapeamento nativo do python A associação destes dicionários 
# é chave valor em que a chave é uma elemento imutável

#criando um dicionário, foi sobreescrevido
pessoa = {
    
    "ID" : 1,
    "nome" : "João",
    "idade" : 39,
    "linguagem" : "PT-BR",
    
    "ID" : 2,
    "nome" : "Maria",
    "idade" : 23,
    "linguagem" : "PT-PG"
}

#imprimindo o dicionário
print(pessoa["ID"])

#tamanho do diciário 
print(len(pessoa))

#outro dicionario 
mydict = {
    '1' : 'a',
    '2' : 'b',
    '3' : 'c'
}

#print de itens chave valor
print(mydict.items())

#print de chaves
print(mydict.keys())

#print valores
print(mydict.values())
