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


def mostrar_tablero(tablero,palabra_secreta):
    list(palabra_secreta)
    print(tablero)
    print(palabra_secreta)

mostrar_tablero(imagenes_ahorcado[0],generar_palabra_secreta())