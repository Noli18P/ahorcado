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

    n = random.randint(0, len(palabras))
    palabra_secreta = palabras[n]

    return palabra_secreta


def main():
    palabra_generada = generar_palabra_secreta()
    palabra = ''
    vidas = 5
    intentos = 0

    while vidas >= 0:
        error = 0
        for letra in palabra_generada:
            if letra in palabra:
                print(letra,end=(' '))
            else:
                print('_',end=(' ')) 
                error += 1
        if error == 0:
            print('\nFelicidades la palabra ers: ', palabra_generada)
            break
        
        if vidas == 0:
            break
        else:
            print(imagenes_ahorcado[intentos])
            letra_usuario = input('\nIntroduce una letra: ').lower()
            palabra += letra_usuario
            
    
        if letra_usuario not in palabra_generada:
            vidas -= 1
            intentos += 1
            print('\nError! Intentalo de nuevo')
    
        
        if vidas == 0:
            print(imagenes_ahorcado[6])
            print("\nPerdiste! La palabra era: ", palabra_generada)
    

if __name__ == '__main__':
    main()