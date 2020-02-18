#------------------------------------------------------------------------#
#           RETORNA NOME MAIS CURTO DA LISTA                             #
#           Python 3.8.1 10-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def menor_nome(lista):    

    anterior = lista[-1]
    
    for i in range(len(lista),0,-1):
        atual = lista[i - 1]
        
        if len(anterior.strip()) < len(atual.strip()): 
            nome_menor = anterior            
            
        else:
            nome_menor = atual
            anterior = atual
            

    return nome_menor.strip().capitalize()







    

