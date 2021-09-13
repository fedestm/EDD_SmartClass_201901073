from Analizador.Lexer import tokens

names = {}

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print("prueba")
    t[0]=t[4]

def p_elementos_group(t):
    """elementos : elementos elemento
                |  elemento
    """

def p_elemento(t):
    'elemento : LQUESTION TELEMENT tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'

def p_tipoElemento(t):
    'tipoElemento : TTYPE EQUALS NORMSTRING'

def p_items(t):
    """items : items item
            |  item
    """

def p_item(t):
    'item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION'
    print("\n")
    print(t[3])
    print(t[5])

def p_valueItem(t):
    """valueItem : NORMSTRING
                |  NUMBER
    """
    t[0] = t[1]

def p_TipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
    """
    t[0] = t[1]

def p_error(t):
    print("Error de sintaxis '%s'" % t.value)

import Analizador.ply.yacc as yacc
parser = yacc.yacc()