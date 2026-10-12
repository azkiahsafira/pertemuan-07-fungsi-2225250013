# ============================================================
# PERTEMUAN 07 - FUNGSI PYTHON
# Latihan 2: Luas Persegi Panjang
# ============================================================

def luas_persegi_panjang(panjang, lebar):
    """Mengembalikan luas persegi panjang."""
    return panjang * lebar


# ------------------------------------------------------------
# Program Utama
# ------------------------------------------------------------

def main():
    print("=" * 50)
    print("LATIHAN 2 - LUAS PERSEGI PANJANG")
    print("=" * 50)

    test_cases = [
        (8, 5),
        (2.5, 4),
        (0, 7),
    ]

    for panjang, lebar in test_cases:
        luas = luas_persegi_panjang(panjang, lebar)

        print(f"Panjang : {panjang}")
        print(f"Lebar   : {lebar}")
        print(f"Luas    : {luas:g}" if isinstance(luas, float)
              and luas.is_integer() else f"Luas    : {luas}")
        print("-" * 50)


if __name__ == "__main__":
    main()