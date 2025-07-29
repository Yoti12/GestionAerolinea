import tkinter as tk  # Se importa el módulo tkinter para crear interfaces gráficas.
from tkinter import messagebox  # Se importa messagebox para mostrar cuadros de diálogo.
from Reserva import reservar_asiento  # Se importa la función reservar_asiento desde el módulo Reserva.

class InterfazReserva:  # Se define la clase InterfazReserva que gestiona la interfaz de reservas.
    def __init__(self, root, avion):  # Constructor que recibe la ventana principal y un objeto Avion.
        self.root = root  # Se guarda la ventana raíz.
        self.avion = avion  # Se guarda el objeto avión.
        self.root.title("Reserva de Asientos")  # Se establece el título de la ventana.

        self.campos = {}  # Diccionario para almacenar las entradas del formulario.

        labels = [  # Lista con las etiquetas de los campos del formulario.
            "Nombre", "Pasaporte", "Teléfono", "Edad",
            "Peso (kg)", "Largo", "Ancho", "Alto",
            "Fila", "Butaca (1-4)"
        ]

        # Se crean etiquetas y campos de texto para cada campo del formulario.
        for i, label in enumerate(labels):
            tk.Label(root, text=label + ":").grid(row=i, column=0)  # Crea la etiqueta y la ubica.
            entry = tk.Entry(root)  # Crea un campo de entrada.
            entry.grid(row=i, column=1)  # Ubica el campo en la cuadrícula.
            self.campos[label.lower().split()[0]] = entry  # Guarda el campo en el diccionario (clave en minúscula).

        tk.Label(root, text="Clase:").grid(row=10, column=0)  # Etiqueta para la selección de clase.
        self.clase_var = tk.StringVar(value="turista")  # Variable para guardar la clase seleccionada (por defecto: turista).
        tk.Radiobutton(root, text="Turista", variable=self.clase_var, value="turista").grid(row=10, column=1)  # Botón para clase turista.
        tk.Radiobutton(root, text="Business", variable=self.clase_var, value="business").grid(row=10, column=2)  # Botón para clase business.

        # Botones de acciones con sus respectivos comandos.
        tk.Button(root, text="Reservar asiento", command=self.on_reservar).grid(row=11, column=1, pady=10)
        tk.Button(root, text="Ver Mapa de Asientos", command=self.mostrar_mapa_asientos).grid(row=12, column=1, pady=5)
        tk.Button(root, text="Listar Pasajeros", command=self.mostrar_pasajeros).grid(row=13, column=1, pady=5)
        tk.Button(root, text="Pasajeros Menores de Edad", command=self.mostrar_menores).grid(row=14, column=1, pady=5)
        tk.Button(root, text="Calcular Ingresos", command=self.mostrar_ingresos).grid(row=15, column=1, pady=5)

    def on_reservar(self):  # Método que se ejecuta cuando se presiona el botón "Reservar asiento".
        datos = {  # Se recogen todos los datos desde los campos del formulario.
            "nombre": self.campos["nombre"].get(),
            "pasaporte": self.campos["pasaporte"].get(),
            "telefono": self.campos["teléfono"].get(),
            "edad": self.campos["edad"].get(),
            "peso": self.campos["peso"].get(),
            "largo": self.campos["largo"].get(),
            "ancho": self.campos["ancho"].get(),
            "alto": self.campos["alto"].get(),
            "fila": self.campos["fila"].get(),
            "butaca": self.campos["butaca"].get(),
            "clase": self.clase_var.get()
        }

        reservar_asiento(self.avion, datos)  # Se llama a la función para intentar reservar el asiento.

    def mostrar_mapa_asientos(self):  # Método que muestra el mapa de asientos del avión.
        mapa = self.avion.obtener_mapa_asientos()  # Obtiene el mapa de asientos.

        ventana = tk.Toplevel(self.root)  # Crea una nueva ventana secundaria.
        ventana.title("Mapa de Asientos")  # Título de la ventana.

        text_widget = tk.Text(ventana, width=60, height=20)  # Se crea un widget de texto para mostrar el mapa.
        text_widget.insert(tk.END, mapa)  # Se inserta el contenido del mapa.
        text_widget.config(state=tk.DISABLED)  # Se desactiva la edición del texto.
        text_widget.pack(padx=10, pady=10)  # Se muestra el widget con padding.

    def mostrar_pasajeros(self):  # Método que muestra la lista de todos los pasajeros por clase.
        lista = self.avion.listar_pasajeros_por_clase()  # Se obtiene la lista desde el avión.

        ventana = tk.Toplevel(self.root)  # Nueva ventana para mostrar la lista.
        ventana.title("Pasajeros por Vuelo")

        texto = tk.Text(ventana, width=60, height=20)
        texto.insert(tk.END, lista)
        texto.config(state=tk.DISABLED)
        texto.pack(padx=10, pady=10)

    def mostrar_menores(self):  # Método que muestra los pasajeros menores de 15 años.
        menores = self.avion.listar_menores_de_edad()  # Se obtiene la lista de menores.

        ventana = tk.Toplevel(self.root)
        ventana.title("Pasajeros Menores de Edad")

        texto = tk.Text(ventana, width=60, height=20)
        texto.insert(tk.END, menores)
        texto.config(state=tk.DISABLED)
        texto.pack(padx=10, pady=10)

    def mostrar_ingresos(self):  # Método que muestra los ingresos del vuelo.
        mensaje = self.avion.calcular_ingresos_por_vuelo()  # Se calcula el ingreso total.
        messagebox.showinfo("Ingresos", mensaje)  # Se muestra el resultado en un cuadro de diálogo.
