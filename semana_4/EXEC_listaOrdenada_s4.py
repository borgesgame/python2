#------------------------------------------------------------------------#
#           LISTA ORDENADA? TRUE OU FALSE                                #
#           Python 3.8.1 13-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def ordenada(lista):

        for j in range(len(lista) - 1):
            if lista[j] > lista[j+1]:
                return False

        return True
