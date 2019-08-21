# -*- encoding utf-8 -*- 

# Sequências são coleções ordenadas embutidades em: strings, listas, turplas e buffres.
#indices são iniciados em 0 

p = "python"

#fatiar pegando os três primeiros elementos da string
print(p[:3])

#é possivel pegar os elementos de forma reversa 
print(p[-1])

#Com comprimento utilizando operadores inclusivos e exclusivos
print(p[4:6])

#é possuive realizar a checagem de estados 
print((p == p[0:6]))
print((p == p[:6]))
print((p == p[:]))

#tabem temos o tamanho 
print(len(p))

#retorna o minino 
print(min(p))

#retorna o maximo
print(max(p))

#retorna um objeto ordenado
print(sorted(p))

#retorna o interator reverso
print(reversed(p))