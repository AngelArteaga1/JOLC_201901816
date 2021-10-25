from abc import ABC, abstractmethod
from Simbolo.Ambito import *

class Instruccion(ABC):
    
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna
    
    @abstractmethod
    def exec(self, ambito):
        pass

    @abstractmethod
    def graph(self, ambito):
        pass

    @abstractmethod
    def compile(self, padre):
        pass
    