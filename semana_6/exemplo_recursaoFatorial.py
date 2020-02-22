#------------------------------------------------------------------------#
#           RECURSAO                                                     #
#           Python 3.8.1 14-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def fatorial(n):
    if n < 1:                       # Base da recursao
        return 1
    else:
        return n * fatorial(n -1)   #Chamada Recursiva

'''
import pytest

@pytest.mark.parametrize("entrada,esperado",[
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (4,24),
    (5,120)
    ])

def testa_fatorial(entrada,esperado):
    assert fatorial(entrada) == esperado
'''
