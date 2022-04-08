import serial
import time
from matplotlib import image
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image


arduino = serial.Serial('COM3', 9600, timeout=1)
print('Conectado')


hot = 31
cold = 25

def imge():
    ventana = Tk()
    ventana.title('CALOR ¡ADVERTENCIA!')
    ventana.iconbitmap(r'C:\Users\EDISSON\Desktop\TAREAS DE PROGRAMACION\Laboratorio8.1\ad.ico')

    imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\EDISSON\Desktop\TAREAS DE PROGRAMACION\Laboratorio8.1\caloor.png').resize((500,500)))
    boton = Button(image=imagen, command=ventana.quit)
    boton.pack()
    ventana.mainloop()

while True:
    data = arduino.readline().decode().strip()
    time.sleep(1)

    if data:
        data = float(data)
        print(data)

        if data >= hot:
            print(imge())
    