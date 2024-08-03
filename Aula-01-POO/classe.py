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