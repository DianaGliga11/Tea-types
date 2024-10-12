from domain import Ceai

class CeaiService:
    def __init__(self, ceai_repository):
        self.__ceai_repository = ceai_repository

    def toate_ceaiurile_service(self):
        return self.__ceai_repository.toate_ceaiurile()

    def genereaza_id(self):
        lista_ceaiuri = self.toate_ceaiurile_service()
        ultimul_ceai = lista_ceaiuri[len(lista_ceaiuri)-1]
        ultimul_id = int(ultimul_ceai.get_id())
        id_curent = ultimul_id+1
        return id_curent

    def adauga_ceai_service(self, nume, tip, pret):
        id = self.genereaza_id()
        ceai = Ceai(id, nume, tip, pret)
        return self.__ceai_repository.adauga(ceai)

    def sortare_service(self):
        return self.__ceai_repository.sortare()

