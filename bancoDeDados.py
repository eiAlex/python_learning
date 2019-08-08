import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="minhasenhasegura",
  database="information_schema",
  buffered= True # Importante definir o buffer como verdadeiro para segurar a conexão 
)   
#mostra a conexão com banco
print(mydb) 

#passar utilizando cursor
testeCursor = mydb.cursor()

testeCursor.execute("CREATE DATABASE DB_TESTE;")
testeCursor.execute("DROP DATABASE DB_TESTE;")

print(testeCursor)

testeCursor.execute("SHOW DATABASES")

for x in testeCursor:
  print(x)


testeCursor.execute("SELECT * FROM CHARACTER_SETS LIMIT 5")
#for x in testeCursor:
  #print(x)

#print(testeCursor._rows)


#retorna as colunas do codigp
testeCursor.execute("SELECT * FROM CHARACTER_SETS LIMIT 5")
#retorna as turplas
dataBase = testeCursor.fetchall()
#print(dataBase)
print("------------------------------------------------")
#percorre a tabela e imprime 

print(testeCursor.column_names)
for table in dataBase:
  print(table)
 