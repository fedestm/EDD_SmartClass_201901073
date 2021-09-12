from lexer import tokens

names = {}

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    #print("prueba")
    t[0]=t[4]

def p_elementos_group(t):
    """elementos : elementos elemento
                |  elemento
    """

def p_elemento(t):
    'elemento : LQUESTION TELEMENT tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'

