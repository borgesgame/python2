#------------------------------------------------------------------------#
#           BUSCA SEQUENCIAL -  ELEMENTO LISTA                           #
#           Python 3.8.1 14-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def busca(lista,elemento):

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
                
    return False
