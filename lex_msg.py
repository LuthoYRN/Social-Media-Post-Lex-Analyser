import ply.lex as lex
import sys

# Define token names
tokens = ['WORD', 'NUMBER', 'WHITESPACE', 'PUNCTUATION', 'HASHTAG', 'NAME', 'ILLEGAL']

# Token rules
def t_WHITESPACE(t):
    r'[ \t]+' 
    return t

def t_HASHTAG(t):
    r'\#[a-zA-Z0-9]+' 
    return t

def t_NAME(t):
    r'\@[a-zA-Z]+'
    return t

def t_WORD(t):
    r'[a-zA-Z]+' 
    return t

def t_NUMBER(t):
    r'\d+'  
    return t

def t_PUNCTUATION(t):
    r'[.,;!?]'
    return t

def t_error(t): #ILLEGAL
    t.type = "ILLEGAL"
    t.value = t.value[0] 
    t.lexer.skip(1)
    return t

# Building the lexer
lexer = lex.lex()

def process_file(input_filename):
    output_filename = input_filename.replace(".msg", ".tkn")

    try:
        with open(input_filename, 'r', encoding='utf-8') as file_in, open(output_filename, 'w', encoding='utf-8') as file_out:
            for line in file_in:
                lexer.input(line)
                while True:
                    tok = lexer.token()
                    if not tok:
                        break
                    token_output = f"{tok.type},{tok.value}"
                    file_out.write(token_output + "\n") 
        print(f"Tokens saved to {output_filename}")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found!")

if len(sys.argv) > 1:
    process_file(sys.argv[1])
else:
    print('Usage: python lex_msg.py <filename>.msg')