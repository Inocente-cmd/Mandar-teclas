import ctypes
import time

#Virtual Key (VK) Microsft

# Función para simular una pulsación de tecla
def send_key_event():
    # Simular pulsación de una tecla cualquiera, en este caso 'F24'
    ctypes.windll.user32.keybd_event(0x87, 0, 0, 0)
    ctypes.windll.user32.keybd_event(0x87, 0, 2, 0)

# Definir la duración entre cada pulsación de tecla (en segundos)
intervalo_actividad = 60  # por ejemplo, cada 60 segundos

# Bucle infinito para simular actividad continua
while True:
    # Simular pulsación de tecla
    send_key_event()

    # Esperar el intervalo de tiempo antes de la próxima actividad
    time.sleep(intervalo_actividad)