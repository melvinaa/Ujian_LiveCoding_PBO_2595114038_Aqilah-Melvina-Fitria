class TiketParkir:
    def __init__(self, nomor_polisi, jenis_kendaraan, durasi):
        self.nomor_polisi = nomor_polisi.strip()
        self.jenis_kendaraan = jenis_kendaraan.strip().capitalize()
        self.durasi = durasi
        self.validasi_data()

    def validasi_data(self):
        if not self.nomor_polisi:
            raise ValueError("Nomor polisi tidak boleh kosong.")
        if not self.jenis_kendaraan not in ["Motor", "Mobil"]:
            raise ValueError("Jenis kendaraan harus Motor atau Mobil.")
        if not isinstance(self.durasi, int) or not 1 <= self.durasi <= 24:
            raise ValueError("Durasi harus berupa bilangan bulat 1-24 jam.")

    def hitung_jam_pertama(self):
        if self.jenis_kendaraan == "Motor":
            return 2000
        else:
            return 5000

    def hitung_jam_tambahan(self):
        if self.durasi <= 1:
            return 0
        if self.jenis_kendaraan == "Motor":
            tarif = 1000
        else:
            tarif = 3000
        return (self.durasi - 1) * tarif

    def hitung_biaya_tambahan(self):
        if self.durasi > 5:
            return 5000
        else:
            return 0

    @staticmethod
    def format_rupiah(nominal):
        return "Rp" + f"{nominal:,.0f}".replace(",", ".")

    def hitung_total(self):
        return (
            self.hitung_jam_pertama()
            + self.hitung_jam_tambahan()
            + self.hitung_biaya_tambahan()
        )

    def tampilkan_tiket(self):
        print("\n=== TIKET PARKIR ===")
        print(f"Nomor polisi    : {self.nomor_polisi}")
        print(f"Jenis kendaraan : {self.jenis_kendaraan}")
        print(f"Durasi          : {self.durasi} jam")
        print(f"Jam pertama     : {self.format_rupiah(self.hitung_jam_pertama())}")
        print(f"Jam tambahan    : {self.format_rupiah(self.hitung_jam_tambahan())}")
        print(f"Biaya tambahan  : {self.format_rupiah(self.hitung_biaya_tambahan())}")
        print(f"Total parkir    : {self.format_rupiah(self.hitung_total())}")
        print("====================")

def input_teks(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong.")

def input_jenis_kendaraan():
    while True:
        jenis = input("Jenis kendaraan (Motor/Mobil) : ").strip().capitalize()
        if jenis in ["Motor", "Mobil"]:
            return jenis
        print("Jenis kendaraan harus Motor atau Mobil.")

def input_durasi():
    while True:
        try:
            durasi = int(input("Durasi parkir (1-24 jam)      : "))
            if 1 <= durasi <= 24:
                return durasi
            print("Durasi harus antara 1 sampai 24 jam.")
        except ValueError:
            print("Durasi harus berupa bilangan bulat.")

def main():
    print("=== SISTEM PARKIR ===")
    nomor_polisi = input_teks("Nomor polisi                  : ")
    jenis_kendaraan = input_jenis_kendaraan()
    durasi = input_durasi()

    tiket = TiketParkir(
        nomor_polisi, jenis_kendaraan, durasi
    )
    tiket.tampilkan_tiket()

if __name__ == "__main__":
    main()