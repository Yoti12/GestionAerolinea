class Asiento:  # Se define la clase Asiento que representará un asiento en una
    #fila con su respectiva butaca y pasajero.
    def __init__(self, fila, butaca, pasajero):  # Constructor que inicializa un objeto Asiento con fila, butaca y pasajero.
        self.fila = fila  # Se asigna el valor de la fila al atributo 'fila' del objeto.
        self.butaca = butaca  # Se asigna el valor de la butaca al atributo 'butaca' del objeto.
        self.pasajero = pasajero  # Se asigna el valor del pasajero al atributo 'pasajero' del objeto.
        
    def __str__(self):  # Método define la representación en cadena del objeto Asiento.
        letra_butaca = {0: "A", 1: "B", 2: "C", 3: "D"}.get(self.butaca, "")  # Se obtiene la letra correspondiente a la butaca usando un diccionario.
        return f"{self.fila}{letra_butaca}"  # Se devuelve una cadena compuesta por la fila y la letra de la butaca.
