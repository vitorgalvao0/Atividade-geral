class Banco():
    pe = ''
    assento = ''
    pe_com_rodas = False
    def __init__(self, pe = None, assento = None):
        self.pe = pe 
        self.assento = assento

    def giratoria(self):
        self.pe_com_rodas = True

class Cadeira(Banco):
    encosto = ''
    def __init__(self, pe, encosto, assento):
        self.encosto = encosto
        super().__init__(pe,assento)

banco = Banco('fofo','rodas')
banco_2 = Banco('duro','sem rodas')

print(banco.assento)
print(banco_2.assento)

cadeira = Cadeira()
print(cadeira.pe)