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
    #print("\n")
    #print(t[3])
    #print(t[5])
    #print("\n")
    

def p_tipoElemento(t):
    'tipoElemento : TTYPE EQUALS NORMSTRING'
    t[0] = t[3].replace("\"","")

def p_items(t):
    """items : items item
            |  item
    """
    try:
        t[1].append(t[2])
        t[0] = t[1]
    except:
        t[0] = []
        t[0].append(t[1])

def p_item(t):
    'item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION'

    #Se colocan dichas posiciones ya que tipeItem esta en la posicion 3 y valueItem en 5
    #Esos son los unicos valores que nos interesan
    #Y siempre se igualan al no terminal que esta asociado, por ejemplo item esta en t[0]
    obj = {
        t[3].replace("'",""):t[5]
    }
    
    t[0] = obj

    #Prueba
    #print(t[3])
    #print(t[5])
    

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