#exe01

numeros = list(range(1,101))

primos = []

print(numeros)

for n in numeros:
    if n>1: 
        primo = True
        for i in range(2,int(n**0.5)+1):
            if (n % i == 0):
                primo = False
                break
        if primo:
            primos.append(n)

print(primos)

#exe02

frase = input("Digite uma frase: ")

vogais = ["a", "e", "i", "o", "u"]
consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

contador_vogais = 0
contador_consoates = 0

for i in frase.lower():
    if(i in vogais):
        contador_vogais += 1
    elif(i in consoantes):
        contador_consoates += 1

print(f"Existem {contador_vogais} vogais na frase!")
print(f"Existem {contador_consoates} consoantes na frase!")
print("Contém a palavra 'engenharia'? ", 'engenharia' in frase)

print(frase[::-1])

#exe03

notas = []

for i in range(3):
    nota = float(input("Informe uma nota: "))
    notas.append(nota)

media = sum(notas)/len(notas)
maior = max(notas)
menor = min(notas)

print(f"A média é: {media}")
print(f"A maior é: {maior}")
print(f"A menor é: {menor}")

#exe04

especiais = "!@#$%¨&*()"

print("Informe uma senha!\nRequisitos:")
print("Pelo menos 8 caracteres")
print("Pelo menos 1 letra maiúscula")
print("Pelo menos 1 letra minúscula")
print("Pelo menos 1 número")
print("Pelo menos 1 caractere especial")
print("A senha não pode ter espaços")

senha = input("\nInforme uma senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False
tem_espaco = False

for char in senha:
    if char.isupper():
        tem_maiuscula = True
    if char.islower():
        tem_minuscula = True
    if char.isdigit():
        tem_numero = True
    if char in especiais:
        tem_especial = True
    if char == " ":
        tem_espaco = True

erros = []

if len(senha) < 8:
    erros.append("Inválido! A senha contém menos de 8 caracteres")
if not tem_maiuscula:
    erros.append("Inválido! A senha não possui letra maiúscula")
if not tem_minuscula:
    erros.append("Inválido! A senha não possui letra minúscula")
if not tem_numero:
    erros.append("Inválido! A senha não possui número")
if not tem_especial:
    erros.append("Inválido! A senha não possui caractere especial")
if tem_espaco:
    erros.append("Inválido! A senha possui espaços")

if erros:
    for erro in erros:
        print(erro)
else:
    print("Senha aceita!")

