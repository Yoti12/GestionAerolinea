import tkinter as tk
from tkinter import messagebox
from Reserva import reservar_asiento
from Clase import Clase
from Reporte import generar_reporte_pasajeros

class InterfazReserva:
    def __init__(self, root, avion):
        # Inicialización de la interfaz con la ventana raíz y el avión
        self.root = root
        self.avion = avion
        self.root.title("Sistema de Aerolínea")

        # Definición de estilos unificados para toda la interfaz
        self.fuente_contenido = ("Arial", 12, "bold")
        self.color_texto = "#05194C"
        self.bg_contenido = "#F2F2F2"

        # Creación del menú lateral izquierdo
        self.frame_menu = tk.Frame(root, width=220, bg="#05194C")
        self.frame_menu.pack(side=tk.LEFT, fill=tk.Y)

        # Área de contenido principal donde se mostrarán formularios y reportes
        self.frame_contenido = tk.Frame(root, bg=self.bg_contenido)
        self.frame_contenido.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Botones del menú lateral con sus respectivas funciones
        botones = [
            ("Reservar Asiento", self.mostrar_formulario_reserva),
            ("Ver Mapa de Asientos", self.mostrar_mapa_asientos),
            ("Listar Pasajeros", self.mostrar_pasajeros),
            ("Pasajeros Menores", self.mostrar_menores),
            ("Calcular Ingresos", self.mostrar_ingresos),
            ("Exportar PDF", self.exportar_pdf),
        ]

        # Creación de los botones en el frame del menú lateral
        for texto, comando in botones:
            tk.Button(self.frame_menu, text=texto, width=20, command=comando,
                      bg="#C60C30", fg="white", activebackground="#A50A26", bd=0,
                      font=("Helvetica", 10, "bold")).pack(pady=10)

        # Diccionario para almacenar referencias a los campos de entrada
        self.campos = {}

    def limpiar_contenido(self):
        # Limpia todos los widgets del frame de contenido antes de mostrar uno nuevo
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def mostrar_formulario_reserva(self):
        # Muestra el formulario para reservar un asiento
        self.limpiar_contenido()

        # Campos del formulario y sus claves para acceder a ellos
        campos = [
            ("Nombre", "nombre"),
            ("Pasaporte", "pasaporte"),
            ("Teléfono", "telefono"),
            ("Edad", "edad"),
            ("Peso (kg)", "peso"),
            ("Largo", "largo"),
            ("Ancho", "ancho"),
            ("Alto", "alto"),
            ("Fila", "fila"),
            ("Butaca", "butaca"),
        ]

        self.campos = {}
        # Creación de etiquetas y entradas para cada campo
        for i, (label_texto, campo) in enumerate(campos):
            tk.Label(self.frame_contenido, text=label_texto,
                     bg=self.bg_contenido, fg=self.color_texto,
                     font=self.fuente_contenido).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entrada = tk.Entry(self.frame_contenido, font=self.fuente_contenido)
            entrada.grid(row=i, column=1, padx=10, pady=5)
            self.campos[campo] = entrada

        # Opción para seleccionar la clase del pasajero (turista o business)
        tk.Label(self.frame_contenido, text="Clase",
                 bg=self.bg_contenido, fg=self.color_texto,
                 font=self.fuente_contenido).grid(row=len(campos), column=0, padx=10, pady=5, sticky="e")
        opcion_clase = tk.StringVar()
        opcion_clase.set("turista")
        tk.OptionMenu(self.frame_contenido, opcion_clase, "turista", "business")\
            .config(font=self.fuente_contenido)
        tk.OptionMenu(self.frame_contenido, opcion_clase, "turista", "business")\
            .grid(row=len(campos), column=1, padx=10, pady=5)
        self.campos["clase"] = opcion_clase

        # Botón para ejecutar la reserva con los datos ingresados
        tk.Button(self.frame_contenido, text="Reservar",
                  bg="#C60C30", fg="white", font=self.fuente_contenido,
                  command=lambda: self.reservar()).grid(
            row=len(campos)+1, column=0, columnspan=2, pady=15)

    def reservar(self):
        # Recopila los datos de los campos y llama a la función reservar_asiento
        entradas = {
            k: (v.get() if not isinstance(v, tk.StringVar) else v.get())
            for k, v in self.campos.items()
        }
        reservar_asiento(self.avion, entradas)

    def mostrar_mapa_asientos(self):
        # Muestra el mapa de asientos del avión
        self.limpiar_contenido()
        mapa = self.avion.obtener_mapa_asientos()
        tk.Label(self.frame_contenido, text=mapa,
                 font=self.fuente_contenido, bg=self.bg_contenido,
                 fg=self.color_texto, justify="left", anchor="nw")\
            .pack(padx=10, pady=10, fill="both", expand=True)

    def mostrar_pasajeros(self):
        # Lista todos los pasajeros por clase
        self.limpiar_contenido()
        pasajeros = self.avion.listar_pasajeros_por_clase()
        texto = pasajeros if pasajeros else "No hay pasajeros registrados."
        tk.Label(self.frame_contenido, text=texto,
                 font=self.fuente_contenido, bg=self.bg_contenido,
                 fg=self.color_texto, justify="left", anchor="nw")\
            .pack(padx=10, pady=10, fill="both", expand=True)

    def mostrar_menores(self):
        # Lista los pasajeros menores de edad
        self.limpiar_contenido()
        menores = self.avion.listar_menores_de_edad()
        texto = menores if menores else "No hay pasajeros menores de edad."
        tk.Label(self.frame_contenido, text=texto,
                 font=self.fuente_contenido, bg=self.bg_contenido,
                 fg=self.color_texto, justify="left", anchor="nw")\
            .pack(padx=10, pady=10, fill="both", expand=True)

    def mostrar_ingresos(self):
        # Muestra el total de ingresos por vuelo
        self.limpiar_contenido()
        total = self.avion.calcular_ingresos_por_vuelo()
        tk.Label(self.frame_contenido, text=total,
                 font=self.fuente_contenido, bg=self.bg_contenido,
                 fg=self.color_texto, justify="left", anchor="nw")\
            .pack(pady=20, padx=10)
    
    def exportar_pdf(self):
        # Genera un reporte PDF de todos los pasajeros
        try:
            pasajeros = []
            # Recorre los asientos de clase Business
            for fila in self.avion.asiento_business:
                for asiento in fila:
                    if asiento:
                        pasajeros.append((asiento.pasajero.nombre, "Business", f"{asiento.fila}-{asiento.butaca}"))
            # Recorre los asientos de clase Turista
            for fila in self.avion.asiento_turista:
                for asiento in fila:
                    if asiento:
                        pasajeros.append((asiento.pasajero.nombre, "Turista", f"{asiento.fila}-{asiento.butaca}"))

            if not pasajeros:
                # Mensaje si no hay pasajeros
                messagebox.showinfo("Exportar PDF", "No hay pasajeros registrados para exportar.")
                return

            # Llamada a la función que genera el PDF
            generar_reporte_pasajeros(pasajeros, "reporte_pasajeros.pdf")
            messagebox.showinfo("Exportar PDF", "Reporte PDF generado correctamente.")

        except Exception as e:
            # Captura cualquier error durante la generación del PDF
            messagebox.showerror("Error", f"No se pudo generar el PDF: {e}")
