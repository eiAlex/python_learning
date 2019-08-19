#Para percorrer sequencias previamente conhecidads se utiliza o for 

palavra = "Python"

for letras in palavra:
    print(letras)

#laços para percorrer uma lista 
cestaDeFrutas = ["Laranja", "Banana", "Uva"]

for frutas in cestaDeFrutas:
    print(frutas)

#laços com numeração de indeses
for index, letras in enumerate(palavra):
    print(index,letras)

#laços com numeração de indeses (sem index)
for  letras in enumerate(palavra):
    print(letras)

#laços de repetição com tamanho prefixado 
for x in range(5):
    print(x)

#laço simples com whihe
cont = 0 
while cont <= 5:
    print(cont)
    cont +=1
