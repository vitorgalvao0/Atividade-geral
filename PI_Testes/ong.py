doacao_valor = []
doacao_nome = []

def informacoes_doacao(valor):
    sub_opcao = int(input('Doacao anonima\n1 - para sim\n2 - para nao: '))
    if sub_opcao == 1:
        print('A doacao sera anonima, obrigado. ')
        doacao_nome.append("Anonima")
    else:
        nome = input('Digite seu nome: ')
        cpf = input('Informe seu CPF: ')
        email = input('Informe um email: ')
    doacao_valor.append(valor)
    print(f'Valor doado foi de {valor}')

opcao = 7 
while opcao != 6:
    total = 0
    for i in range(0,len(doacao_valor)):
         print(f'Nome: {doacao_nome[i]}')
         total = total + doacao_valor[i]
    print(f'Total doado{total}')
    opcao = int(input('''Opcao menu\n[1] - R$50,00\n[2] - R$100,00\n[3] - R$200,00
[4] - R$300,00\n[5] - Outros valores\n[6] - Sair\nDigite a sua opcao:'''))
    if opcao == 1:
        informacoes_doacao(50)
    if opcao == 2:
        informacoes_doacao(100)
    if opcao == 3:
        informacoes_doacao(200)
    if opcao == 4:
        informacoes_doacao(300)
    if opcao == 5:
        pass
    else:
        print('Opcao invalida, digite novamente:')

        




