frase = input("Digite uma frase: ") #pede a frase ao usuario

lista_de_palavras = frase.split() #separa a frase em espaços

#informa quantas palavras unicas tem na frase
palavras_unicas = []

for palavra in lista_de_palavras:
    if (palavra not in palavras_unicas):
        palavras_unicas.append(palavra)

print(f"Total de palavras unicas: {len(palavras_unicas)}")

#informa qual a maior e a menor palavra da frase
palavra_maior = lista_de_palavras[0]
palavra_menor = lista_de_palavras[0]

for palavra in lista_de_palavras:
    if len(palavra) > len(palavra_maior):
        palavra_maior = palavra
    if len(palavra) < len(palavra_menor):
        palavra_menor = palavra

print(f"A maior palavra digitada foi: {palavra_maior}")
print(f"A menor palavra digitada foi: {palavra_menor}")

#informa quais as palavras da frase começam com vogal
vogais = ("a","e","i","o","u","á","é","í","ó","ú","à","è","ì","ò","ù","ã","õ","â","ê","ô","î")

palavras_vogais = []

for palavra in lista_de_palavras:
    if (palavra.lower().startswith(vogais)):
        palavras_vogais.append(palavra)

print(f"Palavras que iniciam com vogais: {palavras_vogais}")

#inverte as palavras da frase
palavras_invertidas = []

for palavra in lista_de_palavras:
    palavras_invertidas.append(palavra[::-1])

print(f"Frase invertida: {" ".join(palavras_invertidas)}")

#informa a media de caracteres por palavra
soma_tamanhos = 0

for palavras in lista_de_palavras:
    soma_tamanhos += len(palavras)

media = soma_tamanhos / len(lista_de_palavras)

print(f"Media de caracteres por palavra: {media:.2f}")

#inverte a frase em ordem alfabética
lista_ordenada = lista_de_palavras[:] 
lista_ordenada.sort() 

print(f"Palavras em ordem alfabética inversa: {lista_ordenada[::-1]}")