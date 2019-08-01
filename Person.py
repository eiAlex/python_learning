# -*- coding utf-8 -*- 

#python é uma linguagem orientada a objetos
# qause tudo em python é orientado a objettos com suas propiedades e métodos 
#uma clase é como um construtor de objetos, ou um moodelo para ciração deles 

#para criar um objeto do tipo class utilizamos a palavra class

#criado uma class com a propiedade x
class MyClass:
    x = 5

#chamda de uma classe

a = MyClass()
print(a.x)


# Todas as classes tem uma função chamada __init__(), que é executada quando a classe é chamada 



# podemos criar a classe  e a iniciarmos 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alex", 28)

print(p1.name, p1.age)

# nas classes podemetos ter tambem metodos 

class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def myfunctio(self):
        print("Hello " + self.name)


c1 = car("Ferrari", "Blue")
c1.myfunctio()