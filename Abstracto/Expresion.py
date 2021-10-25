from abc import ABC, abstractmethod
from Simbolo.Ambito import *

class Expresion(ABC):
    
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna
        self.trueLbl = ''
        self.falseLbl = ''
        self.structType = ''
    
    @abstractmethod
    def exec(self, ambito):
        pass

    @abstractmethod
    def graph(self, padre):
        pass

    @abstractmethod
    def compile(self, padre):
        pass