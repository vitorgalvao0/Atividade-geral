
print("\n____________________________________________________________________________\n")
vagas = [
        [ 'VAGAS  ' , "VAGA 1" , "VAGA 2" , "VAGA 3" , "VAGA 4" , "VAGA 5"],
        [ 'SETOR 1' , "X     " , 'X     ' , "X     " , 'X     ' , "X     "],
        [ 'SETOR 2' , 'X     ' , 'X     ' , 'X     ' , 'X     ' , 'X     '],
        [ 'SETOR 3' , "X     " , "X     " , "X     " , "X     " , 'X     '],
        [ 'SETOR 4' , 'X     ' , 'X     ' , 'X     ' , 'X     ' , 'X     '],
        [ 'SETOR 5' , 'X     ' , 'X     ' , 'X     ' , 'X     ' , 'X     ']

]
print("\n____________________________________________________________________________\n")


def imprimi_vagas():
    for l in range(0,len(vagas[0])):
        linha = " "
        for i in range(0,len(vagas)):
            linha = linha + str(vagas[i][l])+ ' '
        print(linha)
def menu():
    print('''1 - Estacionar
2 - Retirar
3 - Sair
4 - Excluir setor
5 - Adicionar setor''')
while True:
    imprimi_vagas()
    menu()
    op = input(" selecione uma opcao: ")
    if op == '1':
        setor = int(input('Informe o setor: '))
        vaga = int(input('Informe a vaga: '))
        if vagas[setor][vaga] == 'X':
            print('Vaga ocupada!')
        else:
            vagas[setor][vaga] == 'vazio '
            vagas[setor][vaga] = 'X     '
        print('Estacionado!')
    if op == '2':
        setor = int(input('Informe o setor da retirada: '))
        vaga = int(input('Informa a vaga de retirada: '))
        if vagas[setor][vaga] == 'vazio':
            print('Esta vaga esta vazia')
        else:
            vagas[setor][vaga] == ' X '
            vagas[setor][vaga] = ' vazio '
        print('Vaga desocupada!')
    if op == '3':
        print('Sistema finalizado!')
        break
    if op == '4':
        setor = int(input('Qual setor deseja desocupar: '))
        vaga = int(input('Qual vaga deseja desocupar:'))
        for l in range(vaga,len(vagas[0])):
            linha = " "
            for i in range(setor,len(vagas)):
                linha = linha + str(vagas[i][l])+ ' '
                vagas[setor][vaga] = 'O'
    if op == '5':
        pass