import ply.lex as lex

tokens = [
   'OPERANDS'
]



def t_OPERANDS(t):
    
    r'(\+\+|-=|\+=|/=|%=|\*=|&=|\^=|&\^=|<<=|>>=|!=|==|<=|>=|&&|\|\||<<|>>|->|\.\.\.|::=|\{|\}|\[|\]|\(|\)|\+|-|\*|/|%|!|&|\||\^|&\^|;|:|\.|~)'    
    return t


t_ignore  = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

def getLexer():
  return lex.lex()