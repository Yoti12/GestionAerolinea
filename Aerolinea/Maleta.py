class Maleta: # public class Maleta {
    peso_maximo = 23
    # medida_total_maxima = 158

    def __init__(self, peso, ancho, alto, fondo):
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        self.fondo = fondo
        self.medida_total_maxima = 158

    def get_peso(self):
            return self.peso
    
    # def MedidaTotal(self):
    #      self.medida_total_maxima = 158
    #      return  self.medida_total_maxima
    
    def get_medida_total (self):
        return self.ancho + self.alto + self.fondo
    
    def exede_peso (self):
        if self.peso > self.peso_maximo:
            return True
        else:
            return False
        
    def exede_medidad (self):
        if self.get_medida_total() > self.medida_total_maxima:
            return True
        else:
             return False

#     public boolean excedeDePeso() {
#         if (this.peso > this.PESO_MAXIMO){
#             return true;
#         }
#         return false;
#     }

#     public boolean excedeDeMedidas() {
#         if (this.getMedidaTotal() > this.MEDIDA_TOTAL_MAXIMA){
#             return true;
#         }
#         return false;
#     }
# }