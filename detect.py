import random
import time
import pandas as pd
from person import Person

def detect(criminals, suspects):
    detected = []
    start_time = time.time()
    for suspect in suspects:
        if suspect in criminals:
            detected.append(suspect)
            print("Criminal detected: " + str(suspect))
    if len(detected) == 0:
        print("No criminals detected")
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time: {:.6f} seconds".format(execution_time))
    return execution_time

# Función para generar listas de personas
def generate_people_list(num_people):
    people = []
    for i in range(num_people):
        name = "Person" + str(i)
        age = i % 100  # Just for variety in ages
        people.append(Person(name, age).generate_hash())
    return people

# Prueba de eficiencia con diferentes tamaños de entrada
results = []
sizes = [100, 500, 1000, 5000, 10000]
for size in sizes:
    print("Tamaño de entrada:", size)
    criminals = generate_people_list(size // random.randint(2, 10))
    suspects = generate_people_list(size)
    execution_time = detect(criminals, suspects)
    results.append((size, execution_time))

# Crear DataFrame con los resultados
df = pd.DataFrame(results, columns=["Tamaño de entrada", "Tiempo de ejecución (segundos)"])
print("\nResultados:")
print(df)
