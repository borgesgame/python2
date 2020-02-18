#------------------------------------------------------------------------#
#           IMPRIME MATRIZES                                             #
#           Python 3.8.1 09-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def imprime_matriz(matriz):

    qlinhas = len(matriz)
    qcolunas = len(matriz[0][:])
    
    for i in range(qlinhas):  
        for j in range(qcolunas):
            item = matriz[i][j]
            
            if j == qcolunas - 1:
                print(item)

            else:
                print(item,end=' ')



    

