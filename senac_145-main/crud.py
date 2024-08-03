from classes import ONG,Projeto
from api_client import *


# def informacoes_projeto(_i):
#     nome = input('Informe o nome do projeto : ')
#     descricao = input('Descreva seu projeto')
#     responsavel = input('Quem é o responsavel do projeto: ')
#     status = input('Qual status do ptojeto: ')



def createOng(token):
    nome_ong = input("Nome da ong: ")
    ong = ONG(nome_ong)
    nome = input('Informe o nome do projeto : ')
    descricao = input('Descreva seu projeto')
    responsavel = input('Quem é o responsavel do projeto: ')
    status = input('Qual status do ptojeto: ')
    projeto = Projeto(nome ,descricao ,responsavel ,status)
    ong.adicionar_projeto(projeto)
    print(api_create(ong.to_json(),token))

def getOngs():  
    ongs=[]  
    ongs_json=api_read()
    for index, data in zip(range(len(ongs_json)),ongs_json):
        ong = ONG(nome=data['nome'],_id=data['_id'])
        print(f'{index} : Nome: {data['nome']}')
        for p in data['projetos']:
            projeto = Projeto(p['nome'],p['descricao'],
                              p['responsavel'],p['status'],p['_id'])
            ong.adicionar_projeto(projeto)
            print(f'  Projeto ----> {p['nome']}')
        ongs.append(ong)
        print('\n')
    return ongs