from Abstracto.Instruccion import *
from Export import Salida
from Simbolo.AmbitoCompilador import AmbitoCompilador
from Simbolo.Generador import Generador

class Funcion(Instruccion):
    def __init__(self, id, parametros, tipo, instrucciones, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.parametros = parametros
        self.tipo = tipo
        self.instrucciones = instrucciones
    
    def exec(self, ambito):
        try:
            ambito.guardarFunc(self.id, self, self.linea, self.columna)
        except:
            print("Error al guardar funcion")
            Salida.salida += "Error al guardar funcion, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error al guardar funcion", self.linea, self.columna))

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="DEC_FUNCION"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreId = "Nodo" + str(Salida.num)
        Salida.graph += nombreId + '[label="' + str(self.id) + '"];\n'
        Salida.graph += nombreLit + '->' + nombreId + ';\n'
        Salida.num += 1
        if len(self.parametros) > 0:
            nombreParams = "Nodo" + str(Salida.num)
            Salida.graph += nombreParams + '[label="LISTA_PARAMETROS"];\n'
            Salida.graph += nombreLit + '->' + nombreParams + ';\n'
            Salida.num += 1
            for param in self.parametros:
                param.graph(nombreParams)
        nombreInstr = "Nodo" + str(Salida.num)
        Salida.graph += nombreInstr + '[label="INSTRUCCIONES"];\n'
        Salida.graph += nombreLit + '->' + nombreInstr + ';\n'
        Salida.num += 1
        self.instrucciones.graph(nombreInstr)

    def compile(self, ambito):
        ambito.saveFunc(self.id, self)
        genAux = Generador()
        generador = genAux.getInstance()
        
        nuevoAmbito = AmbitoCompilador(ambito.getGlobal(), self.id)

        returnLbl = generador.newLabel()
        nuevoAmbito.returnLbl = returnLbl
        nuevoAmbito.size = 1

        for param in self.parametros:
            tipo = None
            tipoAux = None
            if isinstance(param.tipo, list):
                tipo = param.tipo[0]
                tipoAux = param.tipo[1]
            else:
                tipo = param.tipo
            nuevoAmbito.saveVar(param.id, tipo, (tipo == Tipo.STRING or tipo == Tipo.STRUCT or tipo == Tipo.ARRAY),'',tipoAux)
        
        generador.addBeginFunc(self.id)

        #try:
        self.instrucciones.funcion = True
        self.instrucciones.compile(nuevoAmbito)
        #except:
            #print(f'Error al compilar instrucciones de {self.id}')
        
        generador.addGoto(returnLbl)
        generador.putLabel(returnLbl)
        generador.addEndFunc()
        generador.LeaveAllT()