import pandas as pd
alphabet = "abcdefg"
data = alphabet.split() #split string into a list

for temp in data:
    print (temp)

print(len(alphabet))
thisdict = {}
for letra in range(len(alphabet)):
    print(alphabet[letra])
    
    thisdict[letra] = alphabet[letra]

print(thisdict)