from classe import *
from views import *



dados_humano = []
dados_cao = []



def criar_cao():
    nome = input("Diga o nome do seu cao: ")
    coracao = input("Seu cachorro tem coracao: ")
    cor = input("Qual a cor do seu cao: ")
    peso = float(input("Digite o peso do seu cao: "))
    sexo =  input("Qual o sexo do seu cao: ")
    idade = input("Quantos anos seu cao tem: ")
    tamanho = int(input("Qual o tamanho do seu cao: "))
    raca = input("Qual a raca do seu cao: ")
    cao = Cachorro(nome,coracao,cor,peso,sexo,idade,tamanho,raca)
    dados_cao.append(cao)
    return cao


def criar_humano():
    nome = input("Qual o nome da pessoa: ")
    coracao = input("Essa pessoa tem coracao: ")
    cor = input("Qual a cor dessa pessoa : ")
    sexo =  input("Qual o sexo da pessoa: ")
    idade = input("Qual a idade da pessoa: ")
    peso = float(input("Qual o peso dessa pessoa: "))
    salario = int(input("Qual o salario dessa pessoa: "))
    cpf = int(input("Qual o CPF dessa pessoa: "))
    pessoa = Humano( nome, coracao, cor, sexo,idade, peso, salario, cpf)
    dados_humano.append(pessoa)
    return pessoa

def info_humano(pessoa):
    print(dados_humano[pessoa].nome)
    print(dados_humano[pessoa].coracao)
    print(dados_humano[pessoa].cor)
    print(dados_humano[pessoa].sexo)
    print(dados_humano[pessoa].idade)
    print(dados_humano[pessoa].peso)
    print(dados_humano[pessoa].salario)
    print(dados_humano[pessoa].cpf)

def info_cao(cao):
    print(dados_cao[cao].nome)
    print(dados_cao[cao].coracao)
    print(dados_cao[cao].cor)
    print(dados_cao[cao].peso)
    print(dados_cao[cao].sexo)
    print(dados_cao[cao].idade)
    print(dados_cao[cao].tamanho)
    print(dados_cao[cao].raca)

while True:
    separar()
    menu_principal()
    separar()
   
    op = int(input("Qual a funcao desejada: "))

    if 1 == op:
        criar_humano()

    elif op == 2: 
        p = int(input("Insira o numero [0] para acessar as info: "))
        info_humano(p)

    elif op == 3:
        criar_cao()

    elif op == 4:
        p = int(input("Insira o numero [0] para acessar as info: ")) 
        info_cao(p) 
        
        separar()
        
        op = input("Qual acao deseja que o cao realize: ")

        if op == 1:
            pass

    elif op == 5:
        break

