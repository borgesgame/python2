#------------------------------------------------------------------------#
#           RETORNA MENOR STRING (ORDEM LEXICOGRAFICA)                   #
#           Python 3.8.1 10-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def menor_string(lista):    

    anterior = lista[0].strip()
    
    for i in range(len(lista) - 1):       
        atual = lista[i + 1].strip()
        
        if ord(anterior[:1]) < ord(atual[:1]): 
            nome_menor = anterior            
            
        else:
            nome_menor = atual
            anterior = atual
            

    return nome_menor


if __name__ != "__main__":
    import sys
    
    menor_string(sys.argv[1])
