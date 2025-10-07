#exe01
def msg():
    """Exibe a mensagem 'Hello, World!' na tela."""
    print("Hello, World!")


print(msg .__doc__)
help(msg)


msg()

#exe02
def make_album(artista, album,):
    """Exibe o nome do artista e um álbum."""

    return{'artista': artista, 'album': album}



while True:
    artista = input("Informe o nome de um artista: ")
    album = input("Informe o nome de um álbum desse artista: ")
    make_album(artista, album)
    resposta = input("Deseja informar outro álbum? (s/n) ")
    if resposta.lower() == 'n':
        break

album_info = make_album(artista, album)
print(f"{album_info}")

 