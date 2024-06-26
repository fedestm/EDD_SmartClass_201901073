reserved = {
    'Elements': 'TELEMENTS',
    'element': 'TELEMENT',
    'type': 'TTYPE',
    'item': 'TITEM',
    'Carnet': 'TCARNET',
    'DPI': 'TDPI',
    'Nombre': 'TNOMBRE',
    'Carrera': 'TCARRERA',
    'Password': 'TPASSWORD',
    'Creditos': 'TCREDITOS',
    'Edad': 'TEDAD',
    'Descripcion': 'TDESCRIPCION',
    'Materia': 'TMATERIA',
    'Fecha': 'TFECHA',
    'Hora': 'THORA',
    'Estado': 'TESTADO',
}

tokens = [
    'LQUESTION', 'RQUESTION', 'DOLAR', 'ID', 'EQUALS', 'QUOTATION_MARKS', 'NUMBER', 'NORMSTRING', 'DATE', 'HOUR'
]+list(reserved.values())

t_LQUESTION = r'\¿'
t_RQUESTION = r'\?'
t_DOLAR = r'\$'
t_EQUALS = r'\='
t_QUOTATION_MARKS = r'\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value=0
    return t

def t_NORMSTRING(t):
    r'\"(\\.|[^"\\])*\"'
    #print("'%s'" % t.value)
    return t

def t_Date(t):
    r'\s+(?=\d{2}(?:\d{2})?/\d{1,2}/\d{1,2}\b)'
    return t

def t_Hora(t):
    r'(?=(?:\b[01]\d|2[0-3]):[0-5]\d\b)'
    return t

t_ignore = ' \t\n\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    t.lexer.skip(1)

import Analizador.ply.lex as lex
import re
lexer=lex.lex(reflags=re.IGNORECASE)