import time
import Xlib
import Xlib.display as display
from Xlib import X
import ctypes

# Función para simular una pulsación de tecla
def send_key_event(keycode):
    # Simular pulsación de una tecla cualquiera, en este caso 'F24'
    # Código de la tecla 'F24'
    

    # Crear una conexión con el servidor de visualización X
    disp = display.Display()

    # Encontrar el ID de la ventana con el foco actual
    focus_window = disp.get_input_focus().focus


    # Crear un evento de teclado presionado
    press_event = Xlib.protocol.event.KeyPress(
        time=int(time.time()),
        root=disp.screen().root,
        window=focus_window,
        same_screen=0, event=0,
        child=Xlib.X.NONE,
        root_x=0, root_y=0, event_x=0, event_y=0,
        state=0,
        detail=keycode
    )

    # Enviar el evento de teclado presionado
    focus_window.send_event(press_event)
    disp.sync()

    # Crear un evento de teclado liberado
    release_event = Xlib.protocol.event.KeyRelease(
        time=int(time.time()),
        root=disp.screen().root,
        window=focus_window,
        same_screen=0, event=0,
        child=Xlib.X.NONE,
        root_x=0, root_y=0, event_x=0, event_y=0,
        state=0,
        detail=keycode
    )

    # Enviar el evento de teclado liberado
    focus_window.send_event(release_event)
    disp.sync()

# Definir la duración entre cada pulsación de tecla (en segundos)

# Bucle infinito para simular actividad continua
time.sleep(3)

a = 50
while True:
    
    send_key_event(keycode = 36) # Enter
    send_key_event(keycode = 11) # 2
    send_key_event(keycode = 36) # Enter
    #send_key_event(keycode = a ) # 50     # Omitimos este paso para que sea el mismo numero de la vez pasada
    send_key_event(keycode = 36) # Enter   
    send_key_event(keycode = 36) # Enter
    time.sleep(51)
    print("Esperando...")

    
    # send_key_event(keycode = 36)  # Enter 
    # time.sleep(1)

    # Enter
    # Ramdom del 1 al 3
    # Enter
    # Ramdom del 1 al 100
    # Enter
    # Enter
    # time.sleep(Ramdom2)
