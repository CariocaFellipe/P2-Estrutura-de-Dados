from animal import Animal
from pessoa import Pessoa

animais_cadastrados = []
pessoas_cadastradas = []


def cadastrar_animal():
    tipo = input("Digite o tipo do animal: ")
    idade = input("Digite a idade do animal: ")
    cor = input("Digite a cor do animal: ")
    porte = input("Digite o Porte do Animal: ")

    animal = Animal(tipo, idade, cor, porte)
    animais_cadastrados.append(animal)

    print("Animal cadastrado com sucesso!")


def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    contato = input("Digite o contato da pessoa: ")
    especie = input("Digite a espécie de interesse da pessoa: ")
    idade = input("Digite a idade de interesse da pessoa: ")
    cor = input("Digite a cor de interesse da pessoa: ")
    porte_animal = input("Digite o Porte interessado: ")

    pessoa = Pessoa(nome, contato, especie, idade, cor, porte)
    pessoas_cadastradas.append(pessoa)

    animais_compativeis = buscar_animais_compativeis(pessoa)

    if animais_compativeis:
        print(f"Animais disponíveis que podem ser do interesse de {pessoa.nome}:")
        for animal in animais_compativeis:
            animal.exibir_detalhes()
    else:
        print(f"Nenhum animal disponível corresponde aos interesses de {pessoa.nome}.")


def buscar_animais_compativeis(pessoa):
    animais_compativeis = []
    for animal in animais_cadastrados:
        if pessoa.verificar_compatibilidade(animal):
            animais_compativeis.append(animal)
    return animais_compativeis


def menu():
    while True:
        print("1 - Cadastrar animal")
        print("2 - Cadastrar pessoa")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_animal()
        elif opcao == "2":
            cadastrar_pessoa()
        elif opcao == "3":
            print("Finalizando")
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    menu()
