from .Ambito import Ambito

class Generador:
    generador = None
    def __init__(self):
        # Contadores
        self.contTmp = 0
        self.contLabel = 0
        # Code
        self.imports = ''
        self.codigo = ''
        self.funciones = ''
        self.nativas = ''
        self.enFuncion = False
        self.enNativas = False
        # Lista de Temporales
        self.tmps = []
        self.tmpsR = {}
        # Lista de Imports
        self.fmt = False
        self.math = False
        # Lista de Nativas
        self.printString = False
        self.potencia = False
        self.potenciaLeft = False
        self.concatenar = False
        self.compararIgual = False
        self.uppercase = False
        self.lowercase = False
        self.parseToInt = False
        self.parseToFloat = False
        self.intToString = False
        self.floatToString = False
        self.charToString = False
        self.length = False

    def clean(self):
        # Contadores
        self.contTmp = 0
        self.contLabel = 0
        # Code
        self.codigo = ''
        self.funciones = ''
        self.nativas = ''
        self.enFuncion = False
        self.enNativas = False
        # Lista de Temporales
        self.tmps = []
        # Lista de Nativas
        self.printString = False
        self.potencia = False
        Generador.generador = Generador()

    #############
    # CODE
    #############
    def getEncabezado(self):
        ret = '/*----HEADER----*/\npackage main;\n\nimport (\n' + self.imports +')\n\n'
        if len(self.tmps) > 0:
            ret += 'var '
            for tmp in range(len(self.tmps)):
                ret += self.tmps[tmp]
                if tmp != (len(self.tmps) - 1):
                    ret += ", "
            ret += " float64;\n"
        ret += "var P, H float64;\nvar stack [30101999]float64;\nvar heap [30101999]float64;\n\n"
        return ret

    def getCodigo(self):
        return f'{self.getEncabezado()}{self.nativas}\n{self.funciones}\nfunc main(){{\n{self.codigo}\n}}'

    def getInstance(self):
        if Generador.generador == None:
            Generador.generador = Generador()
        return Generador.generador


    def codeIn(self, code, tab="\t"):
        if(self.enNativas):
            if(self.nativas == ''):
                self.nativas = self.nativas + '/*-----NATIVES-----*/\n'
            self.nativas = self.nativas + tab + code
        elif(self.enFuncion):
            if(self.funciones == ''):
                self.funciones = self.funciones + '/*-----FUNCS-----*/\n'
            self.funciones = self.funciones + tab +  code
        else:
            self.codigo = self.codigo + '\t' +  code

    def addComment(self, comment):
        self.codeIn(f'/* {comment} */\n')
    
    def addSpace(self):
        self.codeIn("\n")

    #################
    # Errores
    #################
    def addError(self, cadenita):
        for i in cadenita:
            self.addPrint('c',ord(i))
        self.addPrint("c", 10)

    ########################
    # Manejo de Temporales
    ########################
    def addTemp(self):
        temp = f't{self.contTmp}'
        self.contTmp += 1
        self.tmps.append(temp)
        self.tmpsR[temp] = temp
        return temp

    def LeaveAllT(self):
        self.tmpsR = {}

    def LeaveT(self, temp):
        if(temp in self.tmpsR):
            self.tmpsR.pop(temp, None)

    def saveT(self, env):
        size = 0
        if len(self.tmpsR) > 0:
            temp = self.addTemp()
            self.LeaveT(temp)
            # Aqui empezamos a guardar los temporales
            self.addExp(temp, 'P', env.size, '+')
            for value in self.tmpsR:
                size += 1
                self.setStack(temp, value, False)
                if size != len(self.tmpsR):
                    self.addExp(temp, temp, '1', '+')
            # Aqui terminamos de guardar los temporales
        ptr = env.size
        env.size = ptr + size
        return ptr
    
    def recoverT(self, env, pos):
        if len(self.tmpsR) > 0:
            temp = self.addTemp()
            self.LeaveT(temp)

            size = 0

            # Recuperacion de temporales
            self.addExp(temp, 'P', pos, '+')
            for value in self.tmpsR:
                size += 1
                self.getStack(value, temp)
                if size != len(self.tmpsR):
                    self.addExp(temp, temp, '1', '+')
            env.size = pos
            # Fin Recuperacion de temporales

    #####################
    # Manejo de Labels
    #####################
    def newLabel(self):
        label = f'L{self.contLabel}'
        self.contLabel += 1
        return label

    def putLabel(self, label):
        self.codeIn(f'{label}:\n')

    ###################
    # GOTO
    ###################
    def addGoto(self, label):
        self.codeIn(f'goto {label};\n')
    
    ###################
    # IF
    ###################
    def addIf(self, left, right, op, label):
        self.LeaveT(left)
        self.LeaveT(right)
        self.codeIn(f'if {left} {op} {right} {{goto {label};}}\n')

    ###################
    # EXPRESIONES
    ###################
    def addExp(self, result, left, right, op):
        self.LeaveT(left)
        self.LeaveT(right)
        self.codeIn(f'{result}={left}{op}{right};\n')

    def addExpMod(self, result, left, right):
        self.codeIn(f'{result}=math.Mod({left},{right});\n')
    
    ###################
    # FUNCS
    ###################
    def addBeginFunc(self, id):
        if(not self.enNativas):
            self.enFuncion = True
        self.codeIn(f'func {id}(){{\n', '')
    
    def addEndFunc(self):
        self.codeIn('return;\n}\n')
        if(not self.enNativas):
            self.enFuncion = False

    ###############
    # STACK
    ###############
    def setStack(self, pos, value, Leave = True):
        self.LeaveT(pos)
        if Leave:
            self.LeaveT(value)
        self.codeIn(f'stack[int({pos})]={value};\n')
    
    def getStack(self, place, pos):
        self.LeaveT(pos)
        self.codeIn(f'{place}=stack[int({pos})];\n')

    #############
    # ENVS
    #############
    def newEnv(self, size):
        self.codeIn(f'P=P+{size};\n')

    def callFun(self, id):
        self.codeIn(f'{id}();\n')

    def retEnv(self, size):
        self.codeIn(f'P=P-{size};\n')

    ###############
    # HEAP
    ###############
    def setHeap(self, pos, value):
        self.LeaveT(pos)
        self.LeaveT(value)
        self.codeIn(f'heap[int({pos})]={value};\n')

    def getHeap(self, place, pos):
        self.LeaveT(pos)
        self.codeIn(f'{place}=heap[int({pos})];\n')

    def nextHeap(self):
        self.codeIn('H=H+1;\n')

    # INSTRUCCIONES
    def addPrint(self, type, value):
        self.LeaveT(value)
        self.codeIn(f'fmt.Printf("%{type}", int({value}));\n')

    def addPrintFloat(self, type, value):
        self.LeaveT(value)
        self.codeIn(f'fmt.Printf("%{type}", {value});\n')
    
    def printTrue(self):
        self.addPrint("c", 116) #t
        self.addPrint("c", 114) #r
        self.addPrint("c", 117) #u
        self.addPrint("c", 101) #e

    def printFalse(self):
        self.addPrint("c", 102) #f
        self.addPrint("c", 97)  #a
        self.addPrint("c", 108) #l
        self.addPrint("c", 115) #s
        self.addPrint("c", 101) #e

    def printNothing(self):
        self.addPrint("c", 110) #n
        self.addPrint("c", 111) #o
        self.addPrint("c", 116) #t
        self.addPrint("c", 104) #h
        self.addPrint("c", 105) #i
        self.addPrint("c", 110) #n
        self.addPrint("c", 103) #g
    
    ##############
    # IMPORTS
    ##############
    def addFmt(self):
        self.imports += '\t"fmt";\n'
        self.fmt = True
    def addMath(self):
        self.imports += '\t"math";\n'
        self.math = True


    ##############
    # NATIVES
    ##############
    def fPrintString(self):
        if(self.printString):
            return
        self.printString = True
        self.enNativas = True

        self.addBeginFunc('printString')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()

        self.putLabel(compareLbl)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', returnLbl)

        self.addPrint('c', tempC)

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl)

        self.putLabel(returnLbl)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempP)
        self.LeaveT(tempH)
        self.LeaveT(tempC)
    
    def fPotencia(self):
        if(self.potencia):
            return
        self.potencia = True
        self.enNativas = True

        self.addBeginFunc('potencia')

        L3 = self.newLabel()
        
        t0 = self.addTemp()
        self.addExp(t0, 'P', '1', '+')

        t1 = self.addTemp()
        self.getStack(t1, t0)

        self.addExp(t0, t0, '1', '+')

        t2 = self.addTemp()
        self.getStack(t2, t0)
        L2 = self.newLabel()
        self.addIf(t2, '0', '<=', L2)
        self.addExp(t0, t1, '', '')

        L0 = self.newLabel()
        L1 = self.newLabel()

        self.putLabel(L0)
        self.addIf(t2, '1', '<=', L1)
        self.addExp(t1, t1, t0, '*')
        self.addExp(t2, t2, '1', '-')
        self.addGoto(L0)

        self.putLabel(L2)
        self.setStack('P', 1)
        self.addGoto(L3)

        self.putLabel(L1)
        self.setStack('P', t1)


        self.putLabel(L3)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(t0)
        self.LeaveT(t1)
        self.LeaveT(t2)

    def fPotenciaStringLeft(self):
        if(self.potenciaLeft):
            return
        self.potenciaLeft = True
        self.enNativas = True

        self.addBeginFunc('potenciaLeft')

        # Guardamos el heap
        retTemp = self.addTemp()
        self.addExp(retTemp, 'H', '', '')

        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()
        #Label para verificar si ya lo logramos
        verificarLbl = self.newLabel()
        #Label para resetear el string
        resetLbl = self.newLabel()


        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()

        self.addExp(tempP, 'P', '1', '+')

        # Temporal del exponente
        Temp = self.addTemp()
        self.addExp(Temp, 'P', '2', '+')

        tempE = self.addTemp()
        self.getStack(tempE, Temp)

        self.putLabel(resetLbl)

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()

        self.putLabel(compareLbl)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', verificarLbl)

        self.setHeap('H', tempC)
        self.nextHeap()

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl)

        #Aqui verificamos si el exponente es 0
        self.putLabel(verificarLbl)
        self.addIf(tempE, '1', '<=', returnLbl)
        self.addExp(tempE, tempE, '1', '-')
        self.addGoto(resetLbl)



        
        self.putLabel(returnLbl)
        self.setHeap('H', '-1')            # FIN DE CADENA
        self.nextHeap()
        self.setStack('P', retTemp)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(retTemp)
        self.LeaveT(tempC)
        self.LeaveT(tempH)
        self.LeaveT(tempE)
        self.LeaveT(tempP)
        self.LeaveT(Temp)

    def fConcatenar(self):
        if(self.concatenar):
            return
        self.concatenar = True
        self.enNativas = True

        self.addBeginFunc('concatenar')

        # Guardamos el heap
        retTemp = self.addTemp()
        self.addExp(retTemp, 'H', '', '')

        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()
        # Label para la segunda cadena
        secondLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena 2
        compareLbl2 = self.newLabel()


        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()

        self.putLabel(compareLbl)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', secondLbl)

        self.setHeap('H', tempC)
        self.nextHeap()

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl)



        self.putLabel(secondLbl)

        self.addExp(tempP, 'P', '2', '+')

        self.getStack(tempH, tempP)

        self.putLabel(compareLbl2)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', returnLbl)

        self.setHeap('H', tempC)
        self.nextHeap()

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl2)

        
        self.putLabel(returnLbl)
        self.setHeap('H', '-1')            # FIN DE CADENA
        self.nextHeap()
        self.setStack('P', retTemp)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(retTemp)
        self.LeaveT(tempH)
        self.LeaveT(tempC)
        self.LeaveT(tempP)

    def fCompararIgual(self):
        if(self.compararIgual):
            return
        self.compararIgual = True
        self.enNativas = True

        self.addBeginFunc('compararIgual')

        # Guardamos el heap
        retTemp = self.addTemp()
        self.addExp(retTemp, 'H', '', '')

        # Label para imprimir true
        trueLbl = self.newLabel()
        #Label para imprimir false
        falseLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()


        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()

        self.putLabel(compareLbl)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', trueLbl)

        self.setHeap('H', tempC)
        self.nextHeap()

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl)

        
        self.putLabel(trueLbl)
        self.putLabel(falseLbl)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(retTemp)
        self.LeaveT(tempP)
        self.LeaveT(tempC)
        self.LeaveT(tempH)

    def fUppercase(self):
        if(self.uppercase):
            return
        self.uppercase = True
        self.enNativas = True

        self.addBeginFunc('uppercase')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()
        # Label para solo concatenar el char
        concatLbl = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()
        tempR = self.addTemp()
        self.addExp(tempR,'H','','')

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()

        self.putLabel(compareLbl)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', returnLbl)
        self.addIf(tempC, '97', '<', concatLbl)
        self.addIf(tempC, '122', '>', concatLbl)

        self.addExp(tempC,tempC,'32','-')
        self.putLabel(concatLbl)
        self.setHeap('H', tempC)
        self.nextHeap()

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl)

        self.putLabel(returnLbl)
        self.setHeap('H', '-1')            # FIN DE CADENA
        self.nextHeap()
        self.setStack('P', tempR)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempC)
        self.LeaveT(tempH)
        self.LeaveT(tempP)
        self.LeaveT(tempR)

    def fLowercase(self):
        if(self.lowercase):
            return
        self.lowercase = True
        self.enNativas = True

        self.addBeginFunc('lowercase')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()
        # Label para solo concatenar el char
        concatLbl = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()
        tempR = self.addTemp()
        self.addExp(tempR,'H','','')

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()

        self.putLabel(compareLbl)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', returnLbl)
        self.addIf(tempC, '65', '<', concatLbl)
        self.addIf(tempC, '90', '>', concatLbl)

        self.addExp(tempC,tempC,'32','+')
        self.putLabel(concatLbl)
        self.setHeap('H', tempC)
        self.nextHeap()

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl)

        self.putLabel(returnLbl)
        self.setHeap('H', '-1')            # FIN DE CADENA
        self.nextHeap()
        self.setStack('P', tempR)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempC)
        self.LeaveT(tempH)
        self.LeaveT(tempP)
        self.LeaveT(tempR)

    def fParseToInt(self):
        if(self.parseToInt):
            return
        self.parseToInt = True
        self.enNativas = True

        self.addBeginFunc('parseToInt')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        ciclo1 = self.newLabel()
        # Label para el segundo ciclo
        siguiente = self.newLabel()
        ciclo2 = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()

        #Temporal del multiplicador y del resultado
        mult = self.addTemp()
        self.addExp(mult,'1','','')
        resultado = self.addTemp()
        self.addExp(resultado,'0','','')

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()
        self.getHeap(tempC, tempH)
        
        #Comprobamos si es negativo el numero
        esNegativo = self.addTemp()
        self.addExp(esNegativo,'0','','')
        self.addIf(tempC, '45', '!=', ciclo1)
        self.addExp(esNegativo,'1','','')
        self.addExp(tempH, tempH, '1', '+')
        
        self.putLabel(ciclo1)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '46', '==', siguiente)
        self.addIf(tempC, '-1', '==', siguiente)
        self.addIf(tempC, '48', '<' , returnLbl)
        self.addIf(tempC, '57', '>' , returnLbl)

        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(mult,mult,'10','*')
        
        #Aqui iteramos
        self.addExp(tempH, tempH, '1', '+')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo1)

        #Seguimos despues de obtener el multiplicador y reseteamos
        self.putLabel(siguiente)
        self.addExp(mult,mult,'10','/')

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)
        
        self.addIf(esNegativo, '0', '==', ciclo2)
        self.addExp(tempH, tempH, '1', '+')

        #Empezamos el segundo ciclo
        self.putLabel(ciclo2)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '46', '==', returnLbl)
        self.addIf(tempC, '-1', '==', returnLbl)

        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(tempC,tempC,'48','-')
        tmp = self.addTemp()
        self.addExp(tmp,tempC,mult,'*')
        self.addExp(resultado,resultado,tmp,'+')
        self.addExp(mult,mult,'10','/')
        
        #Aqui iteramos
        self.addExp(tempH, tempH, '1', '+')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo2)

        self.putLabel(returnLbl)
        
        #Si es negativo lo multiplicamos
        seguir = self.newLabel()
        self.addIf(esNegativo, '0', '==', seguir)
        self.addExp(resultado,'0',resultado,'-')
        
        self.putLabel(seguir)
        self.setStack('P', resultado)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempH)
        self.LeaveT(tempC)
        self.LeaveT(tempP)
        self.LeaveT(mult)
        self.LeaveT(resultado)
        self.LeaveT(tmp)
        self.LeaveT(esNegativo)

    def fParseToFloat(self):
        if(self.parseToFloat):
            return
        self.parseToFloat = True
        self.enNativas = True

        self.addBeginFunc('parseToFloat')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        ciclo1 = self.newLabel()
        # Label para el segundo ciclo
        siguiente = self.newLabel()
        siguiente2 = self.newLabel()
        ciclo2 = self.newLabel()
        #Label para el tercer ciclo
        ciclo3 = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()

        #Temporal del multiplicador y del resultado
        mult = self.addTemp()
        self.addExp(mult,'1','','')
        div = self.addTemp()
        self.addExp(div,'1','','')
        resultado = self.addTemp()
        self.addExp(resultado,'0','','')

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()
        self.getHeap(tempC, tempH)

        #Comprobamos si es negativo el numero
        esNegativo = self.addTemp()
        self.addExp(esNegativo,'0','','')
        self.addIf(tempC, '45', '!=', ciclo1)
        self.addExp(esNegativo,'1','','')
        self.addExp(tempH, tempH, '1', '+')

        self.putLabel(ciclo1)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '46', '==', siguiente)
        self.addIf(tempC, '-1', '==', siguiente)
        self.addIf(tempC, '48', '<' , returnLbl)
        self.addIf(tempC, '57', '>' , returnLbl)

        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(mult,mult,'10','*')
        
        #Aqui iteramos
        self.addExp(tempH, tempH, '1', '+')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo1)

        #Seguimos despues de obtener el multiplicador y reseteamos
        self.putLabel(siguiente)
        self.addExp(mult,mult,'10','/')

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)
        
        self.addIf(esNegativo, '0', '==', ciclo2)
        self.addExp(tempH, tempH, '1', '+')

        #Empezamos el segundo ciclo
        self.putLabel(ciclo2)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '46', '==', siguiente2)
        self.addIf(tempC, '-1', '==', returnLbl)

        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(tempC,tempC,'48','-')
        tmp = self.addTemp()
        self.addExp(tmp,tempC,mult,'*')
        self.addExp(resultado,resultado,tmp,'+')
        self.addExp(mult,mult,'10','/')
        
        #Aqui iteramos
        self.addExp(tempH, tempH, '1', '+')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo2)

        #Aqui seguimos con el ciclo pero de los decimales
        self.putLabel(siguiente2)
        self.addExp(tempH, tempH, '1', '+')
        self.putLabel(ciclo3)
        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', returnLbl)

        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(div,div,'10','/')
        self.addExp(tempC,tempC,'48','-')
        tmp2 = self.addTemp()
        self.addExp(tmp2,tempC,div,'*')
        self.addExp(resultado,resultado,tmp2,'+')
        
        #Aqui iteramos
        self.addExp(tempH, tempH, '1', '+')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo3)
        

        self.putLabel(returnLbl)
        #Si es negativo lo multiplicamos
        seguir = self.newLabel()
        self.addIf(esNegativo, '0', '==', seguir)
        self.addExp(resultado,'0',resultado,'-')
        
        self.putLabel(seguir)
        self.setStack('P', resultado)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempC)
        self.LeaveT(tempH)
        self.LeaveT(tempP)
        self.LeaveT(tmp)
        self.LeaveT(tmp2)
        self.LeaveT(resultado)
        self.LeaveT(esNegativo)
        self.LeaveT(mult)
        self.LeaveT(div)

    def fIntToString(self):
        if(self.intToString):
            return
        if(not self.math):
            self.addMath()
        self.intToString = True
        self.enNativas = True

        self.addBeginFunc('intToString')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para los ciclos
        ciclo1 = self.newLabel()
        ciclo2 = self.newLabel()
        # Label para siguiente
        siguiente = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()
        self.addExp(tempP, 'P', '1', '+')
        
        #Variable resultado
        resultado = self.addTemp()
        self.addExp(resultado,'H','','')

        # Variable del numero
        numero = self.addTemp()
        self.getStack(numero, tempP)
        #Verificamos si el numero es negativo
        seguir = self.newLabel()
        self.addIf(numero,'0','>',seguir)
        self.addExp(numero,'0',numero,'-')
        self.setHeap('H',45)
        self.nextHeap()
        #Ponemos el label para seguir
        self.putLabel(seguir)
        # Temporal del numero 
        TmpNumero = self.addTemp()
        self.addExp(TmpNumero,numero,'','')
        # Temporal del numero 2
        TmpNumero2 = self.addTemp()
        self.addExp(TmpNumero2,numero,'','')
        # Caracter del numero
        caracter = self.addTemp()
        self.addExp(caracter,'0','','')

        #Temporal decimal
        mult = self.addTemp()
        self.addExp(mult,'1','','')
        
        #INICIAMOS EL CICLO
        self.putLabel(ciclo1)
        #VALIDACIONES
        self.addIf(TmpNumero, '1', '<', siguiente)

        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(mult,mult,'10','*')
        
        #Aqui iteramos
        self.addExp(TmpNumero, TmpNumero, '10', '/')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo1)

        #Seguimos despues de obtener el multiplicador y reseteamos
        self.putLabel(siguiente)
        self.addExp(mult,mult,'10','/')

        #Empezamos el segundo ciclo
        self.putLabel(ciclo2)

        self.addIf(mult, '1', '<', returnLbl)


        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(TmpNumero2,numero,mult,'/')
        self.addExp(caracter,TmpNumero2,'48','+')
        self.setHeap('H',caracter)
        self.nextHeap()
        self.addExpMod(numero,numero,mult)
        
        #Aqui iteramos
        self.addExp(mult,mult,'10','/')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo2)
        

        self.putLabel(returnLbl)
        self.setHeap('H','-1')
        self.nextHeap()
        self.setStack('P', resultado)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempP)
        self.LeaveT(numero)
        self.LeaveT(TmpNumero)
        self.LeaveT(TmpNumero2)
        self.LeaveT(mult)
        self.LeaveT(caracter)
        self.LeaveT(resultado)

    def fFloatToString(self):
        if(self.floatToString):
            return
        if(not self.math):
            self.addMath()
        self.floatToString = True
        self.enNativas = True

        self.addBeginFunc('floatToString')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para los ciclos
        ciclo1 = self.newLabel()
        ciclo2 = self.newLabel()
        ciclo3 = self.newLabel()
        # Label para siguiente
        siguiente = self.newLabel()
        siguiente2 = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()
        self.addExp(tempP, 'P', '1', '+')
        
        #Variable resultado
        resultado = self.addTemp()
        self.addExp(resultado,'H','','')

        # Variable del numero
        numero = self.addTemp()
        self.getStack(numero, tempP)
        #Verificamos si el numero es negativo
        seguir = self.newLabel()
        self.addIf(numero,'0','>',seguir)
        self.addExp(numero,'0',numero,'-')
        self.setHeap('H',45)
        self.nextHeap()
        #Ponemos el label para seguir
        self.putLabel(seguir)
        # Temporal del numero 
        TmpNumero = self.addTemp()
        self.addExp(TmpNumero,numero,'','')
        # Temporal del numero 2
        TmpNumero2 = self.addTemp()
        self.addExp(TmpNumero2,numero,'','')
        # Caracter del numero
        caracter = self.addTemp()
        self.addExp(caracter,'0','','')

        #Temporal decimal
        mult = self.addTemp()
        self.addExp(mult,'1','','')
        
        #INICIAMOS EL CICLO
        self.putLabel(ciclo1)
        #VALIDACIONES
        self.addIf(TmpNumero, '1', '<', siguiente)

        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(mult,mult,'10','*')
        
        #Aqui iteramos
        self.addExp(TmpNumero, TmpNumero, '10', '/')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo1)

        #Seguimos despues de obtener el multiplicador y reseteamos
        self.putLabel(siguiente)
        self.addExp(mult,mult,'10','/')

        #Empezamos el segundo ciclo
        self.putLabel(ciclo2)

        self.addIf(mult, '1', '<', siguiente2)


        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(TmpNumero2,numero,mult,'/')
        self.addExp(caracter,TmpNumero2,'48','+')
        self.setHeap('H',caracter)
        self.nextHeap()
        self.addExpMod(numero,numero,mult)
        
        #Aqui iteramos
        self.addExp(mult,mult,'10','/')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo2)

        #Empezamos el proceso de pasar los decimales
        self.putLabel(siguiente2)

        #agregamos el punto
        self.setHeap('H','46')
        self.nextHeap()
        self.addExp(TmpNumero,'0','','')
        
        #Empezamos el tercer ciclo
        self.putLabel(ciclo3)

        self.addIf(TmpNumero, '8', '>=', returnLbl)
        self.addIf(numero, '0', '==', returnLbl)


        #Aqui empezamos las operaciones de cada iteracion
        self.addExp(numero,numero,'10','*')
        self.addExp(caracter,numero,'48','+')
        self.setHeap('H',caracter)
        self.nextHeap()
        self.addExpMod(numero,numero,'1')
        
        #Aqui iteramos
        self.addExp(TmpNumero,TmpNumero,'1','+')
        #Aqui regresamos al ciclo
        self.addGoto(ciclo3)

        self.putLabel(returnLbl)
        self.setHeap('H','-1')
        self.nextHeap()
        self.setStack('P', resultado)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempP)
        self.LeaveT(TmpNumero)
        self.LeaveT(TmpNumero2)
        self.LeaveT(numero)
        self.LeaveT(caracter)
        self.LeaveT(mult)
        self.LeaveT(resultado)

    def fCharToString(self):
        if(self.charToString):
            return
        self.charToString = True
        self.enNativas = True

        self.addBeginFunc('charToString')

        # Temporal puntero a Stack
        tempP = self.addTemp()
        self.addExp(tempP, 'P', '1', '+')

        # Temporal puntero a Heap
        tempH = self.addTemp()
        self.getStack(tempH, tempP)

        # Temporal de la posicion del heap
        tmp = self.addTemp()
        self.addExp(tmp,'H','','')

        #Resultado, solo obtenemos el heap
        resultado = self.addTemp()
        self.addExp(resultado, 'H','','')

        #Solo metemos en el heap el char mas un -1
        self.setHeap(tmp,tempH)
        self.nextHeap()
        self.addExp(tmp,tmp,'1','+')
        self.setHeap(tmp,'-1')
        self.nextHeap()

        #regresamos el resultado
        self.setStack('P', resultado)


        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempH)
        self.LeaveT(tempP)
        self.LeaveT(tmp)
        self.LeaveT(resultado)

    def fLength(self):
        if(self.length):
            return
        self.length = True
        self.enNativas = True

        self.addBeginFunc('length')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()
        self.addExp(tempP, 'P', '1', '+')

        # Temporal puntero a Heap
        tempH = self.addTemp()
        self.getStack(tempH, tempP)

        # Temporal para devolver el resultado
        result = self.addTemp()
        self.addExp(result, '0','','')

        # Temporal para comparar
        tempC = self.addTemp()

        self.putLabel(compareLbl)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', returnLbl)

        self.addExp(result, result, '1', '+')

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl)

        self.putLabel(returnLbl)
        self.setStack('P', result)
        self.addEndFunc()
        self.enNativas = False
        self.LeaveT(tempC)
        self.LeaveT(tempH)
        self.LeaveT(tempP)
        self.LeaveT(result)