#------------------------------------------------------------------------#
#           ENCONTRA IMPARES LISTA RECURSIVO                             #
#           Python 3.8.1 22-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def encontra_impares(lista):
    impares = []
      
    if len(lista) < 1:                                                                                                    
        return impares
    else:        
        if lista[-1] % 2 == 0:
            lista.remove(lista[-1])
        else:
            impares.append(lista[-1])
            lista.remove(lista[-1])
            
        impares.extend(encontra_impares(lista))

    return impares
    




