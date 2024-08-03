
# nome = "banco_01.txt"
# valor_cripto = 1
# discritor = open(nome,"a")
# frase = input("Digite: ")
# new_frase = ''
# for letra in frase:
#     new_frase += chr((ord(letra)+valor_cripto)%127)
# discritor.write(new_frase)

# nome = "banco_01.txt"
# discritor = open(nome,"r")
# new_frase = ''
# valor_cripto = 1
# for letra in discritor.read():
#     new_frase += chr((ord(letra)-valor_cripto)%127)
# print(new_frase + chr(32))

# valor_cripto = 1450
# digitado = input("valor:")
# print(f"Valor deslocamento: {valor_cripto}")
# print(f"Tabela:{ord(digitado)}")
# print(f"Soma(deslocamento + tabela){valor_cripto + ord(digitado)}")
# print(f"Valor utilizado{(valor_cripto + ord(digitado))%128}")

# for salto in range(0,127):
#     new_frase = ''
#     discrito = open('banco_01.txt','r')
#     for l in discrito.read():
#         if ord(l) + salto > 127:
#             new_frase += chr((ord(l) - salto ) %127 )
#         else:
#             new_frase += chr((ord(l) - salto ))
#     print(f'tentativa[{salto}] : {new_frase}')
#     save = open('resultados_conferencia', 'a')
#     save.write(new_frase)
#     save.close()
#     discrito.close()
