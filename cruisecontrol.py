import time  # Importa la librería time

velocidad_inicial = 40

fin = ""
while fin != "si":
    
    velocidad_deseada = int(input("Seleccione una velocidad: "))

    while velocidad_inicial < velocidad_deseada:
        velocidad_inicial += 2  # Actualiza velocidad_inicial sumando 2
        print(velocidad_inicial)
        time.sleep(0.5)  # Pausa de 0.5 segundos entre cada incremento

    while velocidad_inicial > velocidad_deseada:
        velocidad_inicial -= 1  # Actualiza velocidad_inicial sumando 2
        print(velocidad_inicial)
        time.sleep(0.5)  # Pausa de 0.5 segundos entre cada incremento