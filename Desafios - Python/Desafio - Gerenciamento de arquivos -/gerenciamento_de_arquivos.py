def registrar_erro(mensagem):
    """Registra erros inesperados em um arquivo de log."""

    with open("gerenciamento_erros.log", "a", encoding="utf-8") as log:
        from datetime import datetime
        log.write(f"[{datetime.now()}] {mensagem}\n")


def criar_arquivo():
    '''Função que cria arquivo desejado pelo usuario'''

    nome_arquivo = input("Informe o nome do arquivo que deseja criar: ")

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as conteudo:
            texto = input("Informe o conteudo: ")
            conteudo.write(texto)
            print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
    except PermissionError:
        print(f"Permissão negada! Você não pode criar o arquivo '{nome_arquivo}'.")
    except Exception as erro:
        print(f"ERRO! O arquivo '{nome_arquivo}' não foi criado.")
        registrar_erro(f"Erro ao criar '{nome_arquivo}': {erro}")


def abrir_arquivo():
    '''Função que abre o arquivo que o usuario deseja'''

    nome_arquivo = input("Informe o arquivo que deseja abrir: ")

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as conteudo:
            texto = conteudo.read()
            print(f"Conteúdo de {nome_arquivo}:\n{texto}")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except PermissionError:
        print(f"Permissão negada! Você não pode abrir o arquivo '{nome_arquivo}'.")
    except Exception as erro:
        print(f"Ocorreu um erro ao abrir o arquivo: {erro}")
        registrar_erro(f"Erro ao abrir '{nome_arquivo}': {erro}")
    

def editar_arquivo():
    '''Função que edita o arquivo desejado pelo usuario'''

    nome_arquivo = input("Informe o arquivo que deseja editar: ")

    try:
        open(nome_arquivo, "r", encoding="utf-8").close()
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não existe. Não é possível editá-lo.")
        return

    try:
        with open(nome_arquivo, "a", encoding="utf-8") as conteudo:
            texto = input("Informe o conteúdo que deseja adicionar ao arquivo: ")
            conteudo.write("\n" + texto)
            print(f"Arquivo '{nome_arquivo}' editado com sucesso!")
    except PermissionError:
        print(f"Permissão negada! Você não pode editar o arquivo '{nome_arquivo}'.")
    except Exception as erro:
        print(f"Ocorreu um erro ao editar o arquivo: {erro}")
        registrar_erro(f"Erro ao editar '{nome_arquivo}': {erro}")

    
if __name__ == '__main__':

    while True:
        print("\nGerenciamento de Arquivos\n")
        print("1 - Criar arquivo")
        print("2 - Abrir arquivo")
        print("3 - Editar arquivo")
        print("0 - Encerrar o programa")

        try:
            opcao = int(input("\nQual opção deseja realizar? "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            criar_arquivo()
        elif opcao == 2:
            abrir_arquivo()
        elif opcao == 3:
            editar_arquivo()
        elif opcao == 0:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")