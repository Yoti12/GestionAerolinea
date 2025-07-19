from Asiento import Asiento
from Clase import Clase

class Avion:
    ASIENTOS_X_FILA = 4

    def __init__(self, modelo, business, turista):
        self.modelo = modelo
        self.numero_asientos_business = business
        self.numero_asientos_turista = turista

        self.asiento_business = [
            [None for _ in range(self.ASIENTOS_X_FILA)]
            for _ in range(business // self.ASIENTOS_X_FILA)
        ]
        self.asiento_turista = [
            [None for _ in range(self.ASIENTOS_X_FILA)]
            for _ in range(turista // self.ASIENTOS_X_FILA)
        ]

    def get_modelo(self):
        return self.modelo

    def get_numero_filas(self, clase):
        if clase == Clase.BUSINESS:
            return self.numero_asientos_business // self.ASIENTOS_X_FILA
        else:
            return self.numero_asientos_turista // self.ASIENTOS_X_FILA

    def get_butacas_por_fila(self):
        return self.ASIENTOS_X_FILA

    def get_pasajero(self, fila, butaca, clase):
        asiento = None
        if clase == Clase.BUSINESS:
            asiento = self.asiento_business[fila - 1][butaca - 1]
        else:
            asiento = self.asiento_turista[fila - 1][butaca - 1]

        if asiento is not None:
            return asiento.pasajero
        return None

    def reservar_asiento(self, fila, butaca, clase, pasajero):
        asiento_asignado = None
        if clase == Clase.BUSINESS:
            if self.asiento_business[fila - 1][butaca - 1] is None:
                asiento_asignado = Asiento(fila, butaca, pasajero)
                self.asiento_business[fila - 1][butaca - 1] = asiento_asignado
        else:
            if self.asiento_turista[fila - 1][butaca - 1] is None:
                asiento_asignado = Asiento(fila, butaca, pasajero)
                self.asiento_turista[fila - 1][butaca - 1] = asiento_asignado
        return asiento_asignado

    def mostrar_mapa_de_asientos(self):
        print(f"\nAvión {self.modelo}")
        for butaca in range(self.ASIENTOS_X_FILA):
            for fila in range(len(self.asiento_business)):
                print("B" if self.asiento_business[fila][butaca] is not None else "·", end="")
            print(" ", end="")
            for fila in range(len(self.asiento_turista)):
                print("T" if self.asiento_turista[fila][butaca] is not None else "·", end="")
            print()
