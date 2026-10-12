# ============================================================
# PERTEMUAN 07 - FUNGSI PYTHON
# Latihan 4: Statistik Sederhana
# ============================================================

def statistik(data):
    """Mengembalikan nilai minimum, maksimum, dan rata-rata."""
    if not data:
        raise ValueError("Data tidak boleh kosong.")

    total = 0
    minimum = data[0]
    maksimum = data[0]

    for nilai in data:
        total += nilai

        if nilai < minimum:
            minimum = nilai

        if nilai > maksimum:
            maksimum = nilai

    rata_rata = total / len(data)

    return minimum, maksimum, rata_rata


# ------------------------------------------------------------
# Program Utama
# ------------------------------------------------------------

def main():
    print("=" * 50)
    print("LATIHAN 4 - STATISTIK SEDERHANA")
    print("=" * 50)

    data = [70, 80, 65, 90, 75]
    minimum, maksimum, rata_rata = statistik(data)

    print(f"Data      : {data}")
    print(f"Minimum   : {minimum}")
    print(f"Maksimum  : {maksimum}")
    print(f"Rata-rata : {rata_rata:.2f}")

    print("=" * 50)


if __name__ == "__main__":
    main()