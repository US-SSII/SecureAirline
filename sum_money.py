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

    for data in range(num_tests):
        # Conversión de tipo de datos
        num1 = np.array([random.randint(0, 100)], dtype=np.int64)
        num2 = np.array([random.randint(0, 100)], dtype=np.int64)

        ctxt1 = encrypt_int(HE, num1)
        ctxt2 = encrypt_int(HE, num2)

        start_time = time.time()
        ctxt_sum = encrypted_addition(HE, ctxt1, ctxt2)
        decrypt_sum = decrypt_int(HE, ctxt_sum)

        end_time = time.time()

        # print("Suma  de", ctxt1, "+", ctxt2, "=", ctxt_sum)
        # print("Suma de", num1[0], "+", num2[0], "=", decrypt_sum[0])

        total_time += (end_time - start_time)

    avg_time_per_test = total_time / num_tests
    print("Tiempo promedio por operación de suma cifrada:", avg_time_per_test, "segundos")


# Configuración de Pyfhel
HE = setup_pyfhel()

# Realizar pruebas con diferentes tamaños de datos
print("Pruebas con 1000 conjuntos de datos:")
perform_tests(HE, 1000)

print("\nPruebas con 10000 conjuntos de datos:")
perform_tests(HE, 10000)

print("\nPruebas con 100000 conjuntos de datos:")
perform_tests(HE, 100000)
