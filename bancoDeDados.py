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

#Cria DB se ele existe 
testeCursor.execute("CREATE DATABASE IF NOT EXISTS DBTESTE;")

#Cria a tabela 
testeCursor.execute("CREATE TABLE IF NOT EXISTS DBTESTE.VENDEDORES (ID INT AUTO_INCREMENT PRIMARY KEY, NOME VARCHAR (255), ENDERECO VARCHAR(255))")

#Vmostra a tabela 
testeCursor.execute("SHOW TABLES FROM DBTESTE")

for tabelas in testeCursor:
  print(tabelas)

#Inserção de dados no curso é passda por parametros

sql = "INSERT INTO DBTESTE.VENDEDORES (NOME,ENDERECO) VALUES (%s, %s)"
val = ("John" , "Higway 2100")

testeCursor.execute(sql,val)

#COMMITE DA TRANSAÇÃO 
mydb.commit() 

#printe de contagem de linhas
print("Contagem de linhas", testeCursor.rowcount)

#inserção de varias linhas 
val = [
  ("John" , "Higway 2100"),
  ("Dereck" , "level center 13"),
  ("Marie" , "lives town 12"),
  ("John" , "Higway 2100"),
  ("John" , "Higway 2100"),
  ("John" , "Higway 2100"),
  ("John" , "Higway 2100"),
  ("John" , "Higway 2100"),
  ("John" , "Higway 2100")
]

#para mais linhas execute many 
testeCursor.executemany(sql,val) # para
mydb.commit()

#printe de contagem de linhas inteiradas
print("Contagem de linhas", testeCursor.rowcount)

mydb.close()