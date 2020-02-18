def bhaskara(a,b,c):

    d = delta(a,b,c)

    if d >= 0:

        if d > 0:
            return CalcRaiz(a,b,c)

        if d == 0:
            raiz_1 = -b / (2*a)
            return 1, raiz_1

    else:
        return 0


def delta(a,b,c):

    return b**2 - 4*a*c

def CalcRaiz(a,b,c):

    import math

    raiz_1 = (-b + math.sqrt(delta (a,b,c))) / (2*a)
    raiz_2 = (-b - math.sqrt(delta (a,b,c))) / (2*a)

    if raiz_1 < raiz_2:
        return 2,raiz_1,raiz_2

    else:
        return 2,raiz_2,raiz_1

def test_raizes():
    assert bhaskara(1,0,0) == (2,-1.5, 1.0)
