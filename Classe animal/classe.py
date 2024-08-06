class Animal:
    nome = ''
    coracao = ''
    def __init__(self, nome, coracao):
        self.nome = nome
        self.coracao = coracao

class Humano(Animal):
    nome = ''
    coracao = ''
    cor = '' 
    sexo = '' 
    idade = ''
    peso = ''
    salario = '' 
    cpf = ''

    def __init__(self, nome, coracao, cor, sexo, idade, peso, salario, cpf):
        super().__init__(nome, coracao)
        self.cor = cor
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
        self.salario = salario
        self.cpf = cpf

    def falar(self):
        print("Bla...Bla...Bla..Bla")

    def pensar(self):
        print("hmmm.....hmm......hmmm........ ")

class Cachorro(Animal):
    nome = ''
    coracao = ''
    cor = ''
    peso = ''
    sexo = ''
    idade = ''
    tamanho = '' 
    raca = ''
    
    def __init__(self, nome, coracao, cor, peso, sexo, idade, tamanho, raca):
        super().__init__(nome, coracao)
        self.cor = cor
        self.peso = peso
        self.sexo = sexo
        self.idade = idade
        self.tamanho = tamanho
        self.raca = raca

    def latir(self):
        print('Aow-Aow')

    def correr(self):
        print("PEGA-PEGA-PEGA...")

    def sentar(self):
        print("Sentado!")
