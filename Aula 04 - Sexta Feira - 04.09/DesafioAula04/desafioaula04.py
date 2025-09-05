nome_completo = input("Informe o nome completo: ")
idade = input("Informe a idade: ")
senha = input("Informe a senha: ")

if not nome_completo:
    print("Inválido")
elif not idade.isnumeric():
    print("Inválido")
elif int(idade) < 18:
    print("Idade inválida")
elif senha == "1234":
    print("Essa senha não pode ser usada")
elif senha.lower().startswith("admin"):
    print("Essa senha não pode ser usada")
else:
    print("Acesso Liberado!")

if nome_completo.lower().startswith(("a", "e", "i", "o", "u")):
    print("O nome começa com uma vogal.")
else:
    print("O nome não começa com uma vogal.")

idade_bool = bool(int(idade))
print(f"Idade como booleano: {idade_bool}")

if senha.isnumeric():
    print(f"Senha numérica + 10 = {int(senha) + 10}")
else:
    print("A senha não é numérica.")