import ply.lex as lex
import re

tokens = [
    'ID',
    'DIGIT',
    'OPERANDS',
    'FUNCTION',
    'STR',
    'CARRIAGERETURN',
    'SPACE',
    'KEYWORD'
]

def t_KEYWORD(t):
    r"(break|default|func|interface|select|case|defer|go|map|struct|chan|else|goto|package|switch|const|fallthrough|if|range|type|continue|for|import|return|var)"
    #coincidencia = re.search(patron, t)

    # Si hay una coincidencia, devuelve True. De lo contrario, devuelve False.
    return t

def t_FUNCTION(t):
    
    r'[a-zA-Z_][a-zA-Z_0-9]\(.\)'
    return t

def t_ID(t):
    
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_DIGIT(t):
    
    r'\s+\d+\s+'
    return t

def t_OPERANDS(t):
    
    r'\s*(\+\+|=|-=|\+=|/=|%=|\=|&=|\^=|&\^=|<<=|>>=|!=|==|<=|>=|&&|\|\||<<|>>|->|\.\.\.|::=|\{|\}|\[|\]|\(|\)|\+|-|\|/|%|!|&|\||\^|&\^|;|:|\.|~)+\s*'    
    return t

def t_STR(t):
    
    r'[\"|\'].*[\"|\']'
    return t

def t_CARRIAGERETURN(t):
    
    r'\n'
    return t

def t_SPACE(t):
    
    r'\s'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

def getLexer():
  return lex.lex()
