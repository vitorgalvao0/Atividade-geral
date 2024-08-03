import funcoes as f

catalogo = []

while True:
    
    print("----------Menu----------")
    print('''
1   - Criar ong
2   - Criar projeto
3   - Editar ong
4   - Sair
          
------------------------''')
    
    op = int(input("Informe uma opção: "))
    
    if op == 1:
        nome = input('Nome da Ong: ')
        tipo = input('Tipo de Ong: ')
        cnpj = input('CNPJ Ong: ')
        ong = f.create_ong(nome,tipo,cnpj)
        catalogo.append(ong)

    if op == 2:
        nome = input('Nome da descricao: ')
        descricao = input('Descricao: ')
        projeto = f.create_projeto(nome,descricao)    
        nome_ong = input('Nome da Ong: ')
        index = f.localiza_ong_index(nome_ong, catalogo)
        if index is None:
            print("Não existe")
            break
        catalogo[index]['projetos'].append(projeto)

    if op == 3:
        nome_atual = input("Nome da Ong:")
        nome_novo = input( " novo Nome da Ong:")
        ong_index = f.localiza_ong_index(nome_atual)
        f.edit_nome_ong(catalogo[ong_index],nome_novo)