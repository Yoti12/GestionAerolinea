from Maleta import Maleta  # Se importa la clase Maleta desde el archivo Maleta.py para poder utilizarla.

class Pasajero:  # Se define la clase Pasajero que representa a una persona co su maleta.
    def __init__(self, nombre, pasaporte, telefono, edad, maleta):  # Constructor que inicializa los atributos del pasajero.
        self.nombre = nombre  # Asigna el nombre del pasajero.
        self.pasaporte = pasaporte  # Asigna el número de pasaporte del pasajero.
        self.telefono = telefono  # Asigna el número de teléfono del pasajero.
        self.edad = edad  # Asigna la edad del pasajero.
        self.maleta = maleta  # Asigna el objeto maleta al pasajero.
    
    def getNombre(self):  # Método para obtener el nombre del pasajero.
        return self.nombre  # Retorna el nombre.

    def getPasaporte(self):  # Método para obtener el pasaporte del pasajero.
        return self.pasaporte  # Retorna el pasaporte.

    def getTelefono(self):  # Método para obtener el teléfono del pasajero.
        return self.telefono  # Retorna el teléfono.

    def getEdad(self):  # Método para obtener la edad del pasajero.
        return self.edad  # Retorna la edad.

    def get_maleta(self):  # Método para obtener el objeto maleta asociado al pasajero.
        return self.maleta  # Retorna la maleta.

    def __str__(self):  # Método especial que devuelve una representación en string del objeto Pasajero.
        return (
            f"Nombre: {self.nombre}, Pasaporte: {self.pasaporte}, Teléfono: {self.telefono}, "
            f"Edad: {self.edad}, Maleta: {self.maleta}"  # Devuelve un string con toda la información del pasajero y su maleta.
        )
