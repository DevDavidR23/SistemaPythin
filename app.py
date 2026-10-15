import sys
import time
from collections import deque

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





# ------------------------------------------
# BARRA DE PROGRESO CON RETRASO
# ------------------------------------------

def barra_progreso(duracion_ms, ancho=30):
    """Muestra una barra que se llena durante duracion_ms milisegundos."""
    pausa = (duracion_ms / 1000) / ancho     # segundos por paso

    for paso in range(ancho + 1):
        porcentaje = int((paso / ancho) * 100)
        llena = "█" * paso
        vacia = "░" * (ancho - paso)
        sys.stdout.write(f"\r  Procesando: [{llena}{vacia}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(pausa)

    print()   # salto de línea al terminar

class ServidorSimulado:
    def _init_(self):
        self.cola = deque()        # Cola FIFO de datos recibidos
        self.procesados = []       # Datos ya procesados, en orden de salida

    def recibir(self, dato):
        """Simula el envío de un dato al servidor (ENQUEUE)."""
        self.cola.append(dato)
        print(f"  [CLIENTE → SERVIDOR] Dato enviado: {dato}%")

    def procesar_siguiente(self):
        """El servidor atiende el primer dato que llegó (DEQUEUE)."""
        dato = self.cola.popleft()

        # Espera de 2000 ms con barra de progreso antes de imprimir
        barra_progreso(RETRASO_MS)

        self.procesados.append(dato)
        print(
            f"  [SERVIDOR] Dato procesado: {dato}% "
            f"| Pendientes en cola: {len(self.cola)}\n"
        )
        return dato

    def hay_pendientes(self):
        return len(self.cola) > 0


def enviar_y_procesar_en_servidor(datos):
    """Envía los datos en orden y el servidor los procesa uno por uno."""
    servidor = ServidorSimulado()

    print("\n===== ENVIANDO DATOS AL SERVIDOR (FIFO) =====\n")
    for dato in datos:
        servidor.recibir(dato)

    print("\n===== SERVIDOR PROCESANDO UNO POR UNO =====\n")
    while servidor.hay_pendientes():
        servidor.procesar_siguiente()

    # Devuelve los datos en el orden en que el servidor los procesó
    return servidor.procesados

"""""sofia """
def pedir_datos():
    """Solicita al usuario 10 mediciones de humedad."""
    print("Ingresa datos")
    limite_datos = 10
    humedad = []
    for i in range(limite_datos):
        humedad_dato = int(input(f"Medición {i + 1}: "))
        humedad.append(humedad_dato)
    return humedad

def analizar_datos(datos, indice, limite, sequia):
    pass

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

"""""paula """
def preparar_datos(humedad):
    """Aplica el procesamiento elegido a los datos."""
    opcion = mostrar_menu_y_elegir_procesamiento()

    if opcion == "2":
        # El servidor devuelve los datos en el orden FIFO procesado
        humedad = enviar_y_procesar_en_servidor(humedad)

    return humedad
def analizar_humedad(humedad, limite=40):
    """Analiza la humedad y devuelve el total de mediciones con posible sequía."""
    sequia = 0
    print("\n===== ANÁLISIS DE MEDICIONES =====\n")

    total_sequia = analizar_datos(
        humedad,
        0,
        limite,
        sequia
    )

    return total_sequia


def mostrar_resultados(total_mediciones, total_sequia):
    """Imprime los resultados del análisis."""
    porcentaje = (total_sequia / total_mediciones) * 100

    print("\n==========================================")
    print("              RESULTADOS")
    print("==========================================")

    print(f"Total de mediciones: {total_mediciones}")
    print(f"Mediciones con posible sequía: {total_sequia}")
    print(f"Porcentaje de posible sequía: {porcentaje:.2f}%")



def main():
    """Función principal del programa."""
    print("==========================================")
    print("       MONITOREO DE HUMEDAD DEL SUELO")
    print("==========================================")

    humedad = pedir_datos()
    humedad = preparar_datos(humedad)
    total_sequia = analizar_humedad(humedad)
    total_mediciones = len(humedad)
    mostrar_resultados(total_mediciones, total_sequia)


if _name_ == "_main_":
    main()