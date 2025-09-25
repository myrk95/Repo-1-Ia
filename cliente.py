class Client:
    def __init__(self, nom, cognom):
        self.nom = nom
        self.cognom = cognom

    def __str__(self):
        return f"{self.nom} {self.cognom}"
