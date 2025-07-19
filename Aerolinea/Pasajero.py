from Maleta import Maleta
from Azar import Azar
class Pasajero: 
    # public class Pasajero {
    def __init__(self, nombre, pasaporte, telefono, edad, maleta):
        self.nombre = nombre
        self.pasaporte = pasaporte
        self.telefono = telefono
        self.edad = edad
        self.maleta = maleta
    
    def getNombre(self):
        return self.nombre
    
    def getPasaporte(self):
        return self.pasaporte
    
    def getTelefono(self):
        return self.telefono
    
    def getEdad(self):
        return self.edad
    
    def get_maleta(self):
        return self.maleta
#. 	private String nombre;
# 	private String pasaporte;
# 	private String telefono;
# 	private int edad;
# 	private Maleta maleta;
# 	public Pasajero(String nombre, String pasaporte, String telefono, int edad, Maleta maleta) {
# 		this.nombre = nombre;
# 		this.pasaporte = pasaporte;
# 		this.telefono = telefono;
# 		this.edad = edad;
# 		this.maleta = maleta;
# 	}

# 	public String getNombre() {
# 		return nombre;
# 	}

# 	public String getPasaporte() {
# 		return pasaporte;
# 	}

# 	public String getTelefono() {
# 		return telefono;
# 	}

# 	public int getEdad() {
# 		return edad;
# 	}

# 	public Maleta getMaleta() {
# 		return maleta;
# 	}
# }