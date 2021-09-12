reserved = {
    'Elements': 'TELEMENTS',
    'element': 'TELEMENT',
    'type': 'TTYPE',
    'item': 'TITEM',
    'Carnet': 'TCARNET',
    'Dpi': 'TDPI',
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
t_QUOTATIONS_MARKS = r'\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t