#------------------------------------------------------------------------#
#           FUNCAO CONTA LETRAS                                          #
#           Python 3.8.1 10-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def conta_letras(frase, contar ='vogais'):

    frase = frase.replace(' ','').lower()

    count_v = 0
    count_c = 0
    
    for i in range(len(frase)):

        comp = frase[i:i+1]
        if comp == 'a' or comp == 'e' or comp == 'i' or comp == 'o' or comp == 'u' :
            count_v += 1
                
        else:
            count_c += 1
            

    if contar == 'vogais':
        return count_v
    
    elif contar == 'consoantes' or contar == 'consoante':
        return count_c
    
    else:
        return print("erro 0x01: Parametro Incorreto [param. aceito: vogais ou consoantes]")
   


