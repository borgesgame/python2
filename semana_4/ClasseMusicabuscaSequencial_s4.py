#------------------------------------------------------------------------#
#           CLASSE MUSICA COM BUSCA SEQUENCIAL                           #
#           Python 3.8.1 13-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

class Musica:

    def __init__(self,titulo,interprete,compositor,ano):
        self.titulo      = titulo
        self.interprete  = interprete
        self.compositor  = compositor
        self.ano         = ano


class Buscador:

        def busca_por_titulo(self,playlist,titulo):
            for i in range(len(playlist)):
                if playlist[i].titulo == titulo:
                    return i

            return -1
        

        def vamos_buscar(self,playlist = '', titulo = "Simple Man"):

            if playlist == '':
                playlist = [ Musica('Poison Heart','Ramones','Joey Ramone',1993),
                             Musica('Blitzkrieg Bop','Ramones','Joey, Dee Dee e Johnny Ramone',1986),
                             Musica('Ele Disse Não!','Inocentes','Clemente',1983),
                             Musica('Simple Man','Lynyrd Skyrnd','Unknown',1975),
                             Musica('Expulsos do Bar','Garotos Podres','Mau,Portuga',1998)]
            
            onde_achou = self.busca_por_titulo(playlist,titulo)

            if onde_achou == -1:
                print("Minha música preferida não está na playlist")

            else:
                preferida = playlist[onde_achou]
                print(preferida.titulo," - ",preferida.interprete,"/",preferida.compositor,"(",preferida.ano,")")
