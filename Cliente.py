class Cliente:
    def __init__(self, nombre, Dui):
        self.nombre = nombre
        self.Dui = Dui

    def __repr__(self):
        return f"{self.nombre} - {self.Dui}"

    