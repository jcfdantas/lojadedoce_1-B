doces = []
preco = []
volume = []
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
    for i in range(len(doces)):
        print(f'{i + 1}) {doces[i]} - Preço: R${preco[i]:.2f}')


def atualizar():
    print("Essa é sua lista: ")
    listar()
    desejo = input('O que você deseja alterar([n]ome ou [p]reço)? ').lower()
    if desejo in ('n', 'p'):
        try:
            id_item = int(input("Digite o código do item que você deseja atualizar: ")) - 1
            if id_item < 0 or id_item >= len(doces):
                print('Por favor, digite um código de prduto existente.')
            else:
                if desejo == 'p':
                    preco[id_item] = float(input("Digite o novo preço doce: "))
                else:
                    doces[id_item] = input('Qual é o novo nome? ')
                print('Essa é sua lista atualizada:')
                listar()
        except ValueError:
            print('Digite apenas números, por favor.')
    else:
        print('Por favor digite "n" para nome ou "p" para preço')

    



def vendas():
    listar()
    i = int(input("Digite a posição do doce que você deseja: ")) - 1
    print(f"O doce vendido foi {doces[i]}")
    volume_doce = int(input(f"Digite quantos {doces[i]} foram vendidos: "))
    volume.append(volume_doce)
    print(f"O valor recebido foi {preco[i] * volume_doce}")


def deletar_produto():
    if not doces:
        print("Nenhum produto cadastrado.")
        return

    listar()
    try:
        e = int(input("posição do doce para deletar: ")) - 1
    except ValueError:
        print("Digite apenas números!")
        return

    if '''e.isdigit()''' and 0 <= int(e) < len(doces):
        i = int(e)
    elif e in doces:
        i = doces.index(e)
    else:
        print("Inválido.")
        return

    print(doces[i], "deletado.")
    del doces[i]
    del preco[i]


def sair():
    return False


def main():
    print("Loja de doce")
    menu()
    op = int(input("Digite a opção: "))
    match(op):
        case 1:
            cadastrar()
        case 2 | 3 | 4 | 5:  #verificar se somente numeros
            if not doces:
                print("Nenhum produto cadastrado ainda. Cadastre primeiro!")
            else:
                if op == 2:
                    listar()
                elif op == 3:
                    atualizar()
                elif op == 4:
                    vendas()
                elif op == 5:
                    deletar_produto()
        case 6:
            confirmar = input("Tem certeza que deseja sair? (s/n): ").lower()
            if confirmar == "s":
                print("Saindo do sistema... Até logo!")
                return False
        case _:
            print("Digite uma das opções abaixo")
    return True

if __name__ == "__main__":
       while True:
          if not main(): 
              break