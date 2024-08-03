class Animal:
    nome = str
    coracao = bool
    def __init__(self, nome, coracao):
        self.nome = nome
        self.coracao = coracao

class Humano(Animal):
    nome = str
    coracao = str
    cor = str 
    sexo = str 
    idade = int
    peso = int
    salario = int 
    cpf = int

    def __init__(self, nome, coracao, cor, sexo, idade, peso, salario, cpf):
        super().__init__(nome, coracao)
        self.cor = cor
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
        self.salario = salario
        self.cpf = cpf

class Cachorro(Animal):
    nome = str
    coracao = str
    cor = str
    peso = int
    sexo = str
    idade = int
    tamanho = int 
    raca = str
    
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
