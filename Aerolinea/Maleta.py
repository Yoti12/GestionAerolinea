class Maleta:  # Se define la clase Maleta para representar una maleta con peso y dimensiones.
    peso_maximo = 23  # Atributo de clase que indica el peso máximo permitido para una maleta (en kg).

    def __init__(self, peso, ancho, alto, fondo):  # Constructor que inicializa los atributos de una maleta.
        self.peso = peso  # Asigna el peso de la maleta.
        self.ancho = ancho  # Asigna el ancho de la maleta.
        self.alto = alto  # Asigna el alto de la maleta.
        self.fondo = fondo  # Asigna el fondo de la maleta.
        self.medida_total_maxima = 158  # Define la suma máxima permitida de las tres dimensiones (en cm).

    def get_peso(self):  # Método para obtener el peso de la maleta.
            return self.peso  # Retorna el peso actual de la maleta.
    
    def get_medida_total(self):  # Método que calcula la medida total sumando ancho, alto y fondo.
        return self.ancho + self.alto + self.fondo  # Retorna la suma de las tres dimensiones.

    def exede_peso(self):  # Método que verifica si la maleta excede el peso permitido.
        if self.peso > self.peso_maximo:  # Compara el peso actual con el peso máximo permitido.
            return True  # Retorna True si excede el peso.
        else:               #Si NO se cumple.
            return False  # Retorna False si no lo excede.
        
    def exede_medidad(self):  # Método que verifica si la maleta excede la medida total permitida.
        if self.get_medida_total() > self.medida_total_maxima:  # Compara la medida total actual con la máxima permitida.
            return True  # Retorna True si excede la medida.
        else:
             return False  # Retorna False si no lo excede.
        
    def __str__(self):  # Método especial para representar la maleta como una cadena de texto.
        return (
            f"Peso: {self.peso}kg, Dimensiones: {self.ancho}x{self.alto}x{self.fondo}cm, "
            f"Total: {self.get_medida_total()}cm"  # Devuelve una descripción completa del peso y dimensiones de la maleta.
        )



