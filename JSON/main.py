import http.client
import json

def api(url):
    http_request = http.client.HTTPSConnection('brasilapi.com.br')
    http_request.request("GET",url)
    response = http_request.getresponse()
    resposta_bytes = response.read()
    json_ = json.loads(resposta_bytes)
    return json_

def print_json(object):
    if type(object) is list:
        for json_ in object: 
            for key in json_.keys():
                print(f"{key} : {json_[key]}")

    elif type(object) is dict: 
        for key in object.keys():
            print(f"{key} : {object[key]}")


def menu():
    print("-------------------------------------")
    print("1 - Quero ver meu CEP\n2 - Quero descobrir um DDD\n3 - Quero consultar um CNPJ\n4 - Quero ver os feriados\n5 - Quero consultar codigo de um banco\n6 - Ver as taxas atualizadas\n7 - Pesquisar por cidade\n8 - Sair")
    print("-------------------------------------")
    
def espaco(nome):
    return str(nome).replace(' ', '%20')


while True: 
    
    menu()
    op = int(input("Informe oque deseja: "))

    if op == 1:
        cep = input("Qual é seu cep: ")
        json_cep = api(f"/api/cep/v1/{cep}")
        print_json(json_cep)
    
    if op == 2:
        ddd = input("Qual é seu ddd: ")
        json_ddd = api(f"/api/ddd/v1/{ddd}")
        print_json(json_ddd)
    
    if op == 3:
        cnpj = input("Qual é seu cnpj: ")
        json_cnpj = api(f"/api/cnpj/v1/{cnpj}")   
        print_json(json_cnpj)

    if op == 4: 
        ano = input("Qual o ano: ")
        json_ano = api(f"/api/feriado/v1/{ano}")   
        print_json(json_ano)

    if op == 5: 
        codigo = int(input("Qual código deseja consultar: "))
        json_codigo = api(f"/api/banks/v1/{codigo}")
        print_json(json_codigo)

    if op == 6: 
        json_taxa = api(f"/api/taxas/v1")
        print_json(json_taxa)

    if op == 7: 
        cidade = espaco(input("Diga o nome da cidade: "))
        json_cidade = api(f"/api/cptec/v1/cidade/{cidade}")
        print_json(json_cidade)


    if op == 8: 
        print("Muito obrigado por usar o programa!")
        break

