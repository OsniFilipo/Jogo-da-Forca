# Importa o módulo random, necessário para escolher uma palavra aleatória
import random

# Define a função para escolher uma palavra aleatória da lista de palavras
def escolher_palavra():
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
    return random.choice(palavras)

# Define a função para exibir a forca, baseada no número de erros
def exibir_forca(erros):
    # Lista de estágios da forca, representados como strings
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
    return estagios_forca[erros]  # Retorna a string correspondente ao número de erros

# Define a função principal para jogar o jogo da forca
def jogar_forca():
    palavra = escolher_palavra()  # Escolhe uma palavra aleatória da lista
    letras_certas = ["_"] * len(palavra)  # Cria uma lista com underscores para representar as letras ainda não adivinhadas
    letras_erradas = []  # Inicializa uma lista vazia para armazenar letras erradas
    erros = 0  # Contador de erros

    print("Bem-vindo ao jogo da forca!")
    print(exibir_forca(erros))  # Exibe o estágio atual da forca
    print("Palavra:", " ".join(letras_certas))  # Exibe a palavra com os espaços vazios para as letras não adivinhadas

    # Loop principal do jogo
    while True:
        letra = input("Digite uma letra: ").lower()  # Solicita ao jogador que digite uma letra
        
        # Verifica se a letra está na palavra
        if letra in palavra:
            # Substitui o underscore pela letra correta na posição correspondente
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_certas[i] = letra
            print("Palavra:", " ".join(letras_certas))  # Exibe a palavra atualizada
        else:
            letras_erradas.append(letra)  # Adiciona a letra à lista de letras erradas
            erros += 1  # Incrementa o contador de erros
            print(exibir_forca(erros))  # Exibe o estágio atual da forca
            print("Palavra:", " ".join(letras_certas))  # Exibe a palavra atualizada
            print("Letras erradas:", ", ".join(letras_erradas))  # Exibe as letras erradas
        
        # Verifica se o jogador perdeu
        if erros == len(exibir_forca(0).split("\n")) - 1:
            print("Você perdeu! A palavra era:", palavra)
            break
        # Verifica se o jogador ganhou
        elif "_" not in letras_certas:
            print("Parabéns! Você ganhou!")
            break

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    jogar_forca()
