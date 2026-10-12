# ============================================================
# PERTEMUAN 07 - FUNGSI PYTHON
# Latihan 1: Fungsi Salam
# ============================================================

def salam(nama, kelas):
    """Menampilkan salam berdasarkan nama dan kelas."""
    print(f"Halo, {nama}.")
    print(f"Selamat belajar Python di kelas {kelas}.")


# ------------------------------------------------------------
# Program Utama
# ------------------------------------------------------------

def main():
    print("=" * 50)
    print("LATIHAN 1 - FUNGSI SALAM")
    print("=" * 50)

    salam("Alya", "3F")
    print("-" * 50)
    salam("Bima", "3F")

    print("=" * 50)


if __name__ == "__main__":
    main()