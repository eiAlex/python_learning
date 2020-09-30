arr = [2,3,4,3,2,1] 



def validar():
    aux = 0
    for i in arr:
        if i == 3:
            aux += 1
    return aux

print(validar())    

