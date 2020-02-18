#------------------------------------------------------------------------#
#           CLASSE TRIANGULO - METODO TIPO LADO - ORIENTADA A OBJETOS    #
#           Python 3.8.1 12-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

class Triangulo:

    def __init__(self,a,b,c):
        self.a      = a
        self.b      = b
        self.c      = c
        
        
    def perimetro(self):

        return self.a + self.b + self.c


    def tipo_lado(self):

        lado_a = self.a
        lado_b = self.b
        lado_c = self.c

        if lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
            return 'escaleno' # * lados diferentes

        else:
            if lado_a == lado_b and lado_a == lado_c and lado_b == lado_c:
                return 'equilátero' # * lados iguais

            else:
                return 'isósceles' # 2 lados iguais
            

    def retangulo(self):
        '''A soma dos quadrados dos catetos é igual a porra do quadrado da hipotenusa'''
        ''' hipotenusa(ab)² = cateto(bc)² + cateto(ca)² ou (a**2 + b**2) == c**2'''

        if (self.a**2 + self.b**2) == self.c**2:
            return True

        else:
            return False


    def semelhantes(self,triangulo):
        '''o resultado da divisão dos lados de 2 triangulos será um valor constante.'''
        '''Esse valor é chamado de razão de proporcionalidade. Se este valor for igual, os triangulos sao semelhantes'''

        if ((self.a / triangulo.a) == (self.b / triangulo.b)) and ((self.b / triangulo.b) == (self.c / triangulo.c)):
            return True

        else:
            return False

        
    
        

        
                

