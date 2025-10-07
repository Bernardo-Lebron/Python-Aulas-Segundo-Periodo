estoque = {
    "Parafuso" : {"quantidade": 100, "preco": 0.50},
    "Prego" : {"quantidade": 200, "preco": 0.30},
    "Martelo" : {"quantidade": 50, "preco": 19.90},
    "Chave de Fenda" : {"quantidade": 30, "preco": 29.90},
    "Alicate" : {"quantidade": 80, "preco": 14.90}
}

def exibir_estoque():
    """Exibe o estoque atual"""

    print("\nEstoque Atual:")
    for produto, dados in estoque.items():
        print(f"{produto}: Quantidade = {dados['quantidade']}, Preço = R${dados['preco']:.2f}")
    print("\n")


def adicionar_produto():
    """Adiciona um novo produto ao estoque"""

    nome = input("Nome do produto: ")
    if nome in estoque:
        print("Produto já existe no estoque.\n")
        return
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque[nome] = {"quantidade": quantidade, "preco": preco}
    print("Produto adicionado ao estoque.\n")


def atualizar_produto():
    """Atualiza a quantidade e o preço de um produto existente no estoque"""

    nome = input("Nome do produto a ser atualizado: ")
    if nome not in estoque:
        print("Produto não encontrado no estoque.\n")
        return
    quantidade = int(input("Nova quantidade: "))
    preco = float(input("Novo preço: "))
    estoque[nome] = {"quantidade": quantidade, "preco": preco}
    print("Produto atualizado.\n")


def calcular_valor_total():
    """Calcula e exibe o valor total do estoque"""

    total = 0
    for produto in estoque.values():
        total += produto["quantidade"] * produto["preco"]
    print(f"\nValor total do estoque: R${total:.2f}")
    print("\n")


def remover_produto():
    """Remove um produto do estoque"""

    nome = input("Nome do produto a ser removido: ")
    if nome not in estoque:
        print("Produto não encontrado no estoque.\n")
        return
    del estoque[nome]
    print("Produto removido do estoque.\n")


def exibir_estoque_ordenado_por_nome():
    """Exibe o estoque ordenado por nome do produto"""

    print("\nEstoque Ordenado por Nome:")
    for produto in sorted(estoque.keys()):
        dados = estoque[produto]
        print(f"{produto}: Quantidade = {dados['quantidade']}, Preço = R${dados['preco']:.2f}")
    print("\n")


def exibir_estoque_ordenado_por_valor():
    """Exibe o estoque ordenado pelo valor total (quantidade * preço) do produto"""

    print("\nEstoque Ordenado por Valor Total (maior para menor):")
    produtos_ordenados = sorted(estoque.items(),key=lambda item: item[1]["quantidade"] * item[1]["preco"],reverse=True)
    for produto, dados in produtos_ordenados:
        valor_total = dados["quantidade"] * dados["preco"]
        print(f"{produto}: Quantidade = {dados['quantidade']}, "f"Preço = R${dados['preco']:.2f}, "f"Valor total = R${valor_total:.2f}")
    print("\n")


while True:
    
    print("-- Gerenciamento de Estoque --\n")
    print("1 - Exibir estoque")
    print("2 - Adicionar produto")
    print("3 - Atualizar produto")
    print("4 - Calcular valor total do estoque")
    print("5 - Remover produto")
    print("6 - Exibir estoque ordenado por nome")
    print("7 - Exibir estoque ordenado por valor total")
    print("0 - Sair\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_estoque()
    elif opcao == "2":
        adicionar_produto()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        calcular_valor_total()
    elif opcao == "5":
        remover_produto()
    elif opcao == "6":
        exibir_estoque_ordenado_por_nome()
    elif opcao == "7":
        exibir_estoque_ordenado_por_valor()
    elif opcao == "0":
        print("Encerrando o programa...\n")
        break
    else:
        print("Opção inválida.\n")

