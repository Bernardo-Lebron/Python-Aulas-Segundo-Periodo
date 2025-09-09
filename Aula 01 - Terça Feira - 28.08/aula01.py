#Primeiro programa

nome = 'Bernardo Lebron'

idade = 21

print(f"{nome} tem {idade} anos!")

valor = 123.456

print(f"Valor formatado: {valor:.1f}")

valor1 = 0.4

print(f"Valor formatado: {valor1:.1%}")

print(f"Valor formatado: {valor1:>6}")

print(f"Valor formatado: {valor1:^6}")

print(f"Valor formatado: {valor1:<6}")

print(f"Valor formatado: {valor1:-^9}")

print("Olá, {}!" .format(nome))

print("O aluno {} tirou nota {}." .format(nome, 9.5))

print("Nome: {0}, Nota {1}, \nNome novamente: {0}" .format(nome, 9.5))

print("Valor {}".format(valor))