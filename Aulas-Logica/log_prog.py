# a = 12 + 12 + 12 + 12
# print(a)
# b = 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23
# print(b)
# c =  10 - 5
# print(c)
# d = 175 - 150
# print(d)
# e = 8 + 8
# print(e)

# a = 0
# for x in range(0,4):
    # a = a + 12
# print(a)
# 
# a = 0
# count = 0
# while count < 4:
    # count += 1
    # a = a + 12
# print(a)
# 
# a = 10 
# b = 2
# cont = 0
# while (a-b)>=0:
    # a=a - b
    # cont = cont + 1
# print(f"Divisão: {cont})
# print(f"Resto: {a})


# a = 29
# b = 5
# c = "/"

# if c == "/":
    # cont = 0
    # while (a-b)>=0:
        # a = a - b
        # cont = cont + 1
    # print(f"Divisão: {cont}")
    # print(f"Resto: {a}")

# if c == "+":
    # soma = a + b
    # print(soma)

# if c == "-":
    # diferenca = a - b
    # print(diferenca)

# if c == "*":
#     # cont = 0 
    # produto = 0
    # while cont < b:
        # cont += 1
        # produto = produto + a
    # print(f"Produto: {produto}")

# sensor = 100 # menor ou igual a 500 acesa, maior que 500 apagado
# luz = True 

# if sensor > 500:
    # luz = False 
    # print('Apagado')

# if sensor <= 500:
    # luz = True
    # print('Acesa')

sensor_umidade = 1024 #maximo 1024
                     # 0 = 100%(umido)
                     # 1024 = 0%(seco)

if sensor_umidade >= 0 and sensor_umidade < 341:
    print('Humido')
elif sensor_umidade >= 341 and sensor_umidade <= 682:
    print('Semi-seco')
if sensor_umidade > 682 and sensor_umidade <= 1024:
    print('Seco')