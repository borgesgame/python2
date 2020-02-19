#------------------------------------------------------------------------#
#           FUNCAO BUSCA COM BUSCADOR BINARIO                            #
#           Python 3.8.1 19-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

'''Melhor algoritmo para busca em uma lista - log 2 n'''
def busca(lista,elemento):

    primeiro = 0
    ultimo = len(lista) - 1
    
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(meio)
        
        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio -1
            else:
                primeiro = meio + 1

    return False
    
