#------------------------------------------------------------------------#
#           CLASSE BUSCADOR                                              #
#           Python 3.8.1 19-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

class Buscador:

    def busca_sequencial(self,lista,elemento):

        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
                    
        return False

    '''Melhor algoritmo para busca em uma lista - log 2 n'''
    def busca_binaria(self,lista,elemento):

        primeiro = 0
        ultimo = len(lista) - 1
        
        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2

            if lista[meio] == elemento:
                return meio
            else:
                if elemento < lista[meio]:
                    ultimo = meio -1
                else:
                    primeiro = meio + 1

        return -1
    
