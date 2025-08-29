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


def cadastrar():
    nome_doce = input("Digite o nome do produto que será cadastrado: ").strip()

    if not nome_doce.isalpha():
        print(f"O nome '{nome_doce}' é inválido. Digite um nome com letras apenas!")
        return

    try:
        preco_doce = float(input("Digite o preço do doce: "))
    except ValueError:
        print("Preço inválido! Digite apenas números")
        return

    doces.append(nome_doce)
    preco.append(preco_doce)
    print("Produto cadastrado com sucesso!")



def listar():
    for i, doces in enumerate(doces):
        print(f"{i + 1} {doces} Preço: {preco[i]}")


def atualizar():
    print("Essa é sua lista: ")
    for i in range(len(doces)):
        print(i + 1, doces[i])
    id_item = int(input("Digite o item que você deseja atualuizar: ")) - 1
    doces[id_item] = input("Qual doce você deseja colocar no lugar do anterior: ")
    preco[id_item]= float(input("Digite o preço do novo doce: "))

    



def vendas():
    i = int(input("Digite a posição do doce que você deseja: "))
    print(f"O doce vendido foi {doces[i]}")
    data_doce = input("Digite  quando a venda foi realizada: ")
    data.append(data_doce)
    volume_doce = int(input(f"Digite quantos {doces[i]} foram vendidos: "))
    volume.append(volume_doce)
    print(f"O valor recebido foi {preco[i] * volume_doce}")


def deletar_produto():
    #for i in range(len(doces)):
    item = int(input("Digite o doce que você deseja apagar: "))
    '''ValueError:
            print("Digite um número da lista de doces")'''
    doces[item] = "none"
    preco[item] = "none"
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
            cadastrar()
        case 2:
            listar()
        case 3:
            atualizar()
        case 4:
            vendas()
        case 5:
            deletar_produto()
        case 6:
            sair()
        case _:
            print("Digite uma das opções abaixo")


main()

if __name__ == "__main__":
    while True:
        main()
