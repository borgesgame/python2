#------------------------------------------------------------------------#
#           ELEFANTES INCOMODAM RECURSIVO                                #
#           Python 3.8.1 22-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#
import textwrap

def incomodam(n):
    n -= 1
    string = ""
    
    if n < 0:
        return string
    else:        
        string = "incomodam "
        return string + incomodam(n)
    

def elefantes(n):

    verso1 = ""
    verso2 = ""
    verso3 = ""
    musica = ""
        
    if n < 0:
        return musica        
    else:
        verso1 = "Um elefante incomoda muita gente\n"
        verso2 = "elefantes incomodam muita gente\n"        
        verso3 = "elefantes "+incomodam(n)+"muito mais\n"
        
        if n == 1:
            musica = elefantes(n-1) + musica + verso1
            
        elif n > 0:
            musica = musica + str(n)+" "+ verso3
            musica = elefantes(n-1) + musica + str(n)+" "+ verso2

            
                         


    return musica
   
         
    
        

             
        



