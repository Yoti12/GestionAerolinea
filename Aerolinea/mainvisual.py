import tkinter as tk
from tkinter import messagebox

from Pasajero import Pasajero
from Maleta import Maleta
from Avion import Avion
from Clase import Clase

# Creamos el avión
avion = Avion("Boeing 737", 8, 12)  # 8 asientos business, 12 turista

def reservar_asiento():
    try:
        # Leer los valores del formulario
        nombre = entry_nombre.get()
        pasaporte = entry_pasaporte.get()
        telefono = entry_telefono.get()
        edad = int(entry_edad.get())

        peso = float(entry_peso.get())
        largo = float(entry_largo.get())
        ancho = float(entry_ancho.get())
        alto = float(entry_alto.get())

        fila = int(entry_fila.get())
        butaca = int(entry_butaca.get())
        clase = Clase.BUSINESS if var_clase.get() == "business" else Clase.TURISTA

        # Crear objetos
        maleta = Maleta(peso, largo, alto, ancho)
        pasajero = Pasajero(nombre, pasaporte, telefono, edad, maleta)

        asiento = avion.reservar_asiento(fila, butaca, clase, pasajero)

        if asiento:
            messagebox.showinfo("Éxito", f"Asiento reservado: {asiento}")
        else:
            messagebox.showwarning("Ocupado", "Ese asiento ya está ocupado.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Crear la ventana
root = tk.Tk()
root.title("Reserva de Asientos")

# Datos del pasajero
tk.Label(root, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Pasaporte:").grid(row=1, column=0)
entry_pasaporte = tk.Entry(root)
entry_pasaporte.grid(row=1, column=1)

tk.Label(root, text="Teléfono:").grid(row=2, column=0)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=2, column=1)

tk.Label(root, text="Edad:").grid(row=3, column=0)
entry_edad = tk.Entry(root)
entry_edad.grid(row=3, column=1)

# Maleta
tk.Label(root, text="Peso (kg):").grid(row=4, column=0)
entry_peso = tk.Entry(root)
entry_peso.grid(row=4, column=1)

tk.Label(root, text="Largo:").grid(row=5, column=0)
entry_largo = tk.Entry(root)
entry_largo.grid(row=5, column=1)

tk.Label(root, text="Ancho:").grid(row=6, column=0)
entry_ancho = tk.Entry(root)
entry_ancho.grid(row=6, column=1)

tk.Label(root, text="Alto:").grid(row=7, column=0)
entry_alto = tk.Entry(root)
entry_alto.grid(row=7, column=1)

# Asiento
tk.Label(root, text="Fila:").grid(row=8, column=0)
entry_fila = tk.Entry(root)
entry_fila.grid(row=8, column=1)

tk.Label(root, text="Butaca (1-4):").grid(row=9, column=0)
entry_butaca = tk.Entry(root)
entry_butaca.grid(row=9, column=1)

tk.Label(root, text="Clase:").grid(row=10, column=0)
var_clase = tk.StringVar(value="turista")
tk.Radiobutton(root, text="Turista", variable=var_clase, value="turista").grid(row=10, column=1)
tk.Radiobutton(root, text="Business", variable=var_clase, value="business").grid(row=10, column=2)

# Botón
tk.Button(root, text="Reservar asiento", command=reservar_asiento).grid(row=11, column=1, pady=10)

root.mainloop()