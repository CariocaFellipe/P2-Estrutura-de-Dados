from animal import Animal
from pessoa import Pessoa

animais_cadastrados = []
pessoas_cadastradas = []


def cadastrar_animal():
    tipo = input("Digite o tipo do animal: ")
    idade = input("Digite a idade do animal: ")
    cor = input("Digite a cor do animal: ")
    porte = input("Digite o Porte do Animal")

    animal = Animal(tipo, idade, cor)
    animais_cadastrados.append(animal)

    print("Animal cadastrado com sucesso!\n")


def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    contato = input("Digite o contato da pessoa: ")
    especie_interesse = input("Digite a espécie de interesse da pessoa: ")
    idade_interesse = input("Digite a idade de interesse da pessoa: ")
    cor_interesse = input("Digite a cor de interesse da pessoa: ")

    pessoa = Pessoa(nome, contato, especie_interesse, idade_interesse, cor_interesse)
    pessoas_cadastradas.append(pessoa)

    animais_compativeis = buscar_animais_compativeis(pessoa)

    if animais_compativeis:
        print(f"\nAnimais disponíveis que podem ser do interesse de {pessoa.nome}:")
        for animal in animais_compativeis:
            animal.exibir_detalhes()
    else:
        print(f"\nNenhum animal disponível corresponde aos interesses de {pessoa.nome}.\n")


def buscar_animais_compativeis(pessoa):
    animais_compativeis = []
    for animal in animais_cadastrados:
        if pessoa.verificar_compatibilidade(animal):
            animais_compativeis.append(animal)
    return animais_compativeis


def menu():
    while True:
        print("1 - Cadastrar animal")
        print("2 - Cadastrar pessoa interessada em adoção")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_animal()
        elif opcao == "2":
            cadastrar_pessoa()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!\n")


if __name__ == '__main__':
    menu()
