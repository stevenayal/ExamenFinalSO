import sys

def sjf_preemptivo(procesos):
    tiempo = 0
    grafico_gantt = []
    while procesos:
        # Seleccionar proceso con el menor tiempo de ráfaga restante
        cola_listos = [p for p in procesos if p['llegada'] <= tiempo]
        if not cola_listos:
            tiempo += 1
            continue

        actual = min(cola_listos, key=lambda x: x['rafaga'])
        grafico_gantt.append((actual['nombre'], tiempo, tiempo + 1))
        actual['rafaga'] -= 1
        tiempo += 1

        if actual['rafaga'] == 0:
            procesos.remove(actual)

    return grafico_gantt


if __name__ == "__main__":
    procesos = [
        {'nombre': 'A', 'llegada': 0, 'rafaga': 7},
        {'nombre': 'B', 'llegada': 2, 'rafaga': 13},
        {'nombre': 'C', 'llegada': 4, 'rafaga': 3},
        {'nombre': 'D', 'llegada': 4, 'rafaga': 5},
        {'nombre': 'E', 'llegada': 6, 'rafaga': 7},
        {'nombre': 'F', 'llegada': 6, 'rafaga': 3},
    ]

    # Ejecución
    grafico_gantt = sjf_preemptivo(procesos)
    for entrada in grafico_gantt:
        print(f"Proceso {entrada[0]}: {entrada[1]} - {entrada[2]}")