from metaflow import FlowSpec, step

class KuliahFlow(FlowSpec):

    @step
    def start(self):
        self.nama = "L200220169"
        print(f"Mahasiswa {self.nama} memulai proses kuliah.")
        self.next(self.bayar_spp)

    @step
    def bayar_spp(self):
        self.status_spp = True
        print(f"{self.nama} membayar SPP.")
        self.next(self.daftar_matakuliah)

    @step
    def daftar_matakuliah(self):
        if self.status_spp:
            self.matakuliah = "Infrastruktur dan Platform Sains Data"
            print(f"{self.nama} mendaftar mata kuliah {self.matakuliah}.")
            self.next(self.kirim_tugas)  
        else:
            print(f"{self.nama} belum membayar SPP. Proses berhenti.")
            self.next(self.end)

    @step
    def kirim_tugas(self):
        self.nilai_tugas = [85, 90]
        print(f"{self.nama} mengirim tugas dengan nilai {self.nilai_tugas}.")
        self.next(self.ikut_ujian)

    @step
    def ikut_ujian(self):
        self.nilai_ujian = 88
        print(f"{self.nama} mengikuti ujian dengan nilai {self.nilai_ujian}.")
        self.next(self.hitung_nilai_akhir)

    @step
    def hitung_nilai_akhir(self):
        rata_tugas = sum(self.nilai_tugas) / len(self.nilai_tugas)
        self.nilai_akhir = (rata_tugas * 0.4) + (self.nilai_ujian * 0.6)
        print(f"Nilai akhir {self.nama} adalah {self.nilai_akhir:.2f}.")
        self.next(self.end)

    @step
    def end(self):
        print(f"Proses kuliah selesai untuk {self.nama}.")

if __name__ == "__main__":
    KuliahFlow()
