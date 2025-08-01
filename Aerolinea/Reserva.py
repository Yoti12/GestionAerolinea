from tkinter import messagebox  # Se importa el módulo messagebox de tkinter para mostrar mensajes emergentes al usuario.
from Pasajero import Pasajero  # Se importa la clase Pasajero desde el archivo Pasajero.py.
from Maleta import Maleta  # Se importa la clase Maleta desde el archivo Maleta.py.
from Clase import Clase  # Se importa la clase 'Clase' desde el archivo Clase.py, donde se define el tipo de clase B/T.

def reservar_asiento(avion, entradas):  # Se define la función reservar_asiento que toma como parámetros avión y un diccionario.
    nombre = entradas['nombre']  # Se obtiene el valor del nombre desde el diccionario de entradas.
    pasaporte = entradas['pasaporte']  # Se obtiene el número de pasaporte desde las entradas.
    telefono = entradas['telefono']  # Se obtiene el teléfono desde las entradas.
    edad = int(entradas['edad'])  # Se convierte y obtiene la edad del pasajero desde las entradas.
    peso = float(entradas['peso'])  # Se convierte y obtiene el peso de la maleta desde las entradas.
    largo = float(entradas['largo'])  # Se convierte y obtiene el largo de la maleta desde las entradas.
    ancho = float(entradas['ancho'])  # Se convierte y obtiene el ancho de la maleta desde las entradas.
    alto = float(entradas['alto'])  # Se convierte y obtiene el alto de la maleta desde las entradas.
    fila = int(entradas['fila'])  # Se convierte y obtiene la fila del asiento desde las entradas.
    butaca = int(entradas['butaca'])  # Se convierte y obtiene la butaca del asiento desde las entradas.
    clase = Clase.BUSINESS if entradas['clase'] == "business" else Clase.TURISTA  
    # Se determina la clase del asiento (BUSINESS o TURISTA) según el valor en las entradas.
    # Recorremos todos los asientos para verificar duplicados
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



    maleta = Maleta(peso, largo, alto, ancho)  # Se crea un objeto Maleta con los datos ingresados.
    pasajero = Pasajero(nombre, pasaporte, telefono, edad, maleta)  # Se crea un objeto Pasajero con sus datos personales y su maleta.


    asiento = avion.reservar_asiento(fila, butaca, clase, pasajero)  
    # Se intenta reservar un asiento en el avión con la fila, butaca, clase y pasajero especificados.

    if asiento:  # Si el asiento fue reservado exitosamente...
        messagebox.showinfo("Éxito", f"Asiento reservado: {asiento}")  # Se muestra un mensaje de éxito con la información del asiento.
    else:  # Si el asiento ya estaba ocupado...
        messagebox.showwarning("Ocupado", "Ese asiento ya está ocupado.")  # Se muestra una advertencia al usuario indicando que no se pudo reservar.
