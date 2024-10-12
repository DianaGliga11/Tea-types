
class CeaiRepository:
    def __init__(self):
        self.__lista_ceaiuri = []

    def toate_ceaiurile(self):
        return self.__lista_ceaiuri

    # def genereaza_id(self):
    #     ultimul_ceai = self.__lista_ceaiuri[len(self.__lista_ceaiuri)-1]
    #     ultimul_id = int(ultimul_ceai.get_id())
    #     id_curent = ultimul_id+1
    #     return id_curent

    def  gaseste_ceai_dupa_nume(self, nume):
        for ceai in self.__lista_ceaiuri:
            if ceai.get_nume() == nume:
                return ceai
        return -1
    def adauga_ceai(self, ceai):
        if self.gaseste_ceai_dupa_nume(ceai.get_nume()) != -1:
            raise ValueError("Numele trebuie sa fie unic!")
        else:
            self.__lista_ceaiuri.append(ceai)

    # def sortare(self):
    #     lista_noua = []
    #     lista_noua = sorted(self.__lista_ceaiuri, key=lambda ceai: (ceai.get_tip(), -ceai.get_pret()))
    #     return lista_noua

    def sortare(self):
        k=1
        while True:
            sortat = True
            for i in range(0, len(self.__lista_ceaiuri)-k):
                if self.__lista_ceaiuri[i].get_tip() > self.__lista_ceaiuri[i+1].get_tip():
                    self.__lista_ceaiuri[i], self.__lista_ceaiuri[i+1] = self.__lista_ceaiuri[i+1], self.__lista_ceaiuri[i]
                    sortat = False
                elif self.__lista_ceaiuri[i].get_tip() == self.__lista_ceaiuri[i+1].get_tip():
                    if self.__lista_ceaiuri[i].get_pret() < self.__lista_ceaiuri[i+1].get_pret():
                        self.__lista_ceaiuri[i], self.__lista_ceaiuri[i + 1] = self.__lista_ceaiuri[i + 1], self.__lista_ceaiuri[i]
                        sortat = False
            if sortat or k>len(self.__lista_ceaiuri):
                break

        return self.__lista_ceaiuri