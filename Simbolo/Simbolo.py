from Abstracto.Return import *

class Simbolo:

    def __init__(self, val, id, tipoSimbolo, simboloOBJ = ""):
        self.val = val
        self.id = id
        self.tipo = tipoSimbolo
        # Structs
        self.objeto = simboloOBJ
        self.atributos = {}