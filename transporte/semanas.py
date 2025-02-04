import datetime

def obtener_semanas_del_año(año):
    # Crear una lista para almacenar las fechas de cada semana
    semanas = []

    # Obtener el primer día del año
    fecha_inicio = datetime.date(año, 1, 1)

    # Ajustar la fecha de inicio para que sea el primer lunes del año
    # Si el primer día del año no es lunes, retroceder al lunes anterior
    if fecha_inicio.weekday() != 0:  # 0 es lunes
        fecha_inicio -= datetime.timedelta(days=fecha_inicio.weekday())

    # Iterar sobre todas las semanas del año
    for semana in range(53):  # Un año puede tener 53 semanas
        # Calcular la fecha de fin de la semana (domingo)
        fecha_fin = fecha_inicio + datetime.timedelta(days=6)

        # Agregar las fechas de inicio y fin de la semana a la lista
        semanas.append((fecha_inicio, fecha_fin))

        # Avanzar a la siguiente semana
        fecha_inicio = fecha_fin + datetime.timedelta(days=1)

        # Si la fecha de inicio supera el año actual, salir del bucle
        if fecha_inicio.year > año:
            break

    return semanas

def main():
    # Solicitar al usuario que ingrese un año
    año = int(input("Ingrese el año: "))

    # Obtener las fechas de cada semana del año
    semanas = obtener_semanas_del_año(año)

    # Imprimir las fechas de cada semana
    for i, (inicio, fin) in enumerate(semanas, start=1):
        print(f"Semana {i}: {inicio.strftime('%d-%m-%Y')} - {fin.strftime('%d-%m-%Y')}")

if __name__ == "__main__":
    main()