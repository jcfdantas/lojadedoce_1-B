doces = []
preco = []
data = []
volume = []
preco_doce = ("")
nome_doce = ("")
estoque = []


def menu():
    print("      Armázem Loja de Doce      ")
    print("1) Cadastrar produto")
    print("2) Listar produtos cadastrados")
    print("3) Atualizar lista de produtos")
    print("4) Registrar vendas")
    print("5) Deletar produto")
    print("6) Sair")
    '''cadastrar, listar, alterar e deletar'''


def cadastrar(doces, preco, preco_doce, nome_doce):
    nome_doce = input("Digite o produto que será cadastarado: ")
    if nome_doce.isnumeric():
        print(f"O {nome_doce} é inválido, dígite um nome somente com letras!")
    doces.append(nome_doce)
    preco_doce = float(input("Digite o preço do doce: "))
    preco.append(preco_doce)


def listar(doces, preco):
    for i in range(len(doces)):
        print(doces[i], f"Preço: {preco[i]}")


def atualizar(doces, preco):
    print("Essa é sua lista: ")
    for i in range(len(doces)):
        print(doces[i])
    item = int(input("Digite o item que você deseja atualuizar: "))


def vendas(data, volume, preco):
    i = int(input("Digite a posição do doce que você deseja"))
    print(f"O doce vendido foi {doces[i]}")
    data_doce = input("Digite  quando a venda foi realizada: ")
    data.append(data_doce)
    volume_doce = int(input(f"Digite quantos {doces[i]} foram vendidos: "))
    volume.append(volume_doce)
    print(f"O valor recebido foi {preco[i] * volume_doce}")


def deletar_produto(doces):
    try:
        for i in range(len(doces)):
            i = int(input("Digite o doce que você deseja apagar: "))
            return i
    except ValueError:
        print("Digite um número da lista de doces")
    doces[i] = ["none"]
    for linha in doces:
        print(linha)


def sair():
    return False


def main():
    print("Loja de doce")
    menu()
    op = int(input("Digite a opção: "))
    match(op):
        case 1:
            cadastrar(doces, preco, preco_doce, nome_doce)
        case 2:
            listar(doces, preco)
        case 3:
            atualizar(doces, preco)
        case 4:
            vendas(data, volume, preco)
        case 5:
            deletar_produto(doces)
        case 6:
            sair()
        case _:
            print("Digite uma das opções abaixo")


main()

if __name__ == "__main__":
    while True:
        main()
