def create_ong(nome,tipo,cnjp,projeto):
    ong = { 
        'nome': nome, 
        'tipo': tipo, 
        'CNPJ': cnjp, 
        'projeto': []
    }
    return ong

def create_projeto(nome, descricao):
    projeto = {
    'nome': nome, 
    'descricao': descricao
    }
    return projeto

def localiza_ong_index(nome,catalago):
    for index in range(0, len(catalago)):
        if catalago[index]['nome']==nome:
            return index
    return None

def edit_nome_ong(ong,nome):
    ong['nome']=nome
   
