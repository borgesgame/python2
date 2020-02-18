#------------------------------------------------------------------------#
#           RETORNA LISTA DE MAIUSCULAS DE UMA FRASE                     #
#           Python 3.8.1 10-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def maiusculas(string):    

    maiusculas = ""
    for i in range(len(string)):       
                
        if ord(string[i:i+1]) > 64 and ord(string[i:i+1]) < 91: 
            maiusculas += string[i:i+1]            
            

    return maiusculas

