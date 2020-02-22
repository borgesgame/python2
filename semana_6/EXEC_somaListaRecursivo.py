#------------------------------------------------------------------------#
#           SOMA LISTA RECURSIVO                                         #
#           Python 3.8.1 22-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def soma_lista(lista):

    if len(lista) == 1:                                                                                                    
        return lista[0]
    else:
        lista[0] = lista[0] + lista[-1]
        lista.remove(lista[-1])
        
        return soma_lista(lista)





