#GENERAR UNA PALABRA SECRETA
import random

def generar_palabra_secreta():
    palabras = [
        'mono', 'perro', 'gato', 'loro', 'gorila', 'zorro', 'aguila', 'hamster', 'tigre', 'leon'
    ]

    numero_random = random.randint(palabras.lenght)
    palabra = palabras[numero_random]
    return palabra