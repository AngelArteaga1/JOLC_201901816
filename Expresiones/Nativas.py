from Instruccion.Funciones.Parametro import Parametro
from Abstracto.Return import Return
from Export import Salida


from Abstracto.Return import *
import math

def log10(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if not(valor.tipo == Tipo.INT or valor.tipo == Tipo.FLOAT):
        print("Error Semantico: el parametro de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el parametro de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el parametro de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    if valor.val <= 0:
        print("Error Semantico: el parametro de la funcion '" + str(funcion.id) + "' no puede ser negativo o nulo, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el parametro de la funcion '" + str(funcion.id) + "' no puede ser negativo o nulo, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el parametro de la funcion '" + str(funcion.id) + "' no puede ser negativo o nulo", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(math.log10(valor.val), Tipo.FLOAT)

def log(funcion, ambito):
    if len(funcion.parametros) != 2:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    base = funcion.parametros[0].exec(ambito)
    valor = funcion.parametros[1].exec(ambito)
    if not(base.tipo == Tipo.INT or base.tipo == Tipo.FLOAT):
        print("Error Semantico: la base de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(base.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la base de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(base.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la base de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(base.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    if not(valor.tipo == Tipo.INT or valor.tipo == Tipo.FLOAT):
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(base.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(base.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(base.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(math.log(valor.val, base.val), Tipo.FLOAT)

def sin(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if not(valor.tipo == Tipo.INT or valor.tipo == Tipo.FLOAT):
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(math.sin(valor.val), Tipo.FLOAT)

def cos(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if not(valor.tipo == Tipo.INT or valor.tipo == Tipo.FLOAT):
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(math.cos(valor.val), Tipo.FLOAT)

def tan(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if not(valor.tipo == Tipo.INT or valor.tipo == Tipo.FLOAT):
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(math.tan(valor.val), Tipo.FLOAT)

def sqrt(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if not(valor.tipo == Tipo.INT or valor.tipo == Tipo.FLOAT):
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return(0, Tipo.NOTHING)
    elif valor.val < 0:
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser negativo', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser negativo', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser negativo'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(math.sqrt(valor.val), Tipo.FLOAT)

def parse(funcion, ambito):
    if len(funcion.parametros) != 2:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    tipo = funcion.parametros[0]
    valor = funcion.parametros[1].exec(ambito)
    if valor.tipo != Tipo.STRING:
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    try:
        if tipo == Tipo.INT:
            return Return(int(valor.val), Tipo.INT)
        elif tipo == Tipo.FLOAT:
            return Return(float(valor.val), Tipo.FLOAT)
        else:
            print("Error Semantico: el tipo de la funcion '" + str(funcion.id) + "' no es un tipo numerico, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
            Salida.salida += "Error Semantico: el tipo de la funcion '" + str(funcion.id) + "' no es un tipo numerico, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el tipo de la funcion '" + str(funcion.id) + "' no es un tipo numerico", funcion.linea, funcion.columna))
            return Return("Nothing", Tipo.NOTHING)
    except:
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede se puede convertir a " + str(tipo) + ", linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede se puede convertir a " + str(tipo) + ", linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede se puede convertir a " + str(tipo), funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)


def trunc(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if not(valor.tipo == Tipo.FLOAT or valor.tipo == Tipo.INT):
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(math.trunc(valor.val), Tipo.INT)

def Float(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if valor.tipo != Tipo.INT:
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(float(valor.val), Tipo.FLOAT)

def string(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if valor.tipo == Tipo.ARRAY:
        return Return(str(arrayToString(valor)), Tipo.STRING)
    if valor.tipo == Tipo.STRUCT:
        return Return(str(structToString(valor)), Tipo.STRING)
    else:
        return Return(str(valor.val), Tipo.STRING)

def arrayToString(valor):
    array = []
    for item in valor.val:
        if item.tipo == Tipo.ARRAY:
            array.append(arrayToString(item))
            continue
        elif item.tipo == Tipo.STRUCT:
            array.append(structToString(item))
            continue
        array.append(item.val)
    return array

def structToString(valor):
    struct = {}
    for item in valor.val:
        if valor.val[item].tipo == Tipo.STRUCT:
            struct[item] = structToString(valor.val[item])
            continue
        elif valor.val[item].tipo == Tipo.ARRAY:
            struct[item] = arrayToString(valor.val[item])
            continue
        struct[item] = valor.val[item].val
    return struct

def typeof(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if valor.tipo == Tipo.INT:
        return Return("Int64", Tipo.STRING)
    elif valor.tipo == Tipo.FLOAT:
        return Return("Float64", Tipo.STRING)
    elif valor.tipo == Tipo.BOOLEAN:
        return Return("Bool", Tipo.STRING)
    elif valor.tipo == Tipo.CHAR:
        return Return("Char", Tipo.STRING)
    elif valor.tipo == Tipo.STRING:
        return Return("String", Tipo.STRING)
    elif valor.tipo == Tipo.ARRAY:
        return Return("Array", Tipo.STRING)
    elif valor.tipo == Tipo.STRUCT:
        return Return("Struct", Tipo.STRING)
    else:
        return Return("Nothing", Tipo.STRING)

def push(funcion, ambito):
    if len(funcion.parametros) != 2:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    array = funcion.parametros[0].exec(ambito)
    valor = funcion.parametros[1].exec(ambito)
    if array.tipo != Tipo.ARRAY:
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(array.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(array.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(array.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    array.val.append(valor)
    return Return(array.val, Tipo.ARRAY)

def Pop(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    array = funcion.parametros[0].exec(ambito)
    if array.tipo != Tipo.ARRAY:
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(array.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(array.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(array.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = array.val.pop()
    return Return(valor.val, valor.tipo)

def length(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if not(valor.tipo == Tipo.STRING or valor.tipo == Tipo.ARRAY):
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(len(valor.val), Tipo.INT)

def uppercase(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if valor.tipo != Tipo.STRING:
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return(0, Tipo.NOTHING)
    return Return(valor.val.upper(), Tipo.STRING)

def lowercase(funcion, ambito):
    if len(funcion.parametros) != 1:
        print("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(funcion.id) + "' no tiene la cantidad de parametros correctos", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    valor = funcion.parametros[0].exec(ambito)
    if valor.tipo != Tipo.STRING:
        print("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna))
        Salida.salida += "Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "', linea: " + str(funcion.linea) + " columna: " + str(funcion.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: el valor de la funcion '" + str(funcion.id) + "' no puede ser de tipo '" + str(valor.tipo) + "'", funcion.linea, funcion.columna))
        return Return("Nothing", Tipo.NOTHING)
    return Return(valor.val.lower(), Tipo.STRING)