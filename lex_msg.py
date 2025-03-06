import ply.lex as lex
import ply.yacc as yacc

tokens = ['WORD','NUMBER','WHITESPACE','PUNCTUATION','HASHTAG','NAME','ILLEGAL']

def t_WHITESPACE(t):
    r'[ \t]+'
    t.type = 'WHITESPACE'
    return t

def t_HASHTAG(t):
    r'\#[a-zA-Z0-9]+'
    t.type = 'HASHTAG'
    return t

def t_NAME(t):
    r'\@[a-zA-Z0-9]+'
    t.type = 'NAME'
    return t

def t_WORD(t):
    r'[a-zA-Z]+'
    t.type = 'WORD'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PUNCTUATION(t):
    r'[.,;!?]+'
    t.type = 'PUNCTUATION'
    return t


def t_error(t):
    t.type = 'ILLEGAL'
    t.lexer.skip(1)
    return t

lexer = lex.lex()

while True:
    try:
        s = input('text> ')
    except:
        break
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok.type,',', tok.value,sep="")