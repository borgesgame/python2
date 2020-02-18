#------------------------------------------------------------------------#
#           TESTANDO CLASSES PO ORIENTADA A OBJETOS                      #
#           Python 3.8.1 11-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def main():

    tatiane = mulheres('Tatiane','Vermelhos','Branca','de mel','volei','pizza','67kg')
    juliana = mulheres('Juliana','pretos','Branca','castanhos','natacao','sorvete','49kg')
    mara = mulheres('Mara','pretos','Morena','negros','handball','feijoada','75kg')
    ailza = mulheres('Ailza','pretos','Morena','negros','salto na vara','chocolate','63kg')

    juliana.apresenta()
    ailza.apresenta()
    tatiane.apresenta()
    print()
    mara.comidas(5)
    ailza.pratica(3)
    juliana.comidas(1)
    tatiane.comidas(2)
    juliana.pratica(2)
    mara.pratica(0)


class mulheres:

    def __init__(self,nome,cabelos,cor,olhos,esporte,prato,peso):
        self.nome    = nome
        self.cabelos = cabelos
        self.cor     = cor
        self.olhos   = olhos
        self.esporte = esporte
        self.prato   = prato
        self.peso    = peso

    def apresenta(self):
        print(self.nome,"olhos",self.olhos,"cabelos", self.cabelos)

    def pratica(self,qtd):
        print(self.nome,"pratica",self.esporte,"-",qtd,"vezes por semana, e pesa",self.peso,"kilos.")

    def comidas(self,frq):
        print("Adoro",self.prato,"como pelo menos",frq," vezes por mes. Assinado:",self.nome)
