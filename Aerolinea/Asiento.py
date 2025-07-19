class Asiento:
    def __init__(self, fila, butaca, pasajero):
        self.fila = fila 
        self.butaca = butaca
        self.pasajero = pasajero
        
    def __str__(self):
        letra_butaca = {0: "A", 1: "B", 2: "C", 3: "D"}.get(self.butaca, "")
        return f"{self.fila}{letra_butaca}"