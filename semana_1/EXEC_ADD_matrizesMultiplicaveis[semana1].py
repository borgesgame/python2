#------------------------------------------------------------------------#
#           VERIFICA SE MATRIZES SAO MULTIPLICAVEIS                      #
#           Python 3.8.1 08-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#
'''Duas matrizes são multiplicáveis se o número de colunas da primeira é
   igual ao número de linhas da segunda.'''

def sao_multiplicaveis(m1,m2):

    colunas = len(m1[0][:])
    linhas = len(m2)
    
    if colunas == linhas:
        return True    

    else:      

        return False    
                


    







    

