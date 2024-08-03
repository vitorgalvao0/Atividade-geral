''''banco_ong_tabela_doacao = [
                        ['nome','vitor','pedro'],
                        ['valor','1000','20000'],
                        ['cpf','0694456147','08325614649'],
                        ['email','vitor@gmail.com','pedro@gmail.com'],
                        ['telefone','67992295586','6799862251']
]
linha = ' '
linha2 = ' '
linha3 = ' '''
#FEITO  POR MIM
'''for i in range(0,len(banco_ong_tabela_doacao)):
    linha += banco_ong_tabela_doacao[i][0]+' '
print(linha,'\n')
for i in range(0,len(banco_ong_tabela_doacao)):
   linha2 += banco_ong_tabela_doacao[i][1]+' '
print(linha2,'\n')
for i in range(0,len(banco_ong_tabela_doacao)):
    linha3 += banco_ong_tabela_doacao[i][2]+' '
print(linha3,'\n')'''
#CORREÇÃO DO PROFESSOR
'''for l in range(0,len(banco_ong_tabela_doacao[0])):
    linha = ' '
    for i in range(0,len(banco_ong_tabela_doacao)):
        linha = linha + str(banco_ong_tabela_doacao[i][l])+' '
    print(linha)'''

banco_ong_tabela_vertical =  [
                        ['nome','vitor','pedro'],
                        ['valor','1000','20000'],
                        ['cpf','0694456147','08325614649'],
                        ['email','vitor@gmail.com','pedro@gmail.com'],
                        ['telefone','67992295586','6799862251']
]
for l in range(0,len(banco_ong_tabela_vertical[0])):
    linha = ''
    for i in range(0,len(banco_ong_tabela_vertical)):
        print(banco_ong_tabela_vertical[i][l])
    
   