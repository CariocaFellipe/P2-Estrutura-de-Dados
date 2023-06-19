class Pessoa:
    def __init__(self, nome, contato, especie_interesse, idade_interesse, cor_interesse):
        self.nome = nome
        self.contato = contato
        self.especie_interesse = especie_interesse
        self.idade_interesse = idade_interesse
        self.cor_interesse = cor_interesse

    def verificar_compatibilidade(self, animal):
        return (
            animal.tipo == self.especie_interesse
            and animal.idade == self.idade_interesse
            and animal.cor == self.cor_interesse
        )
