#------------------------------------------------------------------------#
#           EXEMPLO DE RECURSAO -  PRINT NUMEROS                         #
#           Python 3.8.1 21-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def x(n):
    if n == 0:
        print(n)
    else:
        x(n-1)
        print(n)
    


x(10)


'''QUESTAO SEMANA 6
Se a função acima for chamada como x(10), onde é necessário colocar o
comando print(n) para que a função imprima os números de 0 até 10?


A) No <espaço A> e no <espaço E>

B) No <espaço A> e no <espaço B>

C) No <espaço C> e no <espaço E>

D) Nenhuma das opções apresentadas está correta

E) No <espaço B> e no <espaço C>

F) No <espaço A> e no <espaço C>

G) No <espaço B> e no <espaço E>

H) No <espaço A>, no <espaço B> e no <espaço C>




'''
