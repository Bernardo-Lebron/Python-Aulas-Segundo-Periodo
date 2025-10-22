arquivo = r"C:\Users\berna\OneDrive\Área de Trabalho\2 Periodo\Python\Aula 17 - Terça feira - 21.10\learning_python.txt"


with open(arquivo) as file_object:
    conteudo = file_object.read()
print("Leitura completa")
print(conteudo.strip(), "\n")

print("Leitura linha a linha")
with open(arquivo) as file_object:
    for linha in file_object:
        print(linha.strip())
print()

print("Leitura usando lista de linhas")
with open(arquivo) as file_object:
    linhas = file_object.readlines()

for linha in linhas:
    print(linha.strip())
