doces = []
preco = []
data = []
volume = []

def menu():
   print("      Armázem Loja de Doce      ") 
   print("1) Cadastrar produto") 
   print("2) Listar produtos cadastrados") 
   print("3) Atualizar lista de produtos") 
   print("4) Deletar produto") 

   '''cadastrar, listar, alterar e deletar'''


def cadastrar(doces, preco):
    nome_doce = input("Digite o produto que será cadastarado: ")
    doces.append(nome_doce)
    preco_doce = float(input("Digite o preço do doce: "))
    preco.append(preco_doce)
    
def vendas (doces, preco, data, volume):
    data_doce = input("Digite  quando a venda foi realizada: ")
    data.append(data_doce)
    volume_doce = int(input(f"Digite quantos {nome_doce} foram vendidos: "))
    volume.append(volume_doce)
    print(f"O valor recebido foi {preco_doce * volume_doce}")


'''def listar():'''

def main():
    print("Loja de doce")
    menu()
    op = int(input("Digite a opção: "))
    match(op):
        case 1: 
            cadastrar(doces, preco)

main()
        