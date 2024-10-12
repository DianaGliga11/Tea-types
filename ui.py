
class UI:
    def __init__(self, ceai_service):
        self.__ceai_service = ceai_service

    def meniu(self):
        meniu = ""
        meniu = meniu + "1. Afiseaza ceaiuri\n"
        meniu = meniu + "2. Adauga ceai\n"
        meniu = meniu + "3. Sorteaza dupa tip si pret\n"
        meniu = meniu + "x-Exit\n"
        return meniu

    def program(self):
        ruleaza = True
        while ruleaza :
            meniul = self.meniu()
            print(meniul)
            comanda = input("Introduceti comanda dorita: ")
            if comanda == '1':
                self.ui_afiseaza_ceaiuri()
            elif comanda == '2':
                self.ui_adauga_ceai()
            elif comanda == '3':
                self.ui_sortare()
            elif comanda == 'x':
                ruleaza = False
            else:
                print("Nu exista aceasta comanda!")

    def ui_afiseaza_ceaiuri(self):
        lista_ceaiuri = self.__ceai_service.toate_ceaiurile_service()
        if len(lista_ceaiuri) == 0:
            print("Nu sunt ceaiuri introduse!")
        else:
            for ceai in lista_ceaiuri:
                print(ceai)

    def ui_adauga_ceai(self):
        try:
            nume = input("Introduceti numele: ")
            tip = input("Introfduceti tipul: ")
            pret = int(input("Introduceti pretul: "))
            self.__ceai_service.adauga_ceai_service(nume, tip, pret)
            print("Adaugat cu succes!")
        except IOError as io:
            print(io)
        except ValueError as ve:
            print(ve)

    def ui_sortare(self):
        lista_sortata = self.__ceai_service.sortare_service()
        for ceai in lista_sortata:
            print(ceai)