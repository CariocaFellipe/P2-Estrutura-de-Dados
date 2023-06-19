from animal import Animal
from pessoa import Pessoa

animais_cadastrados = []
pessoas_cadastradas = []


def cadastrar_animal():
    tipo = input("Digite o tipo do animal: ").upper()
    nome = input("Digite o nome do animal: ").upper()
    idade = input("Digite a idade do animal: ").upper()
    cor = input("Digite a cor do animal: ").upper()
    porte = input("Digite o Porte do Animal: ").upper()

    animal = Animal(tipo, nome, idade, cor, porte)
    animais_cadastrados.append(animal)

    print("Animal cadastrado com sucesso!")


def cadastrar_pessoa():
    nome = input("Digite seu nome: ").upper()
    contato = input("Digite o seu numero ").upper()
    especie = input("Digite a espécie do seu interesse ").upper()
    idade = input("Digite a idade do animal de seu interesse ").upper()
    cor = input("Digite a cor do animal de seu interesse  ").upper()
    porte = input("Digite o Porte de seu interesse: ").upper()

    pessoa = Pessoa(nome, contato, especie, idade, cor, porte)
    pessoas_cadastradas.append(pessoa)

    animais_compativeis = buscar_animais(pessoa)

    if animais_compativeis:
        print(f"Animais que são do gosto de {pessoa.nome}:")
        for animal in animais_compativeis:
            animal.exibir_detalhes()
    else:
        print(f"Nenhum animal ao gosto de {pessoa.nome} encontrado.")


def buscar_animais(pessoa):
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
