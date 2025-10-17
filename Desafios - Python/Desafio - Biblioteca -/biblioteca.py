class Biblioteca():
    def __init__(self):
        self.livros_disponiveis = ["Helena", "Dom Casmurro", "Vidas Secas", "O Cortiço"]
        self.livros_emprestados = {
            "O Pequeno Príncipe": "Ana",
            "1984": "Bruno"
        }

    
    def adicionar_livro(self, titulo):
        """Adiciona um novo livro a lista de livros disponiveis"""

        self.livros_disponiveis.append(titulo)
        print()

    
    def remover_livro(self, titulo):
        """Remove um livro da lista de livros disponíveis"""
        
        if titulo in self.livros_disponiveis:
            self.livros_disponiveis.remove(titulo)
            print("Livro removido com sucesso!")
            print()
        else:
            print("\nLivro não encontrado na base de dados.")
            print()

    
    def exibir_livros(self):
        """Exibe a lista de livros disponiveis"""

        if not self.livros_disponiveis:
            print("\nNenhum livro disponível!")
            print()
        else:
            print(f"\nLivros disponíveis:\n ")
            for livro in self.livros_disponiveis:
                print(f" - {livro}")
            print()

    def exibir_livros_emprestados(self):
        """Exibe a lista de livros emprestados"""

        if not self.livros_emprestados:
            print("\nNenhum livro emprestado!")
            print()
        else:
            print("\nLivros emprestados:\n")
            for livro, usuario in self.livros_emprestados.items():
                print(f" - {livro}, emprestado para {usuario}")
            print()

    def emprestimo_livro(self):
        """Realiza o emprestimo de um livro disponivel para um usuario"""

        livro = input("\nQual livro deseja emprestar? ")
        if livro not in self.livros_disponiveis:
            print("Livro não disponivel para emprestimo!")
            print()
        else:
            usuario = input("\nQuem deseja realizar o emprestimo? ")
            self.livros_disponiveis.remove(livro)
            self.livros_emprestados[livro] = usuario
            print("Emprestimo de livro realizado com sucesso!")
            print()

biblioteca = Biblioteca()

while True:
    print("\nBem-vindo à Biblioteca!\n")
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Exibir livros disponíveis")
    print("4. Exibir livros emprestados")
    print("5. Empréstimo de livro")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        titulo = input("\nQual livro deseja adicionar a biblioteca? ")
        biblioteca.adicionar_livro(titulo)
    elif escolha == '2':
        titulo = input("\nQual livros deseja remover da biblioteca? ")
        biblioteca.remover_livro(titulo)
    elif escolha == '3':
        biblioteca.exibir_livros()
    elif escolha == '4':
        biblioteca.exibir_livros_emprestados()
    elif escolha == '5':
        biblioteca.emprestimo_livro()
    elif escolha == '0':
        print("Encerrando o programa!")
        break
    else:
        print("Opção inválida. Tente novamente.")