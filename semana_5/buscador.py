#------------------------------------------------------------------------#
#           FUNCAO ORDENADOR INSERTION SORT                              #
#           Python 3.8.1 19-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def insertion_sort(lista):

    index = 0
    suspenso = 0

    for i in range(len(lista) - 1):
        
        menor = False
        for eq in range(i,-1,-1):      

            if lista[i+1] < lista[eq]:
                index = eq
                suspenso = lista[i+1]
                menor = True

        if menor:
            for cont in range(i+1,index,-1):
                lista[cont] = lista[cont -1]

                if lista[cont-1] > suspenso:    
                    lista[cont - 1] = suspenso
        print(lista)
                    
                    
    return lista
            
                                    
    
    
