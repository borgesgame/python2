#------------------------------------------------------------------------#
#           GERA LISTAS                                                  #
#           Python 3.8.1 14-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#
import random

def lista_grande(n):
        
        lista = []
        for i in range(n):
            lista.append(random.randrange(0,n))

        return lista
