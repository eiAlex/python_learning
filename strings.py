nome = "Álex"
print(type(nome))

# F string, te de ser chamado sem espaços pode-se realizar operações dentro da string
print(f'Olá {nome} {1+2}')

#arredondando  este print f lembra muito C
x = 1.6155698558
print(f"O numero de ouro é {x:.2f}" )

#como uma string é um vetor podemos percorrelo
print(nome[2])

#todos os atributos do objeto
print(dir(str))
