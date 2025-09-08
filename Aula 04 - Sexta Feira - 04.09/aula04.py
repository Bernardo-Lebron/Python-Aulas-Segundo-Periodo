###### exercicio 1

chovendo = False

if not chovendo:
    print("vou passear")
else:
    print("vou ficar em casa")

###### exercicio 2

usuario_logado = None

if not usuario_logado:
    print("Faça o login para continuar.")
else: 
    print(f"Bem vindo, {usuario_logado}")

usuario_logado = "Alice"

if not usuario_logado:
    print("Faça login para continuar")
else:
    print(f"Bem vindo, {usuario_logado}")

###### exercicio 3

idade = int(input("Informe a sua idade: "))

if idade < 16:
    print("Você não pode votar!")
elif idade >=16 and idade <=17:
    print("Você pode votar (voto facultativo)")
elif idade >= 18 and idade <= 70:
    print("Você pode votar (voto obrigatório)")
elif idade > 70:
    print("Você pode votar (voto facultativo)") 

###### exercicio 4

peso = float(input("Informe seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / (altura * altura)

print(f"O seu IMC é {imc:.2f}", end="\n")

if imc < 18.5:
    print("Abaixo do peso!")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal!")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso!")
else:
    print("Obesidade!")

###### exercicio 5

numero = int(input("Informe um número: "))

if numero % 2 == 0:
    print("O numero é par!")
else:
    print("O numero é ímpar!")

if numero == 0:
    print("O numero é zero!")
elif numero > 0:
    print("O número é positivo!")
else:
    print("O número é negativo!")

###### exercicio 6

usuario_correto = "admin"
senha_correta = "123"

usuario = input("Informe o usuário: ")
senha = input("Informe a senha: ")

if usuario_correto == usuario and senha_correta == senha:
    print("Autenticação bem-sucedida!")
else : 
    print("Usuário ou senha incorretos!")

###### exercicio 7

temperatura = float(input("Temperatura: "))
unidade_original = input("Unidade original (C/F): ").upper()
unidade_destino = input("Converter para (C/F): ").upper()

if unidade_original == "C" and unidade_destino == "F":
    temp_convertida = (temperatura * 9/5) + 32
    print(f"{temperatura} Celsius é igual a {temp_convertida:.1f} Fahrenheit: ")
elif unidade_original == "F" and unidade_destino == "C":
    temp_convertida = (temperatura - 32) + 5/9
    print(f"{temperatura} Fahrenheit é igual a {temp_convertida:.1f} Celsius: ")
elif unidade_original == unidade_destino:
    print(f"As unidade são as mesmas. A temperatura é {temperatura:.1f}")
else:
    print("Unidade inválidas. Por favor, use 'C' para Celsius ou 'F' para Fahrenheit")
