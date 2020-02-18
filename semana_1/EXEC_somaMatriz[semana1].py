#------------------------------------------------------------------------#
#           RETORNA SOMA DE MATRIZES DE MESMA DIMENSAO                   #
#           Python 3.8.1 08-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def soma_matrizes(m1,m2):

    d1 = dimensoes_matriz(m1)
    d2 = dimensoes_matriz(m2)

    if d1 != d2:
        return False

    else:
        matriz = []
        for i in range(len(m1)):
            linhas = []
            for j in range(len(m1[0][:])):
                colunas = int(m1[i][j]) + int(m2[i][j])                
                linhas.append(colunas)

            matriz.append(linhas)

        return matriz    
                


def dimensoes_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0][:])


    return linhas,colunas






    

