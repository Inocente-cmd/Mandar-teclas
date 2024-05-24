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


"""
0x08: Tecla Retroceso (Backspace)
0x09: Tecla Tabulación (Tab)
0x0D: Tecla Enter
0x1B: Tecla Escape
0x20: Barra Espaciadora
0x25: Tecla Flecha Izquierda
0x26: Tecla Flecha Arriba
0x27: Tecla Flecha Derecha
0x28: Tecla Flecha Abajo
0x30 a 0x39: Teclas de 0 a 9
0x41 a 0x5A: Teclas de A a Z
0x60 a 0x69: Teclas Numéricas (0 a 9) en el teclado numérico
0x70 a 0x87: Teclas de Función (F1 a F24)
"""
