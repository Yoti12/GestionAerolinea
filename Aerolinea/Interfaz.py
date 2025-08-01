import tkinter as tk
from tkinter import messagebox
from Reserva import reservar_asiento
from Clase import Clase

class InterfazReserva:
    def __init__(self, root, avion):
        self.root = root
        self.avion = avion
        self.root.title("Sistema de Aerolínea")

        self.frame_menu = tk.Frame(root, width=220, bg="#05194C")
        self.frame_menu.pack(side=tk.LEFT, fill=tk.Y)

        self.frame_contenido = tk.Frame(root, bg="#F2F2F2")
        self.frame_contenido.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        botones = [
            ("Reservar Asiento", self.mostrar_formulario_reserva),
            ("Ver Mapa de Asientos", self.mostrar_mapa_asientos),
            ("Listar Pasajeros", self.mostrar_pasajeros),
            ("Pasajeros Menores", self.mostrar_menores),
            ("Calcular Ingresos", self.mostrar_ingresos),
        ]

        for texto, comando in botones:
            tk.Button(self.frame_menu, text=texto, width=20, command=comando,
                      bg="#C60C30", fg="white", activebackground="#A50A26", bd=0,
                      font=("Helvetica", 10, "bold")).pack(pady=10)

        self.campos = {}

    def limpiar_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def mostrar_formulario_reserva(self):
        self.limpiar_contenido()

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
        for i, (label_texto, campo) in enumerate(campos):
            tk.Label(self.frame_contenido, text=label_texto, bg="#F2F2F2", font=("Arial", 10)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entrada = tk.Entry(self.frame_contenido)
            entrada.grid(row=i, column=1, padx=10, pady=5)
            self.campos[campo] = entrada

        tk.Label(self.frame_contenido, text="Clase", bg="#F2F2F2", font=("Arial", 10)).grid(row=len(campos), column=0, padx=10, pady=5, sticky="e")
        opcion_clase = tk.StringVar()
        opcion_clase.set("turista")
        tk.OptionMenu(self.frame_contenido, opcion_clase, "turista", "business").grid(row=len(campos), column=1, padx=10, pady=5)
        self.campos["clase"] = opcion_clase

        tk.Button(self.frame_contenido, text="Reservar", bg="#C60C30", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: self.reservar()).grid(row=len(campos)+1, column=0, columnspan=2, pady=15)

    def reservar(self):
        entradas = {k: v.get() if not isinstance(v, tk.StringVar) else v.get() for k, v in self.campos.items()}
        reservar_asiento(self.avion, entradas)

    def mostrar_mapa_asientos(self):
        self.limpiar_contenido()
        mapa = self.avion.obtener_mapa_asientos()
        tk.Label(self.frame_contenido, text=mapa, font=("Courier", 10), bg="#F2F2F2", justify="left").pack(padx=10, pady=10)

    def mostrar_pasajeros(self):
        self.limpiar_contenido()
        pasajeros = self.avion.listar_pasajeros_por_clase()
        texto = "\n".join(str(p) for p in pasajeros) if pasajeros else "No hay pasajeros registrados."
        tk.Label(self.frame_contenido, text=texto, bg="#F2F2F2", justify="left", anchor="nw", font=("Arial", 10)).pack(padx=10, pady=10, fill="both", expand=True)

    def mostrar_menores(self):
        self.limpiar_contenido()
        menores = self.avion.listar_menores_de_edad()
        texto = "\n".join(str(p) for p in menores) if menores else "No hay pasajeros menores de edad."
        tk.Label(self.frame_contenido, text=texto, bg="#F2F2F2", justify="left", anchor="nw", font=("Arial", 10)).pack(padx=10, pady=10, fill="both", expand=True)

    def mostrar_ingresos(self):
        self.limpiar_contenido()
        total = self.avion.calcular_ingresos_por_vuelo()
        tk.Label(self.frame_contenido, text=f"Ingresos Totales: ${total}", font=("Arial", 12, "bold"),
                 bg="#F2F2F2", fg="#05194C").pack(pady=20)
