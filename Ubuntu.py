import uinput
import time
import sys
sys.path.append('/ruta/donde/esta/uinput')
import uinput

# Se tiene que install la libreria uinput, usando el siguietne codigo.
#               "sudo apt-get install python3-uinput"
# Se tiene que ejecutar con "sudo python3 Ubuntu.py"


# Crear un dispositivo de entrada virtual
device = uinput.Device([
    uinput.KEY_ENTER,
])

while True:
# Simular la pulsación de la tecla Enter
    device.emit(uinput.KEY_ENTER, 1)  # Presionar la tecla Enter
    device.emit(uinput.KEY_ENTER, 0)  # Soltar la tecla Enter

    # Esperar un segundo antes de salir
    time.sleep(1)

    print("Yes")

    # if precionana esc enteonce:
        #device.destroy()


# Liberar el dispositivo
device.destroy()
