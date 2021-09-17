#IMPORTS
from Export import Salida
#INTRUCCIONES
from Expresiones.AccesoStruct import AccesoStruct
from Instruccion.Structs.decStruct import decStruct
from Instruccion.Structs.AccesoAsignacion import AccesoAsignacion
from Expresiones.Asignar import Asignar
from Instruccion.Variables.Arreglo import Arreglo
from Expresiones.AccesoArray import AccesoArray
from Expresiones.Llamada import Llamada
from Expresiones.Acceso import Acceso
from Instruccion.Print import *
from Instruccion.Variables.Declaracion import *
from Instruccion.Sentencia import *
from Instruccion.Condicional.If import *
from Instruccion.Funciones.Funcion import *
from Instruccion.Funciones.Parametro import *
from Instruccion.Funciones.ReturnST import *
from Instruccion.Structs.CrearStruct import *
from Instruccion.Ciclos.While import *
from Instruccion.Ciclos.For import *
from Instruccion.Ciclos.Break import *
from Instruccion.Ciclos.Continue import *

#EXPRESIONES
from Expresiones.Literal import *
from Expresiones.Aritmetica import *
from Expresiones.Relacional import *
from Expresiones.Logica import *
from Expresiones.Acceso import *
from Expresiones.Rango import *

# LEXICAL ANALYSIS
rw = {
    # GENERAL RW
    "END" : "END",
    "TRUE" : "TRUE",
    "FALSE" : "FALSE",

    # PALBRAS DE FUNCIONES
    "FUNCTION" : "FUNCTION",
    "RETURN" : "RETURN",

    # PALABRAS IFELSE
    "IF" : "IF",
    "ELSE" : "ELSE",
    "ELSEIF" : "ELSEIF",

    # PALABRAS DE WHILE
    "WHILE" : "WHILE",
    "FOR" : "FOR",
    "IN" : "IN",
    "CONTINUE" : "CONTINUE",
    "BREAK": "BREAK",

    # STRUCTS
    "STRUCT" : "STRUCT",
    "MUTABLE" : "MUTABLE",

    # FUNCIONES NATIVAS
    "PRINTLN" : "PRINTLN",
    "PRINT" : "PRINT",

    #TIPOS
    "NOTHING" : "NOTHING",
    "INT64" : "INT64",
    "FLOAT64" : "FLOAT64",
    "BOOL" : "BOOL",
    "CHAR" : "CHAR",
    "STRING" : "STRING",
    "BEGIN" : "BEGIN",
    "LOCAL" : "LOCAL",
    "GLOBAL" : "GLOBAL" 
}

tokens = [
    "ID",

    # VALORES NATIVOS
    "INTLIT",
    "FLOATLIT",
    "STRINGLIT",
    "CHARLIT",

    # SYMBOLS
    # GENERAL SYMBOLS
    "IGUAL",
    "PUNTO",
    "DOSPUNTOS",
    "PUNTOCOMA",
    "COMA",
    "PARABRE",
    "PARCIERRA",
    "CORABRE",
    "CORCIERRA",

    # ARITHMETIC SYMBOLS
    "MAS",
    "MENOS",
    "MULT",
    "DIV",
    "MOD",
    "POW",

    # LOGICAL SYMBOLS
    "AND",
    "OR",
    "NOT",

    # RELATIONAL SYMBOLS
    "MAYOR",
    "MENOR",
    "MAYORIGUAL",
    "MENORIGUAL",
    "IGUALIGUAL",
    "DISTINTO"
] + list(rw.values())

# TOKENS

# SYMBOLS
# GENERAL SYMBOLS
t_IGUAL                 = r'='
t_PUNTO                 = r'\.'
t_DOSPUNTOS             = r':'
t_PUNTOCOMA             = r';'
t_COMA                  = r','
t_PARABRE               = r'\('
t_PARCIERRA             = r'\)'
t_CORABRE               = r'\['
t_CORCIERRA             = r'\]'

# ARITHMETIC SYMBOLS
t_MAS                   = r'\+'
t_MENOS                 = r'-'
t_MULT                  = r'\*'
t_DIV                   = r'/'
t_MOD                   = r'%'
t_POW                   = r'\^'

# LOGICAL SYMBOLS
t_AND                   = r'&&'
t_OR                    = r'\|\|'
t_NOT                   = r'!'

# RELATIONAL SYMBOLS
t_MAYOR                 = r'>'
t_MENOR                 = r'<'
t_MAYORIGUAL            = r'>='
t_MENORIGUAL            = r'<='
t_IGUALIGUAL            = r'=='
t_DISTINTO              = r'!='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = rw.get(t.value.upper(), 'ID')
    return t

def t_FLOATLIT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("ERROR IN PARSE TO FLOAT")
        t.value = 0
    return t

def t_INTLIT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ERROR IN PARSE TO INT")
        t.value = 0
    return t

def t_STRINGLIT(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CHARLIT(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

t_ignore = " \t"

def t_MLCOMMENT(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count("\n")

def t_OLCOMMENT(t):
    r'(\#.*\n)|(\#.*)'
    t.lexer.lineno += 1

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error léxico, El caracter '%s'" % t.value[0] + " no es válido")
    Salida.salida += "Error léxico, El caracter '%s'" % t.value[0] + " no es válido" + "\n"
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'DOSPUNTOS'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALIGUAL', 'DISTINTO'),
    ('left', 'MAYORIGUAL', 'MENORIGUAL', 'MAYOR', 'MENOR'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('left', 'POW'),
    ('left', 'CORABRE', 'PUNTO'),
    ('right', 'UMINUS'),
)

#ANALISIS SINTACTICO

def p_start(t):
    'start : instrucciones'
    t[0] = t[1]
    return t[0]

def p_instrucciones(t):
    '''instrucciones : instrucciones instruccion
                     | instruccion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruccion(t):
    '''instruccion  : printST PUNTOCOMA
                    | declaracionST PUNTOCOMA
                    | decArrayST PUNTOCOMA
                    | decFuncionST PUNTOCOMA
                    | llamadaST PUNTOCOMA
                    | ifST PUNTOCOMA
                    | whileST PUNTOCOMA
                    | forST PUNTOCOMA
                    | breakST PUNTOCOMA
                    | continueST PUNTOCOMA
                    | returnST PUNTOCOMA
                    | crearStructST PUNTOCOMA
                    | accesoAsignacionST PUNTOCOMA'''
    t[0] = t[1]

# SENTENCIA
def p_sentencia(t):
    '''sentencia : instrucciones'''
    t[0] = Sentencia(t[1], t.lineno(1), t.lexpos(0))

# FUNCTION ST
def p_decFuncionST(t):
    '''decFuncionST : FUNCTION ID PARABRE PARCIERRA sentencia END
                    | FUNCTION ID PARABRE listaParametrosST PARCIERRA sentencia END'''
    if len(t) == 7:
        t[0] = Funcion(t[2], [], t[5], t.lineno(1), t.lexpos(1))
    else:
        t[0] = Funcion(t[2], t[4], t[6], t.lineno(1), t.lexpos(1))

def p_listaParametrosST(t):
    '''listaParametrosST : listaParametrosST COMA parametroST
                         | parametroST'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

def p_parametroST(t):
    '''parametroST : ID DOSPUNTOS DOSPUNTOS tipoST 
                   | ID'''
    if len(t) == 2:
        t[0] = Parametro(t[1], None, t.lineno(1), t.lexpos(1))
    else:
        if t.slice[1].type == "ID":
            t[0] = Parametro(t[1], t[4], t.lineno(1), t.lexpos(1))
        else:
            t[0] = t[1]
        
# STRUCTS
# CREATE STRUCT
def p_crearStructST(t):
    '''crearStructST : STRUCT ID listaStructST END
                     | MUTABLE STRUCT ID listaStructST END'''
    if len(t) == 5:
        t[0] = CrearStruct(t[2], t[3], True, t.lineno(1), t.lexpos(1))
    else:
        t[0] = CrearStruct(t[3], t[4], False, t.lineno(1), t.lexpos(1))

def p_listaStructST(t):
    '''listaStructST : listaStructST ID PUNTOCOMA
                     | listaStructST ID DOSPUNTOS DOSPUNTOS tipoST PUNTOCOMA
                     | ID DOSPUNTOS DOSPUNTOS tipoST PUNTOCOMA
                     | ID PUNTOCOMA'''
    if len(t) == 3:
        t[0] = [Parametro(t[1], None, t.lineno(1), t.lexpos(1))]
    elif len(t) == 6:
        t[0] = [Parametro(t[1], t[4], t.lineno(1), t.lexpos(1))]
    elif len(t) == 4:
        t[1].append(Parametro(t[2], None, t.lineno(1), t.lexpos(1)))
        t[0] = t[1]
    else:
        t[1].append(Parametro(t[2], t[5], t.lineno(1), t.lexpos(1)))
        t[0] = t[1]

# ASSIGN ACCESS
def p_AccesoAsignacionST(t):
    'accesoAsignacionST : accesoST IGUAL expresion'
    t[0] = AccesoAsignacion(t[1], t[3], t.lineno(1), t.lexpos(1))


# DECLARACION ARRAY
def p_decArray(t):
    '''decArrayST : expresion listaPosicionesST IGUAL expresion'''
    t[0] = Arreglo(t[1], t[2], t[4],  t.lineno(2), t.lexpos(2))

def p_listaPosicionesST(t):
    '''listaPosicionesST : listaPosicionesST CORABRE expresion CORCIERRA
                         | CORABRE expresion CORCIERRA'''
    if len(t) == 4:
        t[0] = [t[2]]
    else:
        t[1].append(t[3])
        t[0] = t[1]
    

# DECLARATION ST
def p_declaracion(t):
    '''declaracionST : ID IGUAL expresion
                     | ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipoST
                     | LOCAL ID IGUAL expresion
                     | GLOBAL ID IGUAL expresion
                     | LOCAL ID
                     | GLOBAL ID'''
    if len(t) == 4:
        t[0] = Declaracion(t[1], t[3], None, TipoDeclaracion.DEFAULT,  t.lineno(2), t.lexpos(2))
    elif len(t) == 7:
        t[0] = Declaracion(t[1], t[3], t[6], TipoDeclaracion.DEFAULT,  t.lineno(2), t.lexpos(2))
    elif len(t) == 5:
        if t.slice[1].type == "LOCAL":
            t[0] = Declaracion(t[2], t[4], None, TipoDeclaracion.LOCAL,  t.lineno(2), t.lexpos(2))
        else:
            t[0] = Declaracion(t[2], t[4], None, TipoDeclaracion.GLOBAL, t.lineno(2), t.lexpos(2))
    else:
        if t.slice[1].type == "LOCAL":
            t[0] = Declaracion(t[2], None, None, TipoDeclaracion.LOCAL,  t.lineno(2), t.lexpos(2))
        else:
            t[0] = Declaracion(t[2], None, None, TipoDeclaracion.GLOBAL,  t.lineno(2), t.lexpos(2))

# PRINT ST
def p_printlnST(t):
    '''printST  : PRINTLN PARABRE listaExpresionesST PARCIERRA
                | PRINTLN PARABRE PARCIERRA'''
    if len(t) == 5:
        t[0] = Print(t[3], t.lineno(1), t.lexpos(0), True)
    else:
        t[0] = Print([Literal("", Tipo.STRING, t.lineno(1), t.lexpos(0))], t.lineno(1), t.lexpos(0), True)

def p_printST(t):
    '''printST  : PRINT PARABRE listaExpresionesST PARCIERRA
                | PRINT PARABRE PARCIERRA'''
    if len(t) == 5:
        t[0] = Print(t[3], t.lineno(1), t.lexpos(0), False)
    else:
        t[0] = Print([Literal("", Tipo.STRING, t.lineno(1), t.lexpos(0))], t.lineno(1), t.lexpos(0), False)

def p_listaExpresionesST(t):
    '''listaExpresionesST : listaExpresionesST COMA expresion
                          | expresion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

# IF ST
def p_ifST(t):
    '''ifST : IF expresion sentencia END
            | IF expresion sentencia ELSE sentencia END
            | IF expresion sentencia listaElseIf END'''
    if len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 7:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])

def p_listaElseIf(t):
    '''listaElseIf  : ELSEIF expresion sentencia
                    | ELSEIF expresion sentencia ELSE sentencia
                    | ELSEIF expresion sentencia listaElseIf'''
    if len(t) == 4:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])

# WHILE ST
def p_forST(t):
    'forST : FOR ID IN expresion sentencia END'
    t[0] = For(t[2], t[4], t[5], t.lineno(1), t.lexpos(1))

# FOR ST
def p_whileST(t):
    'whileST : WHILE expresion sentencia END'
    t[0] = While(t[2], t[3], t.lineno(1), t.lexpos(1))

# BREAK ST
def p_break(t):
    'breakST : BREAK'
    t[0] = Break(t.lineno(1), t.lexpos(1))

# CONTINUE ST
def p_continue(t):
    'continueST : CONTINUE'
    t[0] = Continue(t.lineno(1), t.lexpos(1))

# RETURN ST
def p_returnST(t):
    '''returnST : RETURN
                | RETURN expresion'''
    if len(t) == 2:
        t[0] = ReturnST(Literal("Nothing",Tipo.NOTHING,t.lineno(1), t.lexpos(1)), t.lineno(1), t.lexpos(1))
    else:
        t[0] = ReturnST(t[2], t.lineno(1), t.lexpos(1))

# LLAMADA A FUNCION ST
def p_llamadaST(t):
    '''llamadaST : ID PARABRE PARCIERRA
                 | ID PARABRE listaExpresionesST PARCIERRA
                 | STRING PARABRE listaExpresionesST PARCIERRA
                 | ID NOT PARABRE listaExpresionesST PARCIERRA'''
    if len(t) == 4:
        t[0] = Llamada(t[1], [], t.lineno(1), t.lexpos(1))
    elif len(t) == 5:
        if t.slice[1].type == "ID":
            t[0] = Llamada(t[1], t[3], t.lineno(1), t.lexpos(1))
        else:
            t[0] = Llamada("string", t[3], t.lineno(1), t.lexpos(1))
    else:
        t[0] = Llamada(t[1] + "!", t[4], t.lineno(1), t.lexpos(1))

# EXPRESION
def p_expresion(t):
    '''expresion   : MENOS expresion %prec UMINUS
                    | NOT expresion %prec UMINUS
                    
                    | expresion MAS expresion
                    | expresion MENOS expresion
                    | expresion MULT expresion
                    | expresion DIV expresion
                    | expresion MOD expresion
                    | expresion POW expresion

                    | expresion MAYOR expresion
                    | expresion MENOR expresion
                    | expresion MAYORIGUAL expresion
                    | expresion MENORIGUAL expresion
                    | expresion IGUALIGUAL expresion
                    | expresion DISTINTO expresion
                    
                    | expresion OR expresion
                    | expresion AND expresion

                    | expresion CORABRE expresion CORCIERRA
                    | expresion CORABRE DOSPUNTOS CORCIERRA
                    | expresion DOSPUNTOS expresion

                    | finalExp'''
    if len(t) == 2: t[0] = t[1]
    elif len(t) == 3:
        # UMINUS
        if t[1] == "-":
            t[0] = Aritmetica(Literal(0, Tipo.INT, t.lineno(1), t.lexpos(0)), t[2], OpAritmetico.MINUS, t.lineno(1), t.lexpos(0))
        else:
            t[0] = Logica(t[2], t[2], OpLogica.NOT, t.lineno(1), t.lexpos(0))
    elif len(t) == 4:
        if t[2] == "+":
            t[0] = Aritmetica(t[1], t[3], OpAritmetico.PLUS, t.lineno(2), t.lexpos(0))
        elif t[2] == "-":
            t[0] = Aritmetica(t[1], t[3], OpAritmetico.MINUS, t.lineno(2), t.lexpos(0))
        elif t[2] == "*":
            t[0] = Aritmetica(t[1], t[3], OpAritmetico.TIMES, t.lineno(2), t.lexpos(0))
        elif t[2] == "/":
            t[0] = Aritmetica(t[1], t[3], OpAritmetico.DIV, t.lineno(2), t.lexpos(0))
        elif t[2] == "%":
            t[0] = Aritmetica(t[1], t[3], OpAritmetico.MOD, t.lineno(2), t.lexpos(0))
        elif t[2] == "^":
            t[0] = Aritmetica(t[1], t[3], OpAritmetico.POW, t.lineno(2), t.lexpos(0))
        elif t[2] == ">":
            t[0] = Relacional(t[1], t[3], OpRelacional.GREATER, t.lineno(2), t.lexpos(2))
        elif t[2] == "<":
            t[0] = Relacional(t[1], t[3], OpRelacional.LESS, t.lineno(2), t.lexpos(2))
        elif t[2] == ">=":
            t[0] = Relacional(t[1], t[3], OpRelacional.GREATEREQUAL, t.lineno(2), t.lexpos(2))
        elif t[2] == "<=":
            t[0] = Relacional(t[1], t[3], OpRelacional.LESSEQUAL, t.lineno(2), t.lexpos(2))
        elif t[2] == "==":
            t[0] = Relacional(t[1], t[3], OpRelacional.EQUALSEQUALS, t.lineno(2), t.lexpos(2))
        elif t[2] == "!=":
            t[0] = Relacional(t[1], t[3], OpRelacional.DISTINT, t.lineno(2), t.lexpos(2))
        elif t[2] == "||":
            t[0] = Logica(t[1], t[3], OpLogica.OR, t.lineno(2), t.lexpos(2))
        elif t[2] == "&&":
            t[0] = Logica(t[1], t[3], OpLogica.AND, t.lineno(2), t.lexpos(2))
        elif t[2] == ":":
            t[0] = Rango(t[1], t[3], t.lineno(2), t.lexpos(2))
    else:
        if t[3] == ":":
            t[0] = AccesoArray(t[1], Rango(Literal(1, Tipo.BEGIN, t.lineno(1), t.lexpos(0)), Literal(-1, Tipo.END, t.lineno(1), t.lexpos(0)), t.lineno(2), t.lexpos(2)), t.lineno(1), t.lexpos(1))
        else:
            t[0] = AccesoArray(t[1], t[3], t.lineno(1), t.lexpos(1))

def p_finalExp(t):
    '''finalExp : PARABRE expresion PARCIERRA
                | INTLIT
                | FLOATLIT
                | STRINGLIT
                | CHARLIT
                | TRUE
                | FALSE
                | ID
                | NOTHING
                | llamadaST
                | accesoST
                | tipoST
                | CORABRE listaExpresionesST CORCIERRA'''
    if len(t) == 2:
        if t.slice[1].type == "INTLIT":
            t[0] = Literal(int(t[1]), Tipo.INT, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "FLOATLIT":
            t[0] = Literal(float(t[1]), Tipo.FLOAT, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "STRINGLIT":
            t[0] = Literal(str(t[1]), Tipo.STRING, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "CHARLIT":
            t[0] = Literal(str(t[1]), Tipo.CHAR, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "END":
            t[0] = Literal(-1, Tipo.END, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "TRUE":
            t[0] = Literal(True, Tipo.BOOLEAN, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "FALSE":
            t[0] = Literal(False, Tipo.BOOLEAN, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "ID":
            t[0] = Acceso(t[1], t.lineno(1), t.lexpos(1))
        elif t.slice[1].type == "NOTHING":
            t[0] = Literal(None, Tipo.NOTHING, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "llamadaST" or t.slice[1].type == "accesoST":
            t[0] = t[1]
        elif t.slice[1].type == "tipoST":
            t[0] = t[1]
    else:
        if t.slice[2].type == "listaExpresionesST":
            t[0] = Literal(t[2], Tipo.ARRAY, t.lineno(1), t.lexpos(0))
        else:
            t[0] = t[2]

def p_accesoST(t):
    '''accesoST : expresion PUNTO ID'''
    t[0] = AccesoStruct(t[1], t[3], t.lineno(2), t.lexpos(2))

#TIPO ST
def p_tipoST(t):
    '''tipoST : INT64
              | FLOAT64
              | BOOL
              | CHAR
              | STRING
              | ID'''
    if t.slice[1].type == "INT64":
        t[0] = Tipo.INT
    elif t.slice[1].type == "FLOAT64":
        t[0] = Tipo.FLOAT
    elif t.slice[1].type == "BOOL":
        t[0] = Tipo.BOOLEAN
    elif t.slice[1].type == "CHAR":
        t[0] = Tipo.CHAR
    elif t.slice[1].type == "STRING":
        t[0] = Tipo.STRING
    elif t.slice[1].type == "ID":
        t[0] = t[1]

def p_error(t):
    print(t)
    Salida.salida += str(t) + "\n"
    print("Error sintáctico en '%s'" % t.value)
    Salida.salida += "Error sintáctico en '%s'" % t.value + "\n"

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    # f = open("./input.jl", "r")
    # input = f.read()
    return parser.parse(input)