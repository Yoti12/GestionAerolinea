from Asiento import Asiento  # Se importa la clase Asiento desde el archivo Asiento.py.
from Clase import Clase  # Se importa la clase Clase desde el archivo Clase.py.

class Avion:  # Se define la clase Avion, que representa un avión con asientos distribuidos por clase.
    ASIENTOS_X_FILA = 4  # Constante que indica cuántas butacas hay por fila.
    PRECIO_BUSINESS = 300  # Precio del boleto en clase Business.
    PRECIO_TURISTA = 150  # Precio del boleto en clase Turista.

    def __init__(self, modelo, business, turista):  # Constructor que inicializa el modelo y la distribución de asientos.
        self.modelo = modelo  # Se asigna el modelo del avión.
        self.numero_asientos_business = business  # Total de asientos en clase Business.
        self.numero_asientos_turista = turista  # Total de asientos en clase Turista.

        # Se inicializa la matriz de asientos para clase Business, con 'None' en cada asiento.
        self.asiento_business = [
            [None for _ in range(self.ASIENTOS_X_FILA)]
            for _ in range(business // self.ASIENTOS_X_FILA)
        ]
        # Se inicializa la matriz de asientos para clase Turista, con 'None' en cada asiento.
        self.asiento_turista = [
            [None for _ in range(self.ASIENTOS_X_FILA)]
            for _ in range(turista // self.ASIENTOS_X_FILA)
        ]

    def get_modelo(self):  # Método para obtener el modelo del avión.
        return self.modelo

    def get_numero_filas(self, clase):  # Método para obtener el número de filas según la clase.
        if clase == Clase.BUSINESS:
            return self.numero_asientos_business // self.ASIENTOS_X_FILA
        else:
            return self.numero_asientos_turista // self.ASIENTOS_X_FILA

    def get_butacas_por_fila(self):  # Método para obtener la cantidad de butacas por fila.
        return self.ASIENTOS_X_FILA

    def get_pasajero(self, fila, butaca, clase):  # Método para obtener al pasajero en una posición específica.
        if clase == Clase.BUSINESS:
            asiento = self.asiento_business[fila - 1][butaca - 1]
        else:
            asiento = self.asiento_turista[fila - 1][butaca - 1]
        return asiento.pasajero if asiento else None  # Se retorna el pasajero si existe en ese asiento.

    def reservar_asiento(self, fila, butaca, clase, pasajero):  # Método para reservar un asiento.
        if clase == Clase.BUSINESS:
            if self.asiento_business[fila - 1][butaca - 1] is None:  # Verifica que el asiento esté disponible.
                self.asiento_business[fila - 1][butaca - 1] = Asiento(fila, butaca, pasajero)  # Reserva el asiento.
                return self.asiento_business[fila - 1][butaca - 1]
        else:
            if self.asiento_turista[fila - 1][butaca - 1] is None:  # Verifica que el asiento esté disponible.
                self.asiento_turista[fila - 1][butaca - 1] = Asiento(fila, butaca, pasajero)  # Reserva el asiento.
                return self.asiento_turista[fila - 1][butaca - 1]
        return None  # Retorna None si el asiento ya estaba ocupado.

    def obtener_mapa_asientos(self):  # Método para obtener una representación del mapa de asientos del avión.
        mapa = f"\nAvión {self.modelo}\n"
        mapa += "FILA\tBusiness\t\tTurista\n"
        num_filas = max(len(self.asiento_business), len(self.asiento_turista))  # Se calcula el máximo número de filas.

        for fila in range(num_filas):
            fila_str = f"{fila + 1}\t"

            # Se representa cada asiento de Business con "B" si está ocupado o "·" si está vacío.
            if fila < len(self.asiento_business):
                fila_str += "".join("B" if asiento else "·" for asiento in self.asiento_business[fila])
            else:
                fila_str += " " * self.ASIENTOS_X_FILA

            fila_str += "\t\t"

            # Se representa cada asiento de Turista con "T" si está ocupado o "·" si está vacío.
            if fila < len(self.asiento_turista):
                fila_str += "".join("T" if asiento else "·" for asiento in self.asiento_turista[fila])
            else:
                fila_str += " " * self.ASIENTOS_X_FILA

            mapa += fila_str + "\n"  # Se añade la línea de la fila al mapa.

        return mapa  # Retorna el mapa como string.

    def listar_pasajeros_por_clase(self):  # Método para listar todos los pasajeros por clase.
        resultado = "\n--- Clase Business ---\n"
        for fila in self.asiento_business:
            for asiento in fila:
                if asiento:
                    resultado += str(asiento.pasajero) + "\n"  # Añade la representación del pasajero.

        resultado += "\n--- Clase Turista ---\n"
        for fila in self.asiento_turista:
            for asiento in fila:
                if asiento:
                    resultado += str(asiento.pasajero) + "\n"  # Añade la representación del pasajero.

        return resultado  # Retorna la lista completa.

    def listar_menores_de_edad(self):  # Método para listar los pasajeros menores de 15 años.
        resultado = "\n--- Pasajeros menores de 15 años ---\n"
        for fila in self.asiento_business:
            for asiento in fila:
                if asiento and asiento.pasajero.edad < 15:
                    resultado += str(asiento.pasajero) + "\n"  # Añade el pasajero si cumple la condición.
        for fila in self.asiento_turista:
            for asiento in fila:
                if asiento and asiento.pasajero.edad < 15:
                    resultado += str(asiento.pasajero) + "\n"

        return resultado  # Retorna la lista de menores.

    def calcular_ingresos_por_vuelo(self):  # Método para calcular los ingresos totales del vuelo.
        total_business = sum(
            1 for fila in self.asiento_business for asiento in fila if asiento  # Cuenta cuántos asientos ocupados hay en Business.
        ) * self.PRECIO_BUSINESS  # Multiplica por el precio de Business.

        total_turista = sum(
            1 for fila in self.asiento_turista for asiento in fila if asiento  # Cuenta cuántos asientos ocupados hay en Turista.
        ) * self.PRECIO_TURISTA  # Multiplica por el precio de Turista.

        total = total_business + total_turista  # Suma los ingresos de ambas clases.

        return (
            f"\n--- Ingresos por Vuelo ---\n"
            f"Ingreso Clase Business: ${total_business}\n"
            f"Ingreso Clase Turista:  ${total_turista}\n"
            f"Ingreso Total:          ${total}\n"  # Devuelve el informe de ingresos como string.
        )