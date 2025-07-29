import tkinter as tk  # Se importa el módulo tkinter para crear la interfaz gráfica.
from Avion import Avion  # Se importa la clase Avion desde el archivo Avion.py.
from Interfaz import InterfazReserva  # Se importa la clase InterfazReserva desde el archivo Interfaz.py.

if __name__ == "__main__":  # Punto de entrada del programa, se asegura de que el código solo se ejecute si el archivo es el principal.
    avion = Avion("Boeing 737", 8, 12)  # Se crea una instancia de la clase Avion con el modelo "Boeing 737", 8 asientos Business y 12 Turista.

    root = tk.Tk()  # Se crea la ventana principal de la interfaz gráfica.
    app = InterfazReserva(root, avion)  # Se crea una instancia de la interfaz de reserva, pasando la ventana y el avión.
    root.mainloop()  # Se inicia el bucle principal de tkinter para que la interfaz se mantenga abierta.