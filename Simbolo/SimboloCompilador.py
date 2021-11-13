from Abstracto.Return import *

class SimboloCompilador:

    def __init__(self, symbolID, symbolType, position, globalVar, inHeap, structType = "", auxTipo = None):
        self.id = symbolID
        self.tipo = symbolType
        self.pos = position
        self.isGlobal = globalVar
        self.inHeap = inHeap
        self.structType = structType
        self.auxTipo = auxTipo

        self.val = None