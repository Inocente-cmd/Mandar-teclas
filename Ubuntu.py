import uinput
import time

# Crear un dispositivo de entrada virtual
device = uinput.Device([
    uinput.KEY_ENTER,
    uinput.KEY_1,  # Agregar la tecla 1 al dispositivo virtual
    uinput.KEY_0,  # Agregar la tecla 0 al dispositivo virtual
    uinput.KEY_2,  # Agregar la tecla 2 al dispositivo virtual
    uinput.KEY_9
])

print("Tienes 3 sec para posicionarte")
time.sleep(3)
print("Ya")

while True:
    # ANTES DE AÑADIR UN NUEMRO, HAY AÑADIR LA TECLA VIRTUAL EN LA LINEA 5
    # Comprobador de archivo, si hay un archivo llamado "Hello World":
                    # Mandar mensaje a whatsappy
                    # device.destroy()
    
    # Simular pulsaciones de teclas
    device.emit(uinput.KEY_ENTER, 1)  # Presionar la tecla Enter
    device.emit(uinput.KEY_ENTER, 0)  # Soltar la tecla Enter
    print("Enter")
    time.sleep(1)

    device.emit(uinput.KEY_2, 1)  # Presionar la tecla 2
    device.emit(uinput.KEY_2, 0)  # Soltar la tecla 2
    print("2")
    time.sleep(1)

    device.emit(uinput.KEY_ENTER, 1)  # Presionar la tecla Enter
    device.emit(uinput.KEY_ENTER, 0)  # Soltar la tecla Enter
    print("Enter")
    time.sleep(1)

    device.emit(uinput.KEY_9, 1)  # Presionar la tecla 1
    device.emit(uinput.KEY_9, 0)  # Soltar la tecla 1
    print("9")
    #time.sleep()

    device.emit(uinput.KEY_0, 1)  # Presionar la tecla 0
    device.emit(uinput.KEY_0, 0)  # Soltar la tecla 0
    print("0")
    #time.sleep()

    device.emit(uinput.KEY_ENTER, 1)  # Presionar la tecla Enter
    device.emit(uinput.KEY_ENTER, 0)  # Soltar la tecla Enter
    print("Enter")
    time.sleep(1)

    device.emit(uinput.KEY_ENTER, 1)  # Presionar la tecla Enter
    device.emit(uinput.KEY_ENTER, 0)  # Soltar la tecla Enter
    print("Enter")
    print("Esperando...")
    time.sleep(105) # añadir 15s mas del tiempo original
    print("Ya paso el tiempo")

# Liberar el dispositivo
device.destroy()
