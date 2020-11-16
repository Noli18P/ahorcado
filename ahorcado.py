#GENERAR UNA PALABRA SECRETA
import random

def generar_palabra_secreta():
    palabras = [
        'mono', 'perro', 'gato', 'loro', 'gorila', 'zorro', 'aguila', 'hamster', 'tigre', 'leon', 'raton',
        'huron', 'tortuga', 'cucaracha', 'cuervo', 'gusano', 'colibri', 'serpiente', 'nutria', 'pato'
    ]

    numero_random = random.randint(0, len(palabras) - 1)
    palabra = palabras[numero_random]
    
    return palabra

palabra_random = generar_palabra_secreta()
print(palabra_random)