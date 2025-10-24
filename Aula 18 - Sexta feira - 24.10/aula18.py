#exe01

while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        soma = n1 + n2
        print(f"A soma de {n1} e {n2} é {soma}.")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

#exe02

def cria_arquivos():
    with open("cats.txt", "w", encoding="utf-8") as cats:
        cats.write("Ninita\n")
        cats.write("Gato de botas\n")
        cats.write("Januário\n")

    with open("dogs.txt", "w", encoding="utf-8") as dogs:
        dogs.write("Nick\n")
        dogs.write("Sexta-Feira\n")
        dogs.write("Hulk\n")


def mostrar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo de {nome_arquivo}:\n{conteudo}")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")


cria_arquivos()
mostrar_arquivo("cats.txt")
mostrar_arquivo("dogs.txt")