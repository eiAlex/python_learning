import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="minhasenhasegura"
)   
#mostra a conexão com banco
print(mydb) 
