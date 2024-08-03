lampadas = [] 
sair = True
while sair:
    opcao = input('''Adicionar lampada - adicionar\nListar lampadas - listar\nSair do programa - sair\nRemover lampada - remover\n''')
    if opcao == "sair":
        sair = False
    if opcao == "adicionar":
        sub_opcao = input("on ou off\n")
        if sub_opcao == "on":
            lampadas.append(True)
        elif sub_opcao == "off":
            lampadas.append(False)
        else:
            print("opcao invalida")
    if opcao == "remover":
        lampadas.pop()
    if opcao == "listar":
        for lampada in lampadas:
            print("lampada", lampada)