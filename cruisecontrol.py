import time  # Con esta libreria podremos simular la aceleración o desaceleración del vehiculo

velocidad_actual = 0 # Velocidad del vehiculo
fin = ""
while fin != "si":
    
    velocidad_deseada = int(input("Seleccione una velocidad: ")) # Aqui el usuario seleccionará la velocidad a la que desea estar

    while velocidad_actual < velocidad_deseada:
        velocidad_actual += 2  # Actualiza la velocidad actual del vehiculo sumando 2
        print(velocidad_actual)
        time.sleep(0.5)  # Pausa de 0.5 segundos entre cada incremento para simular la aceleración del vehiculo

    while velocidad_actual > velocidad_deseada:
        velocidad_actual -= 1  # Actualiza la velocidad actual del vehiculo restando 2
        print(velocidad_actual)
        time.sleep(0.5)  # Pausa de 0.5 segundos entre cada resta para simular la desaceleración del vehiculo
