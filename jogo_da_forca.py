import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
    return random.choice(palavras)

def exibir_forca(erros):
    estagios_forca = [
        """
        |------
        |     |
        |
        |
        |
        |
        -
        """,
        """
        |------
        |     |
        |     O
        |
        |
        |
        -
        """,
        """
        |------
        |     |
        |     O
        |     |
        |
        |
        -
        """,
        """
        |------
        |     |
        |     O
        |    /|
        |
        |
        -
        """,
        """
        |------
        |     |
        |     O
        |    /|\\
        |
        |
        -
        """,
        """
        |------
        |     |
        |     O
        |    /|\\
        |    /
        |
        -
        """,
        """
        |------
        |     |
        |     O
        |    /|\\
        |    / \\
        |
        -
        """
    ]
    return estagios_forca[erros]

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = ["_"] * len(palavra)
    letras_erradas = []
    erros = 0

    print("Bem-vindo ao jogo da forca!")
    print(exibir_forca(erros))
    print("Palavra:", " ".join(letras_certas))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_certas[i] = letra
            print("Palavra:", " ".join(letras_certas))
        else:
            letras_erradas.append(letra)
            erros += 1
            print(exibir_forca(erros))
            print("Palavra:", " ".join(letras_certas))
            print("Letras erradas:", ", ".join(letras_erradas))

        if erros == len(exibir_forca(0).split("\n")) - 1:
            print("Você perdeu! A palavra era:", palavra)
            break
        elif "_" not in letras_certas:
            print("Parabéns! Você ganhou!")
            break

if __name__ == "__main__":
    jogar_forca()
