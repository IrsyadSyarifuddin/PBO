from .nama import Nama
from .nomor_anggota import Nomor_anggota

class Tampil_info:
    def __init__(self, nama, nomor_anggota):
        self.nama = Nama(nama)
        self.nomor_anggota = Nomor_anggota(nomor_anggota)

    def tampil_info(self):
        self.nama.tampil_nama()
        self.nomor_anggota.tampil_nomor_anggota()