from tkinter import messagebox  # Para mostrar mensajes emergentes
from Pasajero import Pasajero  # Clase Pasajero
from Maleta import Maleta      # Clase Maleta
from Clase import Clase        # Enum de clase BUSINESS/TURISTA

def reservar_asiento(avion, entradas):
    # Obtener datos del formulario
    nombre = entradas['nombre']
    pasaporte = entradas['pasaporte']
    telefono = entradas['telefono']
    edad = int(entradas['edad'])
    peso = float(entradas['peso'])
    largo = float(entradas['largo'])
    ancho = float(entradas['ancho'])
    alto = float(entradas['alto'])
    fila = int(entradas['fila'])
    butaca = int(entradas['butaca'])
    clase = Clase.BUSINESS if entradas['clase'] == "business" else Clase.TURISTA

    # Verificar duplicados en todos los asientos (Business y Turista)
    for fila_asientos in avion.asiento_business + avion.asiento_turista:
        for asiento in fila_asientos:
            if asiento:
                p = asiento.pasajero
                if p.nombre == nombre:
                    messagebox.showerror("Error", f"Ya existe un pasajero con el nombre: {nombre}")
                    return
                if p.pasaporte == pasaporte:
                    messagebox.showerror("Error", f"Ya existe un pasajero con el pasaporte: {pasaporte}")
                    return

    # Crear objeto Maleta y Pasajero
    maleta = Maleta(peso, largo, alto, ancho)
    pasajero = Pasajero(nombre, pasaporte, telefono, edad, maleta)

    # Intentar reservar asiento
    asiento = avion.reservar_asiento(fila, butaca, clase, pasajero)

    # Mostrar resultado al usuario
    if asiento:
        messagebox.showinfo("Éxito", f"Asiento reservado: {asiento}")
    else:
        messagebox.showwarning("Ocupado", "Ese asiento ya está ocupado.")
