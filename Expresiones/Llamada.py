from Instruccion.Funciones.Parametro import Parametro
from Abstracto.Expresion import *
from Simbolo.Ambito import *
from Expresiones.Nativas import *
from Export import Salida
from Simbolo.Generador import Generador

class Llamada(Expresion):

    def __init__(self, id, parametros, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.parametros = parametros
    
    def exec(self, ambito):
        funcion = ambito.getFunc(self.id)
        if funcion != None:
            nuevoAmbito = Ambito(ambito.getGlobal(), self.id)
            nuevoAmbito.funcion = True
            for i in range(len(self.parametros)):
                parametro = self.parametros[i].exec(ambito)
                #Verificamos si es el mismo len de los parametros
                if len(funcion.parametros) != len(self.parametros):
                    print("Error Semantico: la llamada a la funcion '" + str(self.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(self.linea) + " columna: " + str(self.columna))
                    Salida.salida += "Error Semantico: la llamada a la funcion '" + str(self.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                    Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(self.id) + "' no tiene la cantidad de parametros correctos", self.linea, self.columna))
                    return Return("Nothing", Tipo.NOTHING)
                #Ahora verificamos si los parametros son como sus tipos
                if funcion.parametros[i].tipo != None:
                    if parametro.tipo == Tipo.STRUCT:
                        if funcion.parametros[i].tipo != parametro.auxTipo:
                            print("Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                            Salida.salida += "Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                            Salida.errores.append(Error("Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "'", self.linea, self.columna))
                            return Return("Nothing", Tipo.NOTHING)
                    else:
                        if funcion.parametros[i].tipo != parametro.tipo:
                            print("Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                            Salida.salida += "Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                            Salida.errores.append(Error("Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "'", self.linea, self.columna))
                            return Return("Nothing", Tipo.NOTHING)
                #verificamos si es una struct
                if parametro.tipo == Tipo.STRUCT:
                    nuevoAmbito.guardarVarStruct(funcion.parametros[i].id, parametro.val, parametro.auxTipo, self.linea, self.columna)
                else:
                    nuevoAmbito.guardarVar(funcion.parametros[i].id, parametro.val, parametro.tipo, self.linea, self.columna)
            funcion.instrucciones.funcion = True
            returnST = funcion.instrucciones.exec(nuevoAmbito)
            if returnST != None:
                if returnST.tipo == Tipo.RETURNST:
                    return returnST.val
                else:
                    return returnST
        elif self.id == "log10":
            return log10(self, ambito)
        elif self.id == "log":
            return log(self, ambito)
        elif self.id == "sin":
            return sin(self, ambito)
        elif self.id == "cos":
            return cos(self, ambito)
        elif self.id == "tan":
            return tan(self, ambito)
        elif self.id == "sqrt":
            return sqrt(self, ambito)
        elif self.id == "parse":
            return parse(self, ambito)
        elif self.id == "trunc":
            return trunc(self, ambito)
        elif self.id == "float":
            return Float(self, ambito)
        elif self.id == "string":
            return string(self, ambito)
        elif self.id == "typeof":
            return typeof(self, ambito)
        elif self.id == "push!":
            return push(self, ambito)
        elif self.id == "pop!":
            return Pop(self, ambito)
        elif self.id == "length":
            return length(self, ambito)
        elif self.id == "uppercase":
            return uppercase(self, ambito)
        elif self.id == "lowercase":
            return lowercase(self, ambito)
        #Ahora verificamos si es una struct
        struct = ambito.getStruct(self.id)
        tipoStruct = ambito.getTipoStruct(self.id)
        if struct != None:
            atributos = {}
            for i in range(len(self.parametros)):
                valor = self.parametros[i].exec(ambito)
                if tipoStruct[i] != None:
                    if valor.tipo == Tipo.STRUCT:
                        if tipoStruct[i] == valor.auxTipo:
                            atributos.update({
                                struct[i] : Return(valor.val, valor.tipo, valor.auxTipo)
                            })
                        else:
                            print("Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                            Salida.salida += "Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                            Salida.errores.append(Error("Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "'", self.linea, self.columna))
                            atributos.update({
                                struct[i] : Return("Nothing", Tipo.NOTHING)
                            })
                    else:
                        if tipoStruct[i] == valor.tipo:
                            atributos.update({
                                struct[i] : Return(valor.val, valor.tipo, self.id)
                            })
                        else:
                            print("Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                            Salida.salida += "Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n" 
                            Salida.errores.append(Error("Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "'", self.linea, self.columna))
                            atributos.update({
                                struct[i] : Return("Nothing", Tipo.NOTHING)
                            })
                else:
                    atributos.update({
                        struct[i] : Return(valor.val, valor.tipo, self.id)
                    })
            return Return(atributos, Tipo.STRUCT, self.id)
        print("Error Semantico: no existe la funcion o el struct '" + str(self.id) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
        Salida.salida += "Error Semantico: no existe la funcion o el struct '" + str(self.id) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: no existe la funcion o el struct '" + str(self.id) + "'", self.linea, self.columna))
        return Return("Nothing", Tipo.NOTHING)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="LLAMADA/STRUCT"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreFuncion = "Nodo" + str(Salida.num)
        Salida.graph += nombreFuncion + '[label="' + self.id + '"];\n'
        Salida.graph += nombreLit + '->' + nombreFuncion + ';\n'
        Salida.num += 1
        if len(self.parametros) > 0:
            nombreLista = "Nodo" + str(Salida.num)
            Salida.graph += nombreLista + '[label="LISTA_PARAMETROS"];\n'
            Salida.graph += nombreLit + '->' + nombreLista + ';\n'
            Salida.num += 1
            for param in self.parametros:
                if isinstance(param, Tipo):
                    nombreTipo = "Nodo" + str(Salida.num)
                    Salida.graph += nombreTipo + '[label="' + str(param) + '"];\n'
                    Salida.graph += nombreLista + '->' + nombreTipo + ';\n'
                    Salida.num += 1
                else:
                    param.graph(nombreLista)

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()
        if self.id == "parse":
            if self.parametros[0] == Tipo.INT:
                ret = self.parametros[1].compile(ambito)
                generador.fParseToInt()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, ret.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('parseToInt')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, Tipo.INT, False)
            elif self.parametros[0] == Tipo.FLOAT:
                ret = self.parametros[1].compile(ambito)
                generador.fParseToFloat()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, ret.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('parseToFloat')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, Tipo.FLOAT, False)
        elif self.id == "trunc":
            ret = self.parametros[0].compile(ambito)
            tmp = generador.addTemp()
            generador.addExp(tmp,ret.val,'','')
            return ReturnCompilador(tmp, Tipo.INT, False)
        elif self.id == "float":
            ret = self.parametros[0].compile(ambito)
            tmp = generador.addTemp()
            generador.addExp(tmp,ret.val,'0.0','+')
            return ReturnCompilador(tmp, Tipo.FLOAT, False)
        elif self.id == "string":
            value = self.parametros[0].compile(ambito)
            if value.tipo == Tipo.INT:
                generador.fIntToString()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, value.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('intToString')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, Tipo.STRING, True)
            elif value.tipo == Tipo.FLOAT:
                generador.fFloatToString()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, value.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('floatToString')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, Tipo.STRING, True)
            elif value.tipo == Tipo.CHAR:
                generador.fCharToString()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, value.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('charToString')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, Tipo.STRING, True)
            elif value.tipo == Tipo.BOOLEAN:
                tempLbl = generador.newLabel()
                result = generador.addTemp()
                
                generador.putLabel(value.trueLbl)
                # Aqui guardamos el true en el heap
                generador.addExp(result,'H','','')
                generador.setHeap('H','116') #t
                generador.nextHeap()
                generador.setHeap('H','114') #r
                generador.nextHeap()
                generador.setHeap('H','117') #u
                generador.nextHeap()
                generador.setHeap('H','101') #e
                generador.nextHeap()
                generador.setHeap('H','-1')
                generador.nextHeap()
                
                generador.addGoto(tempLbl)
                
                generador.putLabel(value.falseLbl)
                # Aqui guardamos el true en el heap
                generador.addExp(result,'H','','')
                generador.setHeap('H','102') #f
                generador.nextHeap()
                generador.setHeap('H','97')  #a
                generador.nextHeap()
                generador.setHeap('H','108') #l
                generador.nextHeap()
                generador.setHeap('H','115') #s
                generador.nextHeap()
                generador.setHeap('H','101') #e
                generador.nextHeap()
                generador.setHeap('H','-1')
                generador.nextHeap()

                generador.putLabel(tempLbl)
                return ReturnCompilador(result, Tipo.STRING, True)
        elif self.id == "length":
                ret = self.parametros[0].compile(ambito)
                generador.fLength()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, ret.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('length')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, Tipo.INT, False)
        elif self.id == "uppercase":
                ret = self.parametros[0].compile(ambito)
                generador.fUppercase()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, ret.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('uppercase')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, Tipo.STRING, True)
        elif self.id == "lowercase":
                ret = self.parametros[0].compile(ambito)
                generador.fLowercase()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, ret.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('lowercase')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, Tipo.STRING, True)
        else:
            try:
                func = ambito.getFunc(self.id)
                if func != None:
                    paramValues = []

                    size = ambito.size
                    for param in self.parametros:
                        paramValues.append(param.compile(ambito))
                    temp = generador.addTemp()

                    generador.addExp(temp, 'P', size+1, '+')
                    aux = 0
                    for param in paramValues:
                        aux += 1
                        generador.setStack(temp, param.val)
                        if aux != len(paramValues):
                            generador.addExp(temp, temp, '1', '+')
                    
                    generador.newEnv(size)
                    generador.callFun(self.id)
                    generador.getStack(temp, 'P')
                    generador.retEnv(size)
                    
                    # TODO: Verificar tipo de la funcion. Boolean es distinto
                    return Return(temp, func.tipo, True)
                else:
                    # STRUCT
                    struct = ambito.getStruct(self.id)
                    if struct != None:
                        self.structType = self.id

                        returnTemp = generador.addTemp()
                        generador.addExp(returnTemp, 'H', '', '')

                        aux = generador.addTemp()
                        generador.addExp(aux, returnTemp, '', '')

                        generador.addExp('H', 'H', len(struct), '+')

                        for att in self.params:
                            value = att.compile(ambito)

                            if value.tipo != Tipo.BOOLEAN:
                                generador.setHeap(aux, value.value)
                            else:
                                retLbl = generador.newLabel()
                                
                                generador.putLabel(value.trueLbl)
                                generador.setHeap(aux, '1')
                                generador.addGoto(retLbl)

                                generador.putLabel(value.falseLbl)
                                generador.setHeap(aux, '0')

                                generador.putLabel(retLbl)
                            generador.addExp(aux, aux, '1', '+')
                        
                        return Return(returnTemp, Tipo.STRUCT, True)
            except:
                print("Error en llamda a funcion")