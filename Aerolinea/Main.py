import tkinter as tk  # Se importa el módulo tkinter para crear la interfaz gráfica.
from Avion import Avion  # Se importa la clase Avion desde el archivo Avion.py.
from Interfaz import InterfazReserva  # Se importa la clase InterfazReserva desde el archivo Interfaz.py.

if __name__ == "__main__":
    from Avion import Avion
    import tkinter as tk

    avion = Avion("Boeing 737", 8, 12)
    root = tk.Tk()
    root.geometry("1200x650")
    app = InterfazReserva(root, avion)
    root.mainloop()
