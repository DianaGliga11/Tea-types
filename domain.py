class Ceai:
    def __init__(self, id, nume, tip, pret):
        self.__id = id
        self.__nume = nume
        self.__tip = tip
        self.__pret = pret

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_tip(self):
        return self.__tip

    def get_pret(self):
        return self.__pret

    def __str__(self):
        return "ID: " + str(self.__id) + " Nume: " + self.__nume + " Tip: " + self.__tip + " Pret: " + str(self.__pret) + "\n"
