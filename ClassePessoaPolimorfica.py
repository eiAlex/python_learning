class Pessoa:
    def __init__ (self, nome ='', idade =0):
        self.nome = nome
        self.idade = idade

    def getIdade(self):
        return self.idade

    def getNome(self):
        return self.nome

   # def setIdade(self):
     #   self.idade = idade

class PessoaFisica(Pessoa):
    def __init__ (self, cpf, nome ='', idade =0):
        Pessoa.__init__ (self, nome, idade)
        self.cpf = cpf


class PessoaJuridica(Pessoa):
    def __init__ (self, cnpj='', nome='', idade =0):
        Pessoa.__init__ (self, nome, idade)
        self.cnpj = cnpj

a = Pessoa()
Pessoa.__init__(a, 'ÁLEX',22)

b = PessoaFisica ('122.333.332-1','aaa')

banco = PessoaJuridica('00.000.000/0001-11', nome='Banco do Brasil', idade=435)

print (a.nome)

print(b.cpf, )

print (banco.nome)
