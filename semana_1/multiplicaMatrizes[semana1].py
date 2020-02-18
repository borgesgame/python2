#------------------------------------------------------------------------#
#           VERIFICA SE MATRIZES SAO MULTIPLICAVEIS                      #
#           Python 3.8.1 08-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#
'''Duas matrizes são multiplicáveis se o número de colunas da primeira é
   igual ao número de linhas da segunda.'''

def sao_multiplicaveis(m1,m2):

    colunas = len(m1[0][:])
    linhas = len(m2)
    
    if colunas != linhas:
        return print("Desculpe, para que duas matrizes sejam multiplicaveis,\n"
                +"o numero de COLUNAS da primeira deve ser igual o numero\n"
                +"de LINHAS da segunda.")
    else:
        return multiplica_matriz(m1,m2)


def multiplica_matriz(m1,m2):

    nlinhas_m1, ncolunas_m1 = len(m1), len(m1[0])
    nlinhas_m2, ncolunas_m2 = len(m2), len(m2[0])

    c = []
    for linha in range(nlinhas_m1):
        #Comecando uma nova linha
        c.append([])
        for coluna in range(ncolunas_m2):
            #Adicionando uma nova coluna na linha
            c[linha].append(0)
            for k in range(ncolunas_m1):
                c[linha][coluna] += m1[linha][k] * m2[k][coluna]

    return c

    
  
                


    







    

