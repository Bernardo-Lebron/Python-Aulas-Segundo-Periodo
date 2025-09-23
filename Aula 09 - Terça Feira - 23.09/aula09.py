nomes = []
datas = []
enderecos = []
telefones = []

while True:
    print("-- Lista de contatos --\n\n"
        "1 - Inserir contato\n" \
        "2 - Remover contato\n" \
        "3 - Pesquisar um contato pelo nome\n" \
        "4 - listar todos os contatos\n" \
        "5 - Listar os contatos cujo nome inicia se com uma dada letra\n" \
        "6 - Rmprimir os aniversariantes do mês\n" \
        "7 - Encerrar o programa")

    var = int(input("\nDigite um comando: "))

    match var:
        case 1:
            nome = input("Informe o nome: ")
            nomes.append(nome)
            data = input("Informe a data de nascimento: ")
            datas.append(data)
            endereco = input("Informe o endereço: ")
            enderecos.append(endereco)
            telefone = input("Informe o telefone: ")
            telefones.append(telefone)

        case 2:
            print(nomes)
            indice = int(input("Informe o indice do contato que você deseja remover: "))
            nomes.pop(indice)
            datas.pop(indice)
            enderecos.pop(indice)
            telefones.pop(indice)
            print(nomes)
            print("Contato removido!")

        case 3:
            pesquisar = input("Pesquisar contato: ")
            if pesquisar in nome:
                print(f"{pesquisar} está na lista de contatos!")
            else:
                print(f"{pesquisar} não está na lista de contatos")

        case 4:
            for i in range(len(nomes)):
                print(f"{i} - {nome} | {datas[i]} | {enderecos[i]} | {telefones[i]}")

        case 5:
            letra_inicial = input("Informe a letra que deseja procurar os contatos: ").upper()
            for i, nome in enumerate(nomes):
                if nome.upper().startswith(letra_inicial):
                    print(f"{i} - {nome} | {datas[i]} | {enderecos[i]} | {telefones[i]}")

        case 6:
            input("Informe um mês em número: ")
            print("Os aniversariantes do mês são: ")
        case 7:
            break