import http.client
import json

class Projeto:
    _id = ' '
    nome = ''
    descricao = ''
    responsavel = ''
    status = '' 

    def __init__(self,  nome = None,descricao = None, responsavel = None, status = None, _id = None):
        self._id = _id
        self.nome = nome
        self.descricao = descricao
        self.responsavel = responsavel 
        self.status = status

    def atualiza_status(self,novo_status = None):
        self.status = novo_status

    def mostrar_informacao(self):
        print(f"Nome: {self.nome}{chr(32)}Descricao: {self.descricao}{chr(32)}Responsavel: {self.responsavel}{chr(32)}Status: {self.status}{chr(32)}")

    def to_json(self):
        json_ = {}
        json_['nome'] = self.nome
        json_['descricao'] = self.descricao
        json_['responsavel'] = self.responsavel
        json_['status'] = self.status 
        return json_




class Ong:
    _id = ' ' 
    nome = ''
    projetos = []

    def __init__(self,nome = None, _id = None):
        self.nome = nome 
        self._id = _id

    def listar_projetos(self):
        for projeto in self.projetos:
            print(projeto.nome)

    def adicionar_projeto(self,projeto):
        self.projetos.append(projeto)

    def buscar_projeto(self,nome):
        for projeto in self.projetos:
            if projeto.nome == nome: 
                return projeto
        return None

    def to_json(self):
        json_ = {}
        json_['nome'] = self.nome
        json_['projetos'] = []
        for projeto in self.projetos:
            p = projeto.to_json()
            json_['projetos'].append(p)
        return json_ 

class GerenciadorDeONG():
    _id = ' '
    ongs = []
    

    def __init__(self):
        pass
        # json_ongs = self.api_get("/ongs")
        # for ongs in json_ongs: 
        #     ong = Ong(ongs['nome'])
        #     print(f"\n---> Nome Ong: {ongs['nome']}\n")
        #     for projeto in ongs['projetos']:
        #         print(f" >>> Projeto: {projeto['nome']}")
        #         print(f"  -+ Descricao do projeto: {projeto['descricao']}")
        #         print(f"  -+ Responsavel pelo projeto : {projeto['responsavel']}")
        #         print(f"  -+ Status do projeto: {projeto['status']}\n")                
        #         projeto = Projeto(projeto['nome'], projeto['descricao'], projeto['responsavel'], projeto['status'])
        #         ong.adicionar_projeto(projeto)
        #     self.adicionar_ong(ongs)

    def adicionar_ong(self,ong):
        self.ongs.append(ong) 


    def api_get(self):
        http_request = http.client.HTTPSConnection('api.viana.dev')
        headers = {'Content-type':'application/json'}
        http_request.request("GET", '/ongs', headers = headers)
        response = http_request.getresponse()
        resposta_bytes = response.read()
        json_ = json.loads(resposta_bytes)
        return json_
    
    def api_create(self, ong_json):
        http_request = http.client.HTTPSConnection('api.viana.dev')
        headers = {'Content-type':'application/json'}
        http_request.request("POST", '/ongs', body = ong_json, headers = headers)
        response = http_request.getresponse()
        resposta_bytes = response.read()
        json_ = json.loads(resposta_bytes)
        return json_  



gerenciador = GerenciadorDeONG()
ong = Ong("VitorGalvao")
projeto = Projeto("S.o.S Natureza", "Ajude a proteger o meio ambiente", "Vitor", "Finalizado")
ong.adicionar_projeto(projeto)
projeto = Projeto("Sangue amigo", "Doe sangue", "Vitor", "Em andamento")
ong.adicionar_projeto(projeto)
json_ = json.dumps(ong.to_json())
# print(json_)
print(gerenciador.api_create(json_))







# print()


# print('''1 - Criar ong
# 2 - Adicionar projetos
# 3 - Lista projeto
# 4 - Buscar projetos
# 5 - Sair''')

# while True:
#     op = int(input("Insira opção: "))
    
#     if op == 1:
#         nome_ong = input("Informe o nome da ong: ")
#         ongs = gerenciador.ongs(nome_ong)
#         print(f"Ong {nome_ong} criada com sucesso!!")

    # elif op == 2: 
    #     nome_projeto = input("Nome do projeto: ")
    #     descricao = input("Descricao do projeto: ")
    #     responsavel = input("Responsavel do projeto: ")
    #     status = input("Status do projeto: ")
    #     projeto = Projeto(nome_projeto,descricao,responsavel,status)
    #     ongs.adicionar_projeto(projeto)
    #     print(f"Projeto {nome_projeto} criado com sucesso!!")
    
    # elif op == 3: 
    #     ongs.listar_projetos()

    # elif op == 4: 
    #     nome = input("Nome do projeto: ")
    #     projeto_valido = ongs.buscar_projeto(nome)
    #     if projeto_valido != None:
    #         print(f"Projeto: {projeto_valido.nome}")
    #         print(f"Status: {projeto_valido.status}")
    #         print(f"Informações sobre: {projeto_valido.mostrar_informacoes()}")

    # elif op == 5:
    #     break