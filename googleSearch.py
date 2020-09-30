#pip install google

from googlesearch import  search


query = "harry poter" # texto para a busca

''' 
tld = se refere ao dominio autoritativos Ex: .com, .br .in .co.in
lang= liguagem de preferência
num = numero de resultados esperados
start = numero especifico de starts que devera começar
stop = com quantos resultados vc gosaria de para
pause = é um sleep de 2 segundo para não ter o http request bloqueado pela google, isto acontece via IP

'''

for i in search(query, tld="com", num=10, stop= 10, pause=2):
    print(i)
