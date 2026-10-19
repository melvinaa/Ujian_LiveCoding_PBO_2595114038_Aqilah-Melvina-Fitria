class PenilaianMahasiswa:
    def __init__(self, nim, nama, nilai_tugas, nilai_uts, nilai_uas):
        self.nim = nim.strip()
        self.nama = nama.strip()
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
        self.validasi_data()

    def validasi_data(self):
        if not self.nim:
            raise ValueError("NIM tidak boleh kosong.")
        if not self.nama:
            raise ValueError("Nama tidak boleh kosong.")
        
        nilai = [self.nilai_tugas, self.nilai_uts, self.nilai_uas]
        for komponen in nilai:
            if not isinstance(komponen, (int, float)):
                raise ValueError("Nilai harus berupa angka.")
            if not 0 <= komponen <= 100:
                raise ValueError("Nilai harus antara 0 dan 100.")

    def hitung_nilai_akhir(self):
        return (
            self.nilai_tugas * 0.30
            + self.nilai_uts * 0.30
            + self.nilai_uas * 0.40
        )

    def tentukan_grade(self):
        nilai_akhir = self.hitung_nilai_akhir()
        if nilai_akhir >= 85:
            return "A"
        elif nilai_akhir >= 75:
            return "B"
        elif nilai_akhir >= 65:
            return "C"
        elif nilai_akhir >= 50:
            return "D"
        else:
            return "E"

    def tentukan_kelulusan(self):
        if self.hitung_nilai_akhir() >= 65:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_hasil(self):
        nilai_akhir = self.hitung_nilai_akhir()
        grade = self.tentukan_grade()
        status = self.tentukan_kelulusan()

        print("\n=== HASIL AKADEMIK ===")
        print(f"NIM         : {self.nim}")
        print(f"Nama        : {self.nama}")
        print(f"Nilai Akhir : {nilai_akhir:.2f}")
        print(f"Grade       : {grade}")
        print(f"Status      : {status}")
        print("=======================")

def input_teks(pesan):
    while True:
        data = input(pesan).strip()
        if data:
            return data
        print("Input tidak boleh kosong. Silakan coba lagi.")

def input_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if 0 <= nilai <= 100:
                return nilai
            print("Nilai harus antara 0 dan 100.")
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def main():
    print("=== SISTEM PENILAIAN ===")
    nim = input_teks("NIM         : ")
    nama = input_teks("Nama        : ")
    nilai_tugas = input_nilai("Nilai Tugas : ")
    nilai_uts = input_nilai("Nilai UTS   : ")
    nilai_uas = input_nilai("Nilai UAS   : ")

    mahasiswa = PenilaianMahasiswa(
        nim, nama, nilai_tugas, nilai_uts, nilai_uas
    )
    mahasiswa.tampilkan_hasil()

if __name__ == "__main__":
    main()