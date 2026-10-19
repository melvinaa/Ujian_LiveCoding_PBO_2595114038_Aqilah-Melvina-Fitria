class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga_satuan, jumlah):
        self.pelanggan = pelanggan.strip()
        self.barang = barang.strip()
        self.harga_satuan = harga_satuan
        self.jumlah = jumlah
        self.validasi_data()

    def validasi_data(self):
        if not self.pelanggan:
            raise ValueError("Nmana pelanggan tidak boleh kosong.")
        if not self.barang:
            raise ValueError("Nama barang tidak boleh kosong.")
        if not isinstance(self.harga_satuan, int) or self.harga_satuan <= 0:
            raise ValueError("Harga harus berupa bilangan bulat positif.")
        if not isinstance(self.jumlah, int) or self.jumlah <= 0:
            raise ValueError("Jumlah harus berupa bilangan bulat positif.")

    def hitung_subtotal(self):
        return self.harga_satuan * self.jumlah

    def tentukan_diskon(self):
        subtotal = self.hitung_subtotal()
        if subtotal >= 500000:
            return 0.15
        elif subtotal >= 250000:
            return 0.15
        elif subtotal >= 100000:
            return 0.05
        else:
            return 0.0

    def hitung_potongan(self):
        return self.hitung_subtotal() * self.tentukan_diskon()

    def hitung_total(self):
        return self.hitung_subtotal() - self.hitung_potongan()

    @staticmethod
    def format_rupiah(nominal):
        return"Rp" +f"{nominal:,.0f}".replace(",", ".")

    def tampilkan_struk(self):
        subtotal = self.hitung_subtotal()
        diskon = self.tentukan_diskon()
        potongan = self.hitung_potongan()
        total = self.hitung_total()

        print("\n===STRUK PEMBAYARAN===")
        print(f"Pelanggan   : {self.pelanggan}")
        print(f"Barang      : {self.barang}")
        print(f"Subtotal    : {self.format_rupiah(subtotal)}")
        print(f"Diskon      : {diskon*100:.0f}%")
        print(f"Potongan    : {self.format_rupiah(potongan)}")
        print(f"Total bayar : {self.format_rupiah(total)}")
        print("========================")

def input_teks(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
             return nilai
        print("Input tidak boleh kosong. Silakan coba lagi.")

def input_bilangan_positif(pesan):
    while True:
        try:
            nilai = int(input(pesan))

            if nilai > 0:
                return nilai
            print("Angka harus lebih besar dari 0.")

        except ValueError:
            print("Input harus berupa bilangan bulat positif.")

def main():
    print("===KASIR MINIMARKET===")

    pelanggan = input_teks("Nama pelanggan : ")
    barang = input_teks("Nama barang    : ")
    harga_satuan = input_bilangan_positif("Harga barang   : Rp")
    jumlah = input_bilangan_positif("Jumlah barang  : ")

    transaksi = TransaksiKasir(
        pelanggan,
        barang,
        harga_satuan,
        jumlah
     )
    transaksi.tampilkan_struk()

if __name__ == "__main__":
    main()