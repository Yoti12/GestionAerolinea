from Avion import Avion  # Se importa la clase Avion desde el archivo Avion.py para ser utilizada en esta clase.

class Vuelo:  # Se define la clase Vuelo que representa un vuelo con origen, destino, fecha y un avión asignado.
    def __init__(self, paisOrigen, paisDestino, fecha, avion):  # Constructor que inicializa los atributos del vuelo.
        self.paisOrigen = paisOrigen  # Asigna el país de origen del vuelo.
        self.paisDestino = paisDestino  # Asigna el país de destino del vuelo.
        self.fecha = fecha  # Asigna la fecha del vuelo.
        self.avion = avion  # Asigna el objeto Avion al vuelo.
        
    def getPaisOrigen(self):  # Método para obtener el país de origen del vuelo.
        return self.paisOrigen  # Retorna el país de origen.

    def getPaisDestino(self):  # Método para obtener el país de destino del vuelo.
        return self.paisDestino  # Retorna el país de destino.

    def getFecha(self):  # Método para obtener la fecha del vuelo.
        return self.fecha  # Retorna la fecha.

    def getAvion(self):  # Método para obtener el avión asignado al vuelo.
        return self.avion  # Retorna el objeto Avion.