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
                

