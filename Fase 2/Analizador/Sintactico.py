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

def p_tipoElemento(t):
    'tipoElemento : TTYPE EQUALS NORMSTRING'

def p_items(t):
    """items : items item
            |  item
    """

def p_item(t):
    'item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION'

def p_valueItem(t):
    """valueItem : NORMSTRING
                |  NUMBER
    """

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

