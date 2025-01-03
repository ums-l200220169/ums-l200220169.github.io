from metaflow import FlowSpec, step

class ProsesKuliahFlow(FlowSpec):

    @step
    def start(self):
        # Memulai proses kuliah
        self.nama_mahasiswa = "Monica Auzan Nalurita"
        self.status_pendaftaran = False
        print(f"Memulai proses kuliah untuk: {self.nama_mahasiswa}")
        self.next(self.pendaftaran)

    @step
    def pendaftaran(self):
        # Proses pendaftaran mahasiswa
        self.status_pendaftaran = True
        print(f"{self.nama_mahasiswa} telah mendaftar untuk kuliah.")
        self.next(self.bayar_spp)

    @step
    def bayar_spp(self):
        # Proses pembayaran SPP
        print(f"{self.nama_mahasiswa} sedang melakukan pembayaran SPP.")
        self.next(self.mengikuti_kuliah)

    @step
    def mengikuti_kuliah(self):
        # Proses mengikuti kuliah
        print(f"{self.nama_mahasiswa} sekarang mengikuti kuliah.")
        self.next(self.dapatkan_nilai)

    @step
    def dapatkan_nilai(self):
        # Proses mendapatkan nilai akhir
        self.nilai_akhir = "B+"
        print(f"{self.nama_mahasiswa} mendapatkan nilai akhir: {self.nilai_akhir}.")
        self.next(self.selesai)

    @step
    def selesai(self):
        # Menyelesaikan alur kerja
        print("Proses kuliah telah selesai. Terima kasih, ", self.nama_mahasiswa)
        self.next(self.end)

    @step
    def end(self):
        # Menyelesaikan alur secara resmi
        print("Alur kerja selesai.")

if __name__ == "__main__":
    ProsesKuliahFlow()
