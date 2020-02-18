#------------------------------------------------------------------------#
#           CLASSE ORDENADOR - SELECAO DIRETA E BURBBLE SORT             #
#           Python 3.8.1 14-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

class Ordenador:


    def direta(self,lista):        
        for i in range(len(lista) - 1):
            menor = i
            
            for j in range(1+i,len(lista)):
                if lista[j] < lista[menor]:
                    menor = j
                    
            lista[i],lista[menor] = lista[menor],lista[i]

        return lista



    def bolha(self,lista):    
        for i in range(len(lista)-1,0,-1):        
            for j in range(i):
                if lista[j+1] < lista[j]:
                    lista[j],lista[j+1] = lista[j+1],lista[j] 

        return lista

