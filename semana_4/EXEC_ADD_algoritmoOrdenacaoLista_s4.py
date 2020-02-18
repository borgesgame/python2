#------------------------------------------------------------------------#
#           ORNDENA LISTA                                                #
#           Python 3.8.1 14-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def ordena(lista):
    
    for i in range(len(lista) - 1):
        menor = i
        
        for j in range(1+i,len(lista)):
            if lista[j] < lista[menor]:
                menor = j
                
        lista[i],lista[menor] = lista[menor],lista[i]

    return lista
