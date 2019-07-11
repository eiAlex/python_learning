
n = int ( input ("Escreva o número para o fatorial:") )

def fat(n):
    if n <= 1:
         return 1 
    return fat( n - 1 ) * n

print("O fatorial é : ", fat(n) ) 