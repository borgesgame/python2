#------------------------------------------------------------------------#
#           ELEFANTES INCOMODAM RECURSIVO                                #
#           Python 3.8.1 22-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def incomodam(n):
    n -= 1
    string = ""
    
    if n < 0:
        return string
    else:        
        string = "incomodam "
        return string + incomodam(n)
    

def elefantes(n):

    string = ""
        
    if n < 1:
        return string        
    else:
        if n >= 1 :
            if n == 1:
                string = "Um elefante incomoda muita gente. "
                print(""+elefantes(n-1) + string,"\n")
            else:
                                
                string = "elefantes "+incomodam(n)+"muito mais. "
                print(str(n)+" "+ elefantes(n-1) + string,"\n")
                
                string = "elefantes incomodam muita gente. "
                print(str(n)+" "+ string,"\n")
   
         
    

    return ""
        

             
        



