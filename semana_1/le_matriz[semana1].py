#------------------------------------------------------------------------#
#           LE DESENHA E IMPRIME MATRIZES                                #
#           Python 3.8.1 08-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def le_matriz():

    i = int(input("Insira o numero de linhas: "))
    j = int(input("Insira o numero de colunas: "))
    
    desenha_matriz(i,j)

def desenha_matriz(nlinhas,ncolunas):
 
    matriz = []
    
    for i in range(nlinhas):
        linha = []
        
        for j in range(ncolunas):
            coluna = input("Insira um valor para linha["+ str(i) +"] coluna["+ str(j)+"]: " )
            linha.append(coluna)

        matriz.append(linha)

        print()

    imprime_matriz(matriz,nlinhas)


def imprime_matriz(matriz, qlinhas):
  
    for ind in range(qlinhas):
        print(matriz[ind][:])





    

