from lexer import tokens

names = {}

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    #print("prueba")
    t[0]=t[4]