from Abstracto.Instruccion import *
from Export import Salida
from Simbolo.Generador import Generador

class Print(Instruccion):

    def __init__(self, listaVal, linea, columna, nuevaLinea):
        Instruccion.__init__(self, linea, columna)
        self.listaVal = listaVal
        self.nuevaLinea = nuevaLinea
    
    def exec(self, ambito):
        imprimir = ""
        for val in self.listaVal:   
            valor = val.exec(ambito)
            if valor.tipo == None:
                return
            elif valor.tipo == Tipo.ARRAY:
                imprimir += str(self.arrayToString(valor))
                continue
            elif valor.tipo == Tipo.STRUCT:
                imprimir += str(self.structToString(valor))
                continue
            elif valor.tipo == Tipo.NOTHING:
                imprimir += "Nothing"
                continue
            imprimir += str(valor.val)
        if self.nuevaLinea:
            print(imprimir)
            Salida.salida += imprimir + "\n"
        else:
            print(imprimir, end="")
            Salida.salida += imprimir

    def structToString(self, valor):
        struct = {}
        for item in valor.val:
            if valor.val[item].tipo == Tipo.STRUCT:
                struct[item] = self.structToString(valor.val[item])
                continue
            elif valor.val[item].tipo == Tipo.ARRAY:
                struct[item] = self.arrayToString(valor.val[item])
                continue
            struct[item] = valor.val[item].val
        return struct

    def arrayToString(self, valor):
        array = []
        for item in valor.val:
            if item.tipo == Tipo.ARRAY:
                array.append(self.arrayToString(item))
                continue
            elif item.tipo == Tipo.STRUCT:
                array.append(self.structToString(item))
                continue
            array.append(item.val)
        return array

    def graph(self, padre):
        nombrePrint = "Nodo" + str(Salida.num)
        if self.nuevaLinea: 
            Salida.graph += nombrePrint + '[label="PRINTLN"];\n'
        else:
            Salida.graph += nombrePrint + '[label="PRINT"];\n'
        Salida.graph += padre + '->' + nombrePrint + ';\n'
        Salida.num += 1
        nombreLista = "Nodo" + str(Salida.num)
        Salida.graph += nombreLista + '[label="LISTA_VALORES"];\n'
        Salida.graph += nombrePrint + '->' + nombreLista + ';\n'
        Salida.num += 1
        for val in self.listaVal:
            val.graph(nombreLista)

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()
        if not generador.fmt:
            generador.addFmt()
        for val in self.listaVal:
            valor = val.compile(ambito)

            if(valor.tipo == Tipo.INT):
                generador.addPrint("d", valor.val)
            elif(valor.tipo == Tipo.FLOAT):
                generador.addPrintFloat("f", valor.val)
            elif(valor.tipo == Tipo.CHAR):
                generador.addPrint("c", valor.val)
            elif valor.tipo == Tipo.BOOLEAN:
                tempLbl = generador.newLabel()
                
                generador.putLabel(valor.trueLbl)
                generador.printTrue()
                
                generador.addGoto(tempLbl)
                
                generador.putLabel(valor.falseLbl)
                generador.printFalse()

                generador.putLabel(tempLbl)
            elif valor.tipo == Tipo.STRING:
                # print(valor.val)
                generador.fPrintString()

                paramTemp = generador.addTemp()
                
                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, valor.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('printString')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)
            elif valor.tipo == Tipo.NOTHING:
                generador.printNothing()
            else:
                print("POR HACER")
            
        if self.nuevaLinea:
            generador.addPrint("c", 10)