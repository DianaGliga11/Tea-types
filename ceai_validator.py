# from ceai_repository import CeaiRepository
# class CeaiValidator:
#     def __init__(self):
#         self.__lista_erori = []
#
#     def eroare_nume(self, nume):
#         ceai_repo = CeaiRepository()
#         lista_ceaiuri = ceai_repo.toate_ceaiurile()
#         for ceai in lista_ceaiuri:
#             if ceai.get_nume() == nume:
#                 self.__lista_erori.append("Numele trebuie sa fie unic!")
#         if len(self.__lista_erori) != 0:
#             raise ValueError(self.__lista_erori)