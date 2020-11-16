import random

imagenes_ahorcado = [
    """
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

    palabra_secreta = random.choices(palabras)

    return palabra_secreta

def mostrar_tablero(intentos):
    if intentos == 0:
        print('     A H O R C A D O')
    print(imagenes_ahorcado[intentos])

def main():
    palabra_generada = generar_palabra_secreta()
    list(palabra_generada)

    print(palabra_generada)

if __name__ == '__main__':
    main()