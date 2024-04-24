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
def perform_tests(HE, num_tests):
    total_time = 0

    data = [np.array([random.randint(0, 100)], dtype=np.int64) for _ in range(num_tests)]

    sum = sum([data[i] for i in range(num_tests)])

    zero = np.array([0], dtype=np.int64)

    sum_encrypted = encrypt_int(HE, zero)

    start_time = time.time()

    for number in data:
        ctxt = encrypt_int(HE, number)
        sum_encrypted = encrypted_addition(HE, sum, ctxt)

    end_time = time.time()



    print("Total encriptado = ", decrypt_int(HE, sum_encrypted))
    print("Total desencriptado = ", sum)

    total_time += (end_time - start_time)

    print("Tiempo total:", total_time, "segundos")


# Configuración de Pyfhel
HE = setup_pyfhel()

# Realizar pruebas con diferentes tamaños de datos
print("Pruebas con 1000 conjuntos de datos:")
perform_tests(HE, 1000)

print("\nPruebas con 10000 conjuntos de datos:")
perform_tests(HE, 10000)

print("\nPruebas con 100000 conjuntos de datos:")
perform_tests(HE, 100000)
