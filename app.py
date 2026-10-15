RETRASO_MS = 2000


def analizar_datos(datos, indice, limite, sequia):

    # CASO BASE:
    # Si el índice llega al tamaño de la lista,
    # significa que ya analizamos todos los datos.
    if indice == len(datos):
        return sequia

    # Obtener el dato actual de humedad
    humedad = datos[indice]

    # Determinar si existe una posible condición de sequía
    if humedad < limite:
        print(
            f"Medición {indice + 1}: {humedad}% "
            f"→ Posible condición de sequía"
        )

        # Aumentar el contador de mediciones con posible sequía
        sequia += 1

    else:
        print(
            f"Medición {indice + 1}: {humedad}% "
            f"→ Humedad adecuada"
        )

    # LLAMADA RECURSIVA:
    # La función se llama nuevamente para analizar
    # el siguiente dato de la lista.
    return analizar_datos(
        datos,
        indice + 1,
        limite,
        sequia
    )


def factorial(n):
    pass


def barra_progreso(duracion_ms, ancho=30):
    pass


class ServidorSimulado:
    def __init__(self):
        self.cola = None
        self.procesados = None

    def recibir(self, dato):
        pass

    def procesar_siguiente(self):
        pass

    def hay_pendientes(self):
        pass


def enviar_y_procesar_en_servidor(datos):
    pass


def pedir_datos():
    """Solicita al usuario 10 mediciones de humedad."""
    print("Ingresa datos")
    limite_datos = 10
    humedad = []
    for i in range(limite_datos):
        humedad_dato = int(input(f"Medición {i + 1}: "))
        humedad.append(humedad_dato)
    return humedad


def mostrar_menu_y_elegir_procesamiento():
    """Muestra el menú y devuelve la opción elegida."""
    print("\n==========================================")
    print("               MENÚ")
    print("==========================================")
    print("1. Procesar datos localmente")
    print("2. Enviar al servidor y procesar uno por uno (FIFO)")

    opcion = input("Elige una opción (1/2): ").strip()

    while opcion not in ("1", "2"):
        opcion = input("Opción inválida. Elige 1 o 2: ").strip()


def preparar_datos(humedad):
    pass


def analizar_humedad(humedad, limite=40):
    pass


def mostrar_resultados(total_mediciones, total_sequia):
    pass


def main():
    pass
