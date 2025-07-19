from Maleta import Maleta
from Pasajero import Pasajero
from Avion import Avion
from Clase import Clase

def main():
    # Crear una maleta
    maleta1 = Maleta(20, 50, 50, 50)
    print("Maleta creada:")
    print("Peso:", maleta1.get_peso())
    print("Medida total:", maleta1.get_medida_total())
    print("¿Excede peso?", maleta1.exede_peso())
    print("¿Excede medidas?", maleta1.exede_medidad())
    print()

    # Crear un pasajero con esa maleta
    pasajero1 = Pasajero("Juan Pérez", "A1234567", "+59312345678", 30, maleta1)
    print("Pasajero creado:")
    print("Nombre:", pasajero1.getNombre())
    print("Pasaporte:", pasajero1.getPasaporte())
    print("Teléfono:", pasajero1.getTelefono())
    print("Edad:", pasajero1.getEdad())
    print("Peso de su maleta:", pasajero1.get_maleta().get_peso())
    print()

    # Crear un avión
    avion = Avion("Boeing 737", 8, 12)  # 8 business (2 filas), 12 turista (3 filas)
    print(f"Avión creado: Modelo {avion.get_modelo()}")
    print("Número de filas en Business:", avion.get_numero_filas(Clase.BUSINESS))
    print("Número de filas en Turista:", avion.get_numero_filas(Clase.TURISTA))
    print("Butacas por fila:", avion.get_butacas_por_fila())
    print()

    # Reservar un asiento en Business
    avion.reservar_asiento(1, 1, Clase.BUSINESS, pasajero1)
    # Reservar un asiento en Turista
    avion.reservar_asiento(2, 2, Clase.TURISTA, pasajero1)

    # Mostrar mapa de asientos
    print("Mapa de asientos después de reservar:")
    avion.mostrar_mapa_de_asientos()

if __name__ == "__main__":
    main()
