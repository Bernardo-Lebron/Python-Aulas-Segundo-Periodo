import random

def escolher_palavra():
    """Escolhe uma palavra aleatória de uma lista predefinida."""

    palavras = ["MORANGO", "BANANA", "MELANCIA", "CHUTEIRA", "CADERNO", "COMPUTADOR"]
    return random.choice(palavras)


def desenhar_forca(erros):
    """Desenha o estado atual da forca com base no número de erros."""
    
    estagios = [
        """
          _______
         |/      |
         |
         |
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |       |
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \\|
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \\|/
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \\|/
         |       |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \\|/
         |       |
         |      / \\
        _|___
        """
    ]
    print(estagios[erros])


def jogo_forca():
    """Função principal para jogar o jogo da forca."""

    palavra = escolher_palavra()
    letras_tentadas = {}
    erros = 0
    max_erros = 6

    print("=== JOGO DA FORCA ===\n")

    while erros < max_erros:
        desenhar_forca(erros)

        exibicao = ""
        for letra in palavra:
            if letra in letras_tentadas and letras_tentadas[letra]:
                exibicao += letra + " "
            else:
                exibicao += "_ "
        print(f"\nPalavra: {exibicao}")

        chute = input("\nDigite uma letra: ").upper()

        if len(chute) != 1:
            print("Digite apenas uma letra!")
            continue

        if chute in letras_tentadas:
            print("Você já tentou essa letra!")
            continue

        if chute in palavra:
            print("Você acertou uma letra!")
            letras_tentadas[chute] = True
        else:
            print("Letra errada!")
            letras_tentadas[chute] = False
            erros += 1

        venceu = True
        for letra in palavra:
            if letra not in letras_tentadas or not letras_tentadas[letra]:
                venceu = False
                break

        if venceu:
            print(f"\nParabéns! Você acertou, a palavra era: {palavra}")
            break
        
    if erros == max_erros:
        desenhar_forca(erros)
        print("\nVocê foi enforcado!")
        print(f"A palavra era: {palavra}")

jogo_forca()