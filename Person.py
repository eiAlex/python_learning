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
    
    def funcaoPrint(self):
        print("Helllo ", self.name, self.age)

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

# Herança com python 

# A herança nos permite definir uma classe que herda todos métodos e propiedades de uma classe vindos de outra classe.

# Temos a classe pai que está sendo herdada de, também chamada de classe base.
# temos a classe filha que recebe todos os atributos oriundos da classe pai derivada.

# No paython qualquer classe pode ser uma classe pai, a sintaxe é a mesma para crialção de qulquer uma classse

# classe filha de pessoa 

class Student(Person):
    pass # use a palavra pass para utiliza

# Utilizamos os atributos de pessoa

s = Student("Aline",28)
print(s.name, s.age)

# utilizando método de função derivada 
s.funcaoPrint()


# inicando com com o __init()__

# A função __imiti()__ é chamada automaticamente quando toda vez que é criada por um obejeto 
# caso quando ela é passada como na classe filha ela sobreescrever o init da função pai

class student2(Person):
    def __init__ ( self, fname, fage, year): # qaundo se adiciona o init desta forma a classe não erdará de seu pai 
        # para manter a erança utilize um inite para classe pai 
        Person.__init__(self, fname, fage)
        self.graduationYaer = year


#z = Student("Mike", 21, 2019)

#z.funcaoPrint()

#