#------------------------------------------------------------------------#
#           ALGORITMO BURBBLE SORT - ORDENACAO                           #
#           Python 3.8.1 14-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#


def bolha(lista):
    
    for i in range(len(lista)-1,0,-1):        
        for j in range(i):
            if lista[j+1] < lista[j]:
                lista[j],lista[j+1] = lista[j+1],lista[j] 

    return lista
