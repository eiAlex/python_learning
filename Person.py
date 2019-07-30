# -*- coding utf-8 -*- 


# Todas as classes tem uma função chamada __init__(), que é executada quando a classe é chamada 

# podemos criar a classe  e a iniciarmos 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alex", 28)

print(p1.name, p1.age)