#GENERAR UNA PALABRA SECRETA
import random

imagenes_ahorcado = ["""
    A H O R C A D O
      +---+
      |   |
          |
          |
          |
          |
    =========
    """, """
      +---+
      |   |
      0   |
          |
          |
          |
    =========
    """, """
      +---+
      |   |
      0   |
      |   |
          |
          |
    =========
    """, """
      +---+
      |   |
      0   |
     /|   |
          |
          |
    =========
    """, """
      +---+
      |   |
      0   |
     /|\  |
          |
          |
    =========
    """, """
      +---+
      |   |
      0   |
     /|\  |
     /    |
          |
    =========
    """, """
      +---+
      |   |
      0   |
     /|\  |
     / \  |
          |
    =========
    """]


def generar_palabra_secreta():
    palabras = [
        'mono', 'perro', 'gato', 'loro', 'gorila', 'zorro', 'aguila', 'hamster', 'tigre', 'leon', 'raton',
        'huron', 'tortuga', 'cucaracha', 'cuervo', 'gusano', 'colibri', 'serpiente', 'nutria', 'pato'
    ]

    numero_random = random.randint(0, len(palabras) - 1)
    palabra = palabras[numero_random]
    
    return list(palabra)


def mostrar_tablero(palabra_secreta):
    list(palabra_secreta)
    intentos = 0
    print(imagenes_ahorcado[intentos])
    print('Letras incorrectas: ')

    print(palabra_secreta[0], end=(' '))
    longitud_palabra = len(palabra_secreta)

    for letra in range(longitud_palabra - 1):
        print('_', end=(' '))
    print('\nAdivina una letra: ')
    letra_usuario = input()


mostrar_tablero(generar_palabra_secreta())