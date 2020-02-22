#------------------------------------------------------------------------#
#           FUNCAO ORDENADOR INSERTION SORT                              #
#           Python 3.8.1 19-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def insertion_sort(lista):

    index_max = 0
    suspenso_min = 0
    for i in range(len(lista)-1):
        
        menor = False
        for eq in range(i,-1,-1):      

            if lista[i+1] < lista[eq]:
                menor = True
                index_max = eq
                suspenso_min = lista[i+1]

        if menor:
            print("Suspenso:",suspenso_min,"Delta alocacao:",index_max)
            for cont in range(i+1,index_max,-1):
                lista[cont] = lista[cont-1]

                if lista[cont-1] > suspenso_min:    
                    lista[cont-1] = suspenso_min

                                
    return lista
            
                                    
    
    
