from cliente import Client

class Bus:
    def __init__(self, identificador, total_seients):
        self.identificador = identificador
        self.total_seients = total_seients
        self.clients = []  # llista d'objectes Client

    def venda(self, nom, cognom):
        if len(self.clients) >= self.total_seients:
            return "Error: no hi ha seients lliures."
        client = Client(nom, cognom)
        self.clients.append(client)
        return f"S'ha venut un bitllet a {client}"

    def devolucio(self, nom, cognom):
        for c in self.clients:
            if c.nom == nom and c.cognom == cognom:
                self.clients.remove(c)
                return f"S'ha retornat el bitllet de {c}"
        return "Error: aquest client no existeix a la llista."

    def estat(self):
        lliures = self.total_seients - len(self.clients)
        return (f"Bus {self.identificador}\n"
                f"Total: {self.total_seients}\n"
                f"Lliures: {lliures}\n"
                f"Venuts: {len(self.clients)}\n"
                f"Clients: {[str(c) for c in self.clients]}")
