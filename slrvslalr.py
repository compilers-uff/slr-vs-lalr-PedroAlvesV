from ply import lex, yacc
import sys

if len(sys.argv) < 2:
  print('Missing parser parameter')
  exit()

parser = sys.argv[1].upper()

if parser != 'SLR' and parser != 'LALR':
  print('Invalid parser')
  exit()

tokens = ['ID','MULT','EQ']

t_ID   = r'[a-zA-Z_][a-zA-Z_]*'
t_MULT = r'\*'
t_EQ   = r'='

def t_error(t):
  print('Invalid character', t.value[0])
  t.lexer.skip(1)

lex.lex()

def p_S_1(p):
  'S : L EQ R'
  
def p_S_2(p):
  'S : R'

def p_L_1(p):
  'L : MULT R'

def p_L_2(p):
  'L : ID'

def p_R(p):
  'R : L'

def p_error(p):
  print('Syntax error', p.value)

yacc.yacc(parser)