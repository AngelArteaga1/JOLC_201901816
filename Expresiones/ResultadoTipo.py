from Abstracto.Return import *
from Export import Salida

def getTipo(leftType, rightType, Operador, linea, columna):
    if Operador == OpAritmetico.PLUS:
        if rightType == Tipo.INT and leftType == Tipo.INT:
            return Tipo.INT
        elif rightType == Tipo.INT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.INT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        else:
            print("Error Semantico: no es posible realizar la suma de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la suma de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna)
            Salida.errores.append(Error("Error Semantico: no es posible realizar la suma de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpAritmetico.MINUS:
        if rightType == Tipo.INT and leftType == Tipo.INT:
            return Tipo.INT
        elif rightType == Tipo.INT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.INT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        else:
            print("Error Semantico: no es posible realizar la resta de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la resta de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la resta de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpAritmetico.TIMES:
        if rightType == Tipo.INT and leftType == Tipo.INT:
            return Tipo.INT
        elif rightType == Tipo.INT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.INT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        elif (rightType == Tipo.STRING and leftType == Tipo.STRING) or (leftType == Tipo.STRING and rightType == Tipo.STRING):
            return Tipo.STRING
        else:
            print("Error Semantico: no es posible realizar la multiplicación de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la multiplicación de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la multiplicación de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpAritmetico.DIV:
        if rightType == Tipo.INT and leftType == Tipo.INT:
            return Tipo.FLOAT
        elif rightType == Tipo.INT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.INT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        else:
            print("Error Semantico: no es posible realizar la división de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la división de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la división de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpAritmetico.POW:
        if rightType == Tipo.INT and leftType == Tipo.INT:
            return Tipo.INT
        elif rightType == Tipo.INT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.INT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        elif leftType == Tipo.STRING and rightType == Tipo.INT:
            return Tipo.STRING
        else:
            print("Error Semantico: no es posible realizar la potencia de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la potencia de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la potencia de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpAritmetico.MOD:
        if rightType == Tipo.INT and leftType == Tipo.INT:
            return Tipo.INT
        elif rightType == Tipo.INT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.INT:
            return Tipo.FLOAT
        elif rightType == Tipo.FLOAT and leftType == Tipo.FLOAT:
            return Tipo.FLOAT
        else:
            print("Error Semantico: no es posible realizar la resta de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la resta de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la resta de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpRelacional.GREATER:
        if leftType == Tipo.INT and rightType == Tipo.FLOAT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.FLOAT and rightType == Tipo.INT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.FLOAT and rightType == Tipo.FLOAT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.INT and rightType == Tipo.INT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.STRING and rightType == Tipo.STRING:
            return Tipo.BOOLEAN
        else:
            print("Error Semantico: no es posible realizar la comparacion '>' de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la comparacion '>' de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la comparacion '>' de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpRelacional.LESS:
        if leftType == Tipo.INT and rightType == Tipo.FLOAT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.FLOAT and rightType == Tipo.INT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.FLOAT and rightType == Tipo.FLOAT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.INT and rightType == Tipo.INT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.STRING and rightType == Tipo.STRING:
            return Tipo.BOOLEAN
        else:
            print("Error Semantico: no es posible realizar la comparacion '<' de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la comparacion '<' de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la comparacion '<' de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpRelacional.GREATEREQUAL:
        if leftType == Tipo.INT and rightType == Tipo.FLOAT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.FLOAT and rightType == Tipo.INT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.FLOAT and rightType == Tipo.FLOAT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.INT and rightType == Tipo.INT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.STRING and rightType == Tipo.STRING:
            return Tipo.BOOLEAN
        else:
            print("Error Semantico: no es posible realizar la comparacion '>=' de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la comparacion '>=' de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la comparacion '>=' de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpRelacional.LESSEQUAL:
        if leftType == Tipo.INT and rightType == Tipo.FLOAT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.FLOAT and rightType == Tipo.INT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.FLOAT and rightType == Tipo.FLOAT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.INT and rightType == Tipo.INT:
            return Tipo.BOOLEAN
        elif leftType == Tipo.STRING and rightType == Tipo.STRING:
            return Tipo.BOOLEAN
        else:
            print("Error Semantico: no es posible realizar la comparacion '<=' de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: no es posible realizar la comparacion '<=' de tipo '" + str(rightType) + "' y '" + str(leftType) + "', linea: " + str(linea) + " columna: " + str(columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no es posible realizar la comparacion '<=' de tipo '" + str(rightType) + "' y '" + str(leftType) + "'", linea, columna))
            return Tipo.NOTHING
    elif Operador == OpRelacional.EQUALSEQUALS:
        return Tipo.BOOLEAN
    elif Operador == OpRelacional.DISTINT:
        return Tipo.BOOLEAN
    