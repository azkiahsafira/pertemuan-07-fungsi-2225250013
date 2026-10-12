# ============================================================
# PERTEMUAN 07 - FUNGSI PYTHON
# Latihan 5: Local Scope dan Global Scope
# ============================================================

# ------------------------------------------------------------
# Variabel Global
# ------------------------------------------------------------

x = 10


# ------------------------------------------------------------
# Definisi Fungsi
# ------------------------------------------------------------

def demo(x):
    """Menunjukkan bahwa parameter x merupakan variabel lokal."""
    y = x + 5

    print(f"Nilai x di dalam fungsi : {x}")
    print(f"Nilai y di dalam fungsi : {y}")

    return y


# ------------------------------------------------------------
# Program Utama
# ------------------------------------------------------------

def main():
    print("=" * 50)
    print("LATIHAN 5 - SCOPE VARIABEL")
    print("=" * 50)

    print(f"Nilai x sebelum fungsi  : {x}")

    hasil = demo(20)

    print("-" * 50)
    print(f"Nilai x setelah fungsi  : {x}")
    print(f"Nilai return dari demo  : {hasil}")

    print("=" * 50)


if __name__ == "__main__":
    main()