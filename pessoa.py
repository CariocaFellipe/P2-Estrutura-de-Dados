class Pessoa:
    def __init__(self, nome, contato, especie, idade, cor):
        self.nome = nome
        self.contato = contato
        self.especie = especie
        self.idade = idade
        self.cor = cor

    def verificar_compatibilidade(self, animal):
        return (
            animal.tipo == self.especie
            and animal.idade == self.idade
            and animal.cor == self.cor
        )
