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
