class Base():
    marca = ''
    modelo = ''
    ano = ''
    cor = ''
    def __init__(self,marca = None, modelo = None, ano = None, cor = None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

class Carro (Base):
    status_motor = False
    velocidade = 0
    def __init__(self, marca=None, modelo=None, ano=None, cor=None, status_motor = None, velocidade = None):
        self.status_motor = status_motor
        self.velocidade = velocidade
        super().__init__(marca, modelo, ano, cor)


    def ligar_motor(self):
        print("Motor ligado !")
        self.status_motor = True

    def desligar_motor(self):
        print("Motor desligado !")
        self.status_motor = False
    
    def status_motor_painel(self):
        print(f"Velocidade: "(self.velocidade))
        print(f"Status: "(self.status_motor))

    def acelerar(self):
        if self.status_motor != True:
            for vel in range(0,10):
                self.velocidade += 10
            print("Acelerando")
        else: 
            print("Carro Desligado")
carros = []
while True:
    print("1 - Para criar carro\n2 - Selecionar carro\n3 - Localização do carro")
    op = int(input("Opção: "))
    if op == 1:

        _marca = input("Informe a marca: ")
        _modelo = input("Informe a modelo: ")
        _ano = input("Informe a ano: ")
        _cor = input("Informe a cor: ")

        carro = Base(_marca, _modelo, _ano, _cor,)
        carros.append(carro)
    
    elif op == 2:
        
        op = int(input("Selecione o carro: "))
        carro_selecionado = carros[op-1]
        op_2 = int(input("1 - Ligar motor\n2 - Desligar motor\n3 - Acelerar\n4 - Painel\n5 - Editar carro"))
        
        if op == 1: 
            carro_selecionado.ligar_motor()
        
        elif op == 2 :
            carro_selecionado.desligar_motor()      
        
        elif op == 2:
            carro_selecionado.acelerar()       
        
        elif op == 3:
            carro_selecionado.status_motor_painel()
        
        elif op == 4:
            _marca = input("Informe a marca: ")
            _modelo = input("Informe a modelo: ")
            _ano = input("Informe a ano: ")
            _cor = input("Informe a cor: ")

            carro = Base(_marca, _modelo, _ano, _cor)
            carros.append(carro)
            print(carro)

    elif op == 3:
        carro_procurado = input("")