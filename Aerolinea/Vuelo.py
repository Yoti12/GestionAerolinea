# #1 public class Vuelo {
#     private String paisOrigen;
#     private String paisDestino;
#     private String fecha;
#     private Avion avion;
from Avion import Avion

class Vuelo:
    def __init__(self, paisOrigen, paisDestino, fecha, avion):
        self.paisOrigen = paisOrigen
        self.paisDestino = paisDestino
        self.fecha = fecha
        self.avion = avion

#     public Vuelo(String paisOrigen, String paisDestino, String fecha, Avion avion) {
#         this.paisOrigen = paisOrigen;
#         this.paisDestino = paisDestino;
#         this.fecha = fecha;
#         this.avion = avion;
#     }

#     public String getPaisOrigen() {
#         return this.paisOrigen;
#     }
    def getPaisOrigen (self):
        return self.paisOrigen
#     public String getPaisDestino() {
#         return this.paisDestino;
#     }
    def getPaisDestino (self):
        return self.paisDestino
#     public String getFecha() {
#         return this.fecha;
#     }
    def getFecha(self):
        return self.fecha
#     public Avion getAvion() {
#         return this.avion;
#     }
    def getAvion (self):
        return self.avion
# }