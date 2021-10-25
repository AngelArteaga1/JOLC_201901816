from enum import Enum
import enum

class OpLogica(Enum):
    AND = 0
    OR = 1
    NOT = 2

class OpRelacional(Enum):
    GREATER = 0
    LESS = 1
    GREATEREQUAL = 2
    LESSEQUAL = 3
    EQUALSEQUALS = 4
    DISTINT = 5

class OpAritmetico(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIV = 3
    MOD = 4
    POW = 5

class Tipo(Enum):
    NULL = 0
    INT = 1
    FLOAT = 2
    BOOLEAN = 3
    CHAR = 4
    STRING = 5
    ARRAY = 6
    RANGE = 7
    STRUCT = 8
    NOTHING = 9

    RETURNST = 10
    CONTINUEST = 11
    BREAKST = 12

    BEGIN = 13
    END = 14

class TipoDeclaracion(Enum):
    DEFAULT = 0
    LOCAL = 1
    GLOBAL = 2

class Error:
    def __init__(self, descripcion, linea, columna):
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna

class Return:
    def __init__(self, val, tipo, auxTipo = ""):
        self.val = val
        self.tipo = tipo
        self.auxTipo = auxTipo

    def exec(self, ambito):
        return self

class ReturnCompilador:
    def __init__(self, val, tipo, esTemp, auxTipo = ""):
        self.val = val
        self.tipo = tipo
        self.esTemp = esTemp
        self.auxTipo = auxTipo

    def exec(self, ambito):
        return self