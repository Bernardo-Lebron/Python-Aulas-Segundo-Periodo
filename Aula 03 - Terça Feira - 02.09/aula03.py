#exe01

nome = input("Digite seu nome completo: ")

print(f"Maiusculas: {nome.upper()}")
print(f"Minusculas: {nome.lower()}")

nome_sem_espaco = len(nome.replace(" ", ""))
print("Total de letras:", nome_sem_espaco)

primeiro_nome = nome.split()
print("Primeiro Nome:", primeiro_nome[0])

#exe02

frase = input("Digite uma frase: ")

quantidade = frase.lower().count("a")

print("Número de letras 'a' ou 'A': ", quantidade)

#exe03

senha = input("Digite uma senha: ")

tamanho_senha = len(senha)

print("Tamanho da senha:", tamanho_senha)

print("Contém @? ", '@' in senha)

print("Senha longa? ", len(senha)>8)

#exe04

codificador_de_vogais = input("Digite uma frase: ")

print("Frase codificada: ", codificador_de_vogais.lower().replace("a", "1")
    .replace("e", "2").replace("i", "3").replace("o", "4").replace("u", "5"))

#exe05

temperatura = float(input("Informe a temperatura em Celsius: "))

fahrenheit = (temperatura * 1.8) + 32

print("Temperatura em Fahrenheit: ", fahrenheit)

#exe06

raio_circulo = float(input("Informe o raio do círculo: "))

area_circulo = 3.14*(raio_circulo**2)

print("A área do círculo é: ", area_circulo)
