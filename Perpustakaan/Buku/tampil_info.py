from .judul import Judul
from .pengarang import Pengarang

class Tampil_info:
    def __init__(self, judul, pengarang):
        self.judul = Judul(judul)
        self.pengarang = Pengarang(pengarang)

    def tampil_info(self):
        self.judul.tampil_judul()
        self.pengarang.tampil_pengarang()