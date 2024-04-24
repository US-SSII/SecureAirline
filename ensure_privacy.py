import random
import time

import numpy as np
from Pyfhel import Pyfhel


# Función para generar un objeto Pyfhel con la configuración adecuada
def setup_pyfhel():
    HE = Pyfhel()
    HE.contextGen(scheme='bfv', n=2**14, t_bits=20)  # Generar contexto con los mismos parámetros
    HE.keyGen()  # Generar claves
    return HE

# Función para cifrar un número entero utilizando Pyfhel
def encrypt_int(HE, number):
    return HE.encryptInt(number)

# Función para descifrar un número entero cifrado utilizando Pyfhel
def decrypt_int(HE, ciphertext):
    return HE.decryptInt(ciphertext)

# Función para sumar dos números enteros cifrados
def encrypted_addition(HE, ctxt1, ctxt2):
    return ctxt1 + ctxt2

# Función para realizar pruebas de suma con datos cifrados
def perform_tests(HE, asked, num=5):
    total_time = 0

    data = [encrypt_int(HE, number) for number in asked]

    start_time = time.time()

    found = []

    for number in asked[:num]:
        print("Número a buscar:", number)
        print("Números encontrados:", [decrypt_int(HE, ctxt) for ctxt in data])
        if any(np.array_equal(number, decrypt_int(HE, ctxt)) for ctxt in data):
            found.append(decrypt_int(HE, number))

    end_time = time.time()

    print("Cantidad de precios encontrados:", len(found))

    total_time += (end_time - start_time)

    print("Tiempo total:", total_time, "segundos")




# Configuración de Pyfhel
HE = setup_pyfhel()

# Realizar pruebas con diferentes tamaños de datos
print("Pruebas con 1000 conjuntos de datos:")
perform_tests(HE, [np.array([random.randint(0, 100)], dtype=np.int64) for _ in range(100)])

print("\nPruebas con 10000 conjuntos de datos:")
perform_tests(HE, [np.array([random.randint(0, 100)], dtype=np.int64) for _ in range(100)])

print("\nPruebas con 100000 conjuntos de datos:")
perform_tests(HE, [np.array([random.randint(0, 100)], dtype=np.int64) for _ in range(100000)])