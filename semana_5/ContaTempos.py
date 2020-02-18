#------------------------------------------------------------------------#
#           CLASSE CONTA TEMPOS                                          #
#           Python 3.8.1 14-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#
import ordenador
import random
import time

class ContaTempos:
    
    def lista_aleatoria(self,n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000)

        return lista


    def compara(self,n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        
        o = ordenador.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou", depois - antes)


        antes = time.time()
        o.direta(lista2)
        depois = time.time()
        print("Direta demorou", depois - antes)
