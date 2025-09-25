from bus import Bus

busos = []
print("=== Sistema de Gestió de Busos ===")

while True:
    print("\n1.- Crear bus")
    print("2.- Venda de bitllets")
    print("3.- Devolució de bitllets")
    print("4.- Estat d'un bus")
    print("5.- Estat de TOTS els busos")
    print("0.- Sortir")

    try:
        opcio = int(input("Opció: "))
    except ValueError:
        print("Has d'introduir un número.")
        continue

    if opcio == 0:
        print("Sortint del sistema...")
        break

    elif opcio == 1:
        ident = input("ID del bus: ")
        total = int(input("Nombre de seients: "))
        busos.append(Bus(ident, total))
        print(f"Bus {ident} creat amb {total} seients.")

    elif opcio == 2:
        ident = input("ID del bus: ")
        nom = input("Nom del client: ")
        cognom = input("Cognom del client: ")

        for bus in busos:
            if bus.identificador == ident:
                print(bus.venda(nom, cognom))
                break
        else:
            print("Error: bus no trobat.")

    elif opcio == 3:
        ident = input("ID del bus: ")
        nom = input("Nom del client: ")
        cognom = input("Cognom del client: ")

        for bus in busos:
            if bus.identificador == ident:
                print(bus.devolucio(nom, cognom))
                break
        else:
            print("Error: bus no trobat.")

    elif opcio == 4:
        ident = input("ID del bus: ")
        for bus in busos:
            if bus.identificador == ident:
                print(bus.estat())
                break
        else:
            print("Error: bus no trobat.")

    elif opcio == 5:
        if not busos:
            print("No hi ha busos registrats.")
        for bus in busos:
            print(bus.estat())
