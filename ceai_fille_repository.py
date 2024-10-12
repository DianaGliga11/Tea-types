from ceai_repository import CeaiRepository
from domain import Ceai

class CeaiFilleRepository(CeaiRepository):
    def __init__(self, nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_din_fisier()

    def adauga(self, ceai):
        super().adauga_ceai(ceai)
        self.scrie_in_fisier()

    def citeste_din_fisier(self):
        try:
            f = open(self.__nume_fisier, "r")
            linie = f.readline().strip("\n")
            while linie != "":
                lista_atribute = linie.split(",")
                id = int(lista_atribute[0])
                nume = lista_atribute[1]
                tip = lista_atribute[2]
                pret = int(lista_atribute[3])
                ceai = Ceai(id, nume, tip, pret)
                super().adauga_ceai(ceai)
                linie = f.readline().strip("\n")
            f.close()
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__nume_fisier)

    def scrie_in_fisier(self):
        try:
            f = open(self.__nume_fisier, "w")
            toate_ceaiurile = super().toate_ceaiurile()
            for ceai in toate_ceaiurile:
                id = ceai.get_id()
                nume = ceai.get_nume()
                tip = ceai.get_tip()
                pret = ceai.get_pret()
                linie = str(id) + "," + nume + "," + tip + "," + str(pret) + "\n"
                f.write(linie)
            f.close()
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__nume_fisier)