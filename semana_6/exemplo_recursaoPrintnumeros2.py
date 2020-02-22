#------------------------------------------------------------------------#
#           EXEMPLO DE RECURSAO -  PRINT NUMEROS 2                       #
#           Python 3.8.1 21-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def x(n):
    if n >= 0 and n <=2:
        return n
    else:
        return x(n-1) + x(n-2) + x(n-3)

print(x(6))

 
'''
1 chamada 5+4+3 = 12
2 chamada 4+2+0 = 6
3 chamada 3+0+0 = 3
4 chamada 2+0+0 = 2               


return x(n [2,3,4,5]) + x(n [0,0,2,4]) + x( n [0,0,0,3])'''





