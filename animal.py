class Animal:
    def __init__(self, tipo, idade, cor, porte):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte

    def exibir_detalhes(self):
        print(f"Tipo: {self.tipo}")
        print(f"Idade: {self.idade}")
        print(f"Cor: {self.cor}")
        print(f"Porte: {self.porte}")
        print()
