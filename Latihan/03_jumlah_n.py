# ============================================================
# PERTEMUAN 07 - FUNGSI PYTHON
# Latihan 3: Jumlah Bilangan 1 sampai n
# ============================================================

def jumlah_n(n):
    """Mengembalikan jumlah bilangan bulat dari 1 sampai n."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif.")

    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# ------------------------------------------------------------
# Program Utama
# ------------------------------------------------------------

def main():
    print("=" * 50)
    print("LATIHAN 3 - JUMLAH BILANGAN 1 SAMPAI N")
    print("=" * 50)

    test_cases = [1, 5, 10, 100]

    for n in test_cases:
        hasil = jumlah_n(n)
        rumus = n * (n + 1) // 2

        print(f"n                    : {n}")
        print(f"Hasil fungsi         : {hasil}")
        print(f"Hasil rumus n(n+1)/2 : {rumus}")
        print(f"Status               : {'Sesuai' if hasil == rumus else 'Tidak sesuai'}")
        print("-" * 50)


if __name__ == "__main__":
    main()