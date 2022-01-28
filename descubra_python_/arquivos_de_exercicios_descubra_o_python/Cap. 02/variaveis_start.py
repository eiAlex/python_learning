
# Declarando e inicializando uma variável
f = 0 
print(f)

# declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variáveis de tipos diferentes
print("isto é uma string" + str(1))

# Variável Global X Variável local 
def algumafuncion():
    f = 100
    print(f)

algumafuncion()
print(f)