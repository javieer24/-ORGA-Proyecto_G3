# Lista de tokens
reservadas = {
    # Palabras reservadas
    'new_print':'NEWPRINT',
    'end_print':'ENDPRINT',
    'set_print_x':'SET_PRINT_X',
    'set_print_o':'SET_PRINT_O',
    'set_print_triangulo':'SET_PRINT_TRIANGULO',
    'set_print_estrella':'SET_PRINT_ESTRELLA',
    # Colores
    'cyan':'T_CYAN',
    'magenta':'T_MAGENTA',
    'amarillo':'T_AMARILLO',
    'negro':'T_NEGRO',
}

tokens = [
    # Valores
    'ENTERO',
    'ID',
    # Simbolos
    'PUNTOCOMA',
    'COMA',
    'PARIZQ',
    'PARDER',
] + list(reservadas.values())

# Definición de reglas de la gramática

t_NEWPRINT = r'new_print'
t_ENDPRINT = r'end_print'
t_SET_PRINT_X = r'set_print_x'
t_SET_PRINT_O = r'set_print_o'
t_SET_PRINT_TRIANGULO = r'set_print_triangulo'
t_SET_PRINT_ESTRELLA = r'set_print_estrella'

t_T_CYAN = r'cyan'
t_T_NEGRO = r'negro'
t_T_AMARILLO = r'amarillo'
t_T_MAGENTA = r'magenta'
t_PUNTOCOMA = r';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\#.*'

def calcular_columna(t):
    # Esta función calcula la columna basada en el desplazamiento léxico (lexpos)
    # y el texto de entrada
    texto = t.lexer.lexdata
    lexpos = t.lexer.lexpos
    line_start = texto.rfind('\n', 0, lexpos) + 1
    return lexpos - line_start + 1

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)

# Esquema de traducción

from Interprete.Enums import *
from Interprete.Impresion import *

def p_init(t) :
    'init            : L_SENT'
    t[0] = t[1]

def p_LSENT(t) :
    '''L_SENT : L_SENT SENT
              | SENT
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
         t[0] = [t[1]]


def p_SENT(t) :
    '''SENT : NEWPRINT ID PUNTOCOMA L_SENT_PRINT ENDPRINT PUNTOCOMA
    '''
    id = t[2]
    sentencias = t[4]

    t[0] = Impresion(id, sentencias)

def p_L_SENT_PRINT(t) :
    '''L_SENT_PRINT : L_SENT_PRINT SENT_PRINT
                    | SENT_PRINT
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_SENT_PRINT(t) :
    '''SENT_PRINT : SET_PRINT PARIZQ ENTERO COMA ENTERO COMA COLOR PARDER PUNTOCOMA
    '''

    figura = t[1]
    fila = t[3]
    columna = t[5]
    color = t[7]

    t[0] = Instruccion(figura, color, fila, columna)

def p_COLOR(t) :
    '''COLOR : T_CYAN
             | T_MAGENTA
             | T_AMARILLO
             | T_NEGRO
    '''
    t[0] = COLOR.BLANCO

    if t[1] == 'cyan': t[0] = COLOR.CYAN
    elif t[1] == 'magenta': t[0] = COLOR.MAGENTA
    elif t[1] == 'amarillo': t[0] = COLOR.YELLOW
    elif t[1] == 'negro': t[0] = COLOR.BLACK

def p_SET_PRINT(t) :
    '''SET_PRINT : SET_PRINT_X
                | SET_PRINT_O
                | SET_PRINT_TRIANGULO
                | SET_PRINT_ESTRELLA
    '''
    t[0] = FIGURA.VACIO

    if t[1] == 'set_print_x':
        t[0] = FIGURA.EQUIS
    if t[1] == 'set_print_o':
        t[0] = FIGURA.CIRCULO
    if t[1] == 'set_print_triangulo':
        t[0] = FIGURA.TRIANGULO
    if t[1] == 'set_print_estrella':
        t[0] = FIGURA.ESTRELLA


def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")

# Ejecucion

import ply.lex as Lex
import ply.yacc as yacc

lexer = Lex.lex()
parser = yacc.yacc(debug=True)

def parse(input) :
    return parser.parse(input)