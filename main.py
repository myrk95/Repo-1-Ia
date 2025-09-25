from bus import Bus

buses = []
print("=== Sistema de Buses ===")

while True:
    print("\n1.- Crear bus")
    print("2.- Venta de billetes")
    print("3.- Devolución de billetes")
    print("4.- Estado de un bus")
    print("5.- Estado de TODOS los buses")
    print("0.- Salir")

    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Debes ingresar un número.")
        continue

    if opcion == 0:
        print("Saliendo del sistema...")
        break

    elif opcion == 1:
        ident = input("ID del bus: ")
        total = int(input("Número de asientos: "))
        buses.append(Bus(ident, total))
        print(f"Bus {ident} creado con {total} asientos.")

    elif opcion == 2:
        ident = input("ID del bus: ")
        nombre = input("Nombre del cliente: ")
        apellido = input("Apellido del cliente: ")

        for bus in buses:
            if bus.identificador == ident:
                print(bus.venta(nombre, apellido))
                break
        else:
            print("Error: bus no encontrado.")

    elif opcion == 3:
        ident = input("ID del bus: ")
        nombre = input("Nombre del cliente: ")
        apellido = input("Apellido del cliente: ")

        for bus in buses:
            if bus.identificador == ident:
                print(bus.devolucion(nombre, apellido))
                break
        else:
            print("Error: bus no encontrado.")

    elif opcion == 4:
        ident = input("ID del bus: ")
        for bus in buses:
            if bus.identificador == ident:
                print(bus.estado())
                break
        else:
            print("Error: bus no encontrado.")

    elif opcion == 5:
        if not buses:
            print("No hay buses registrados.")
        for bus in buses:
            print(bus.estado())
