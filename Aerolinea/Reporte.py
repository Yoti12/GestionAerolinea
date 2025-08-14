from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_reporte_pasajeros(lista_pasajeros, archivo_salida="reporte_pasajeros.pdf"):
    """
    Genera un reporte PDF con la lista de pasajeros.
    lista_pasajeros debe ser una lista de tuplas: (nombre, clase, asiento)
    """
    c = canvas.Canvas(archivo_salida, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Reporte de Pasajeros")

    c.setFont("Helvetica", 12)
    y = 720  # posición inicial en la página

    # Encabezados
    c.drawString(50, y, "Nombre")
    c.drawString(250, y, "Clase")
    c.drawString(400, y, "Asiento")
    y -= 20
    c.line(50, y, 550, y)
    y -= 20

    # Contenido
    for nombre, clase, asiento in lista_pasajeros:
        c.drawString(50, y, str(nombre))
        c.drawString(250, y, str(clase))
        c.drawString(400, y, str(asiento))
        y -= 20

        # Si llegamos al final de la página, creamos una nueva
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750

    c.save()
    print(f"Reporte PDF generado en '{archivo_salida}'")
