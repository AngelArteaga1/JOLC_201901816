from Abstracto.Expresion import Expresion
from Abstracto.Instruccion import *
from Abstracto.Return import *
from Export import Salida
from Instruccion.Variables.Declaracion import Declaracion
from Simbolo.Generador import Generador
from Simbolo.AmbitoCompilador import AmbitoCompilador

class For(Instruccion):

    def __init__(self, id, expresion, instrucciones, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.expresion = expresion
        self.instrucciones = instrucciones
    
    def exec(self, ambito):
        valor = self.expresion.exec(ambito)
        nuevoAmbito = Ambito(ambito, "For")
        if valor.tipo == Tipo.RANGE:
            rango = range(valor.val.minimo.val, valor.val.maximo.val+1)
            for i in rango:
                nuevoAmbito.guardarVar(self.id, i, Tipo.INT, self.linea, self.columna)
                item = self.instrucciones.exec(nuevoAmbito)
                if item != None:
                    if item.tipo == Tipo.BREAKST:
                        break
                    elif item.tipo == Tipo.CONTINUEST:
                        continue
                    else:
                        return item
        elif valor.tipo == Tipo.ARRAY:
            for i in valor.val:
                nuevoAmbito.guardarVar(self.id, i.val, i.tipo, self.linea, self.columna)
                item = self.instrucciones.exec(nuevoAmbito)
                if item != None:
                    if item.tipo == Tipo.BREAKST:
                        break
                    elif item.tipo == Tipo.CONTINUEST:
                        continue
                    else:
                        return item
        elif valor.tipo == Tipo.STRING:
            for i in valor.val:
                nuevoAmbito.guardarVar(self.id, i, Tipo.STRING, self.linea, self.columna)
                item = self.instrucciones.exec(nuevoAmbito)
                if item != None:
                    if item.tipo == Tipo.BREAKST:
                        break
                    elif item.tipo == Tipo.CONTINUEST:
                        continue
                    else:
                        return item
        else:
            print("Error Semantico: el valor del for no es iterable porque es de tipo " + str(valor.tipo) + ", linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el valor del for no es iterable porque es de tipo " + str(valor.tipo) + ", linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el valor del for no es iterable porque es de tipo " + str(valor.tipo), self.linea, self.columna))
            return

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="FOR"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreId = "Nodo" + str(Salida.num)
        Salida.graph += nombreId + '[label="' + str(self.id) + '"];\n'
        Salida.graph += nombreLit + '->' + nombreId + ';\n'
        Salida.num += 1
        self.expresion.graph(nombreLit)
        nombreInstr = "Nodo" + str(Salida.num)
        Salida.graph += nombreInstr + '[label="INSTRUCCIONES"];\n'
        Salida.graph += nombreLit + '->' + nombreInstr + ';\n'
        Salida.num += 1
        self.instrucciones.graph(nombreInstr)

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()

        #Comentamos que comenzamos el if
        generador.addComment("INICIO DEL FOR")
        nuevoAmbito = AmbitoCompilador(ambito)

        exp = self.expresion.compile(ambito)

        continueLbl = generador.newLabel()
        breakLbl = generador.newLabel()
        iterateLbl = generador.newLabel()
        #Se lo seteamos al nuevo ambito
        nuevoAmbito.breakLbl = breakLbl
        nuevoAmbito.continueLbl = iterateLbl

        if exp.tipo == Tipo.RANGE:

            #Obtenemos los valores
            min = exp.val.minimo.compile(ambito)
            max = exp.val.maximo.compile(ambito)
            tmp = generador.addTemp()
            generador.addExp(tmp,min.val,'','')

            #**********AQUI YA EMPEZAMOS EL CICLO**********
            generador.putLabel(continueLbl)
            newVar = nuevoAmbito.saveVar(self.id, Tipo.INT, False)
            # Obtencion de posicion de la variable
            tempPos = newVar.pos
            if(not newVar.isGlobal):
                tempPos = generador.addTemp()
                generador.addExp(tempPos, 'P', newVar.pos, "+")
            generador.setStack(tempPos, tmp)

            #Ahora ya compilamos las intrucciones
            self.instrucciones.compile(nuevoAmbito)

            generador.addGoto(iterateLbl)
            generador.putLabel(iterateLbl)
            generador.addExp(tmp,tmp,'1','+')
            generador.addIf(tmp,max.val,'>',breakLbl)
            generador.addGoto(continueLbl)
        elif exp.tipo == Tipo.STRING:

            #Obtenemos los valores
            tmp = generador.addTemp()
            tmpH = generador.addTemp()
            generador.addExp(tmpH,exp.val,'','')
            generador.getHeap(tmp,tmpH)

            #**********AQUI YA EMPEZAMOS EL CICLO**********
            generador.putLabel(continueLbl)
            newVar = nuevoAmbito.saveVar(self.id, Tipo.CHAR, False)
            # Obtencion de posicion de la variable
            tempPos = newVar.pos
            if(not newVar.isGlobal):
                tempPos = generador.addTemp()
                generador.addExp(tempPos, 'P', newVar.pos, "+")
            generador.setStack(tempPos, tmp)

            #Ahora ya compilamos las intrucciones
            self.instrucciones.compile(nuevoAmbito)

            generador.addGoto(iterateLbl)
            generador.putLabel(iterateLbl)
            generador.addExp(tmpH,tmpH,'1','+')
            generador.getHeap(tmp,tmpH)
            generador.addIf(tmp,'-1','==',breakLbl)
            generador.addGoto(continueLbl)
        elif exp.tipo == Tipo.ARRAY:

            #Obtenemos los valores
            tmp = generador.addTemp()
            tmpH = generador.addTemp()
            generador.addExp(tmpH,exp.val,'','')
            generador.getHeap(tmp,tmpH)

            #**********AQUI YA EMPEZAMOS EL CICLO**********
            generador.putLabel(continueLbl)
            newVar = nuevoAmbito.saveVar(self.id, exp.auxTipo, True)
            # Obtencion de posicion de la variable
            tempPos = newVar.pos
            if(not newVar.isGlobal):
                tempPos = generador.addTemp()
                generador.addExp(tempPos, 'P', newVar.pos, "+")
            generador.setStack(tempPos, tmp)

            #Ahora ya compilamos las intrucciones
            self.instrucciones.compile(nuevoAmbito)

            generador.addGoto(iterateLbl)
            generador.putLabel(iterateLbl)
            generador.addExp(tmpH,tmpH,'1','+')
            generador.getHeap(tmp,tmpH)
            generador.addIf(tmp,'-1','==',breakLbl)
            generador.addGoto(continueLbl)

        generador.putLabel(breakLbl)
        generador.addComment("FIN DEL FOR")