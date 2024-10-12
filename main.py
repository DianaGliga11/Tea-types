from ceai_fille_repository import CeaiFilleRepository
from ceai_service import CeaiService
from ui import UI
from teste_service import *

if __name__ == '__main__':
    teste()
    ceai_repository = CeaiFilleRepository("ceaiuri.txt")
    ceai_service = CeaiService(ceai_repository)
    ui = UI(ceai_service)
    ui.program()
