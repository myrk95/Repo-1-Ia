from cliente import Cliente

class Bus:
    def __init__(self, identificador, total_asientos):
        self.identificador = identificador
        self.total_asientos = total_asientos
        self.pasajeros = []  # lista de objetos Cliente

    def venta(self, nombre, apellido):
        if len(self.pasajeros) >= self.total_asientos:
            return "Error: no hay asientos libres."
        cliente = Cliente(nombre, apellido)
        self.pasajeros.append(cliente)
        return f"Se vendió un billete a {cliente}"

    def devolucion(self, nombre, apellido):
        for c in self.pasajeros:
            if c.nombre == nombre and c.apellido == apellido:
                self.pasajeros.remove(c)
                return f"Se devolvió el billete de {c}"
        return "Error: ese cliente no existe en la lista."

    def estado(self):
        libres = self.total_asientos - len(self.pasajeros)
        return (f"Bus {self.identificador}\n"
                f"Total: {self.total_asientos}\n"
                f"Libre: {libres}\n"
                f"Vendido: {len(self.pasajeros)}\n"
                f"Clientes: {[str(c) for c in self.pasajeros]}")
