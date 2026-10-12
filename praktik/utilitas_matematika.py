# ============================================================
# PERTEMUAN 07 - FUNGSI PYTHON
# Praktik 2: Utilitas Matematika Modular
# ============================================================

# ------------------------------------------------------------
# Fungsi Perhitungan
# ------------------------------------------------------------

def luas_persegi_panjang(p, l):
    """Mengembalikan luas persegi panjang."""
    return p * l


def luas_segitiga(a, t):
    """Mengembalikan luas segitiga."""
    return 0.5 * a * t


def jumlah_n(n):
    """Mengembalikan jumlah bilangan 1 sampai n."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif.")

    total = 0

    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    """Mengembalikan nilai faktorial n."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif.")

    hasil = 1

    for i in range(2, n + 1):
        hasil *= i

    return hasil


# ------------------------------------------------------------
# Fungsi Input
# ------------------------------------------------------------

def input_angka(pesan):
    """Meminta input angka dan mengulang jika input tidak valid."""
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")


def input_bilangan_nonnegatif(pesan):
    """Meminta bilangan bulat nonnegatif."""
    while True:
        teks = input(pesan).strip()

        try:
            n = int(teks)

            if n < 0:
                print("Nilai tidak boleh negatif.")
                continue

            return n

        except ValueError:
            print("Input harus berupa bilangan bulat nonnegatif.")


# ------------------------------------------------------------
# Fungsi Menu
# ------------------------------------------------------------

def tampilkan_menu():
    """Menampilkan pilihan operasi matematika."""
    print("\n" + "=" * 55)
    print("             UTILITAS MATEMATIKA")
    print("=" * 55)
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah bilangan 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")
    print("-" * 55)


# ------------------------------------------------------------
# Fungsi Program Utama
# ------------------------------------------------------------

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi [0-4]: ").strip()

        if pilihan == "1":
            print("\n[LUAS PERSEGI PANJANG]")
            panjang = input_angka("Masukkan panjang: ")
            lebar = input_angka("Masukkan lebar  : ")

            hasil = luas_persegi_panjang(panjang, lebar)

            print(f"Luas persegi panjang = {hasil:g}")

        elif pilihan == "2":
            print("\n[LUAS SEGITIGA]")
            alas = input_angka("Masukkan alas   : ")
            tinggi = input_angka("Masukkan tinggi : ")

            hasil = luas_segitiga(alas, tinggi)

            print(f"Luas segitiga = {hasil:g}")

        elif pilihan == "3":
            print("\n[JUMLAH BILANGAN 1 SAMPAI N]")
            n = input_bilangan_nonnegatif("Masukkan n: ")

            hasil = jumlah_n(n)

            print(f"Jumlah 1 sampai {n} = {hasil}")

        elif pilihan == "4":
            print("\n[FAKTORIAL]")
            n = input_bilangan_nonnegatif("Masukkan n: ")

            hasil = faktorial(n)

            print(f"{n}! = {hasil}")

        elif pilihan == "0":
            print("\nProgram selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak tersedia. Silakan pilih 0 sampai 4.")


# ------------------------------------------------------------
# Eksekusi Program
# ------------------------------------------------------------

if __name__ == "__main__":
    main()