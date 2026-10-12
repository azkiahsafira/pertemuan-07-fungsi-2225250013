# Pertemuan 07 Fungsi Python
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika FKIP Untirta  
**Tahun Ajaran:** 2026/2027 Ganjil

## Identitas Mahasiswa
| Keterangan | Identitas |
|---|---|
| Nama | Azkiah Safira |
| NIM | 2225250013 |
| Kelas | 3F |

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

Melalui latihan dan praktik ini, mahasiswa diharapkan mampu:
- Mendefinisikan dan memanggil fungsi Python.
- Menggunakan parameter dan argumen secara tepat.
- Mengembalikan hasil perhitungan menggunakan `return`.
- Memahami local scope dan global scope.
- Melakukan pengujian, tracing, dan debugging fungsi.
- Mengembangkan program matematika yang mudah dibaca dan digunakan kembali.

Materi ini merupakan kelanjutan dari Pertemuan 06 tentang nested loop,
pola, akumulasi, dan pencacahan. Proses perhitungan yang sebelumnya
ditulis dalam satu alur program dapat dipisahkan menjadi fungsi-fungsi
dengan tugas yang jelas.

## Cara Menjalankan
Pastikan Python 3 sudah terpasang dan terminal VS Code berada di folder
utama proyek.

Periksa versi Python:

    python3 --version

Jalankan latihan sesuai nama berkasnya:

    python3 latihan/01_salam.py
    python3 latihan/02_luas_persegi_panjang.py
    python3 latihan/03_jumlah_n.py
    python3 latihan/04_statistik_sederhana.py
    python3 latihan/05_scope.py

Jalankan program praktik utama:

    python3 praktik/utilitas_matematika.py

Pada Windows, perintah `python3` dapat diganti menjadi `python`
jika sesuai dengan konfigurasi Python di komputer.

## Struktur Fungsi
| Berkas/Fungsi | Parameter | Kegunaan | Nilai Kembali |
|---|---|---|---|
| `salam(nama, kelas)` | `nama`, `kelas` | Menampilkan salam dan kelas | Tidak ada; menggunakan `print` |
| `luas_persegi_panjang(p, l)` | `p`, `l` | Menghitung luas persegi panjang | `p * l` |
| `jumlah_n(n)` | `n` | Menghitung jumlah bilangan 1 sampai n | Nilai total |
| `statistik(data)` | `data` | Menghitung nilai minimum, maksimum, dan rata-rata | Tuple berisi tiga nilai |
| `demo(x)` | `x` | Menunjukkan perbedaan variabel lokal dan global | Nilai `y` |
| `luas_segitiga(a, t)` | `a`, `t` | Menghitung luas segitiga | `0.5 * a * t` |
| `faktorial(n)` | `n` | Menghitung faktorial menggunakan perulangan | Nilai faktorial |
| `tampilkan_menu()` | Tidak ada | Menampilkan pilihan operasi | Tidak ada; menggunakan `print` |

Pada latihan jumlah bilangan, statistik, dan praktik matematika,
perulangan digunakan untuk memproses data. Ini menghubungkan kembali
materi Pertemuan 06 dengan konsep fungsi pada Pertemuan 07.

## Hasil Pengujian
| Program | Input | Hasil yang Diharapkan |
|---|---|---|
| Salam | Nama Alya, kelas 3F | Salam menampilkan nama dan kelas |
| Luas persegi panjang | p = 8, l = 5 | 40 |
| Luas persegi panjang | p = 2.5, l = 4 | 10.0 |
| Jumlah 1 sampai n | n = 1 | 1 |
| Jumlah 1 sampai n | n = 5 | 15 |
| Jumlah 1 sampai n | n = 10 | 55 |
| Statistik sederhana | [70, 80, 65, 90, 75] | Minimum 65, maksimum 90, rata-rata 76.0 |
| Scope | x global = 10, argumen demo = 20 | Nilai x global tetap 10; hasil fungsi 25 |
| Luas persegi panjang | p = 8, l = 5 | 40 |
| Luas segitiga | a = 10, t = 6 | 30.0 |
| Jumlah 1 sampai n | n = 10 | 55 |
| Faktorial | n = 5 | 120 |
| Faktorial | n = 0 | 1 |

**Catatan pengujian:**  
Isi hasil aktual berdasarkan keluaran program setelah dijalankan.
Status dinyatakan **Sesuai** jika hasil aktual sama dengan hasil
yang diharapkan. Uji juga input batas dan input yang tidak valid.


## Refleksi
Melalui Pertemuan 07, saya memahami bahwa fungsi membantu memisahkan
program menjadi bagian-bagian yang memiliki tugas jelas. Parameter
digunakan untuk menerima data, sedangkan `return` mengirimkan hasil
agar dapat digunakan kembali oleh bagian program lain.

Saya juga memahami bahwa variabel lokal hanya dapat digunakan dalam
cakupan fungsi tempat variabel tersebut dibuat. Salah satu kesalahan
yang perlu dihindari adalah mencoba mengakses variabel lokal dari luar
fungsi. Perbaikannya adalah mengembalikan nilai menggunakan `return`.

Dibandingkan dengan program pada Pertemuan 06, penggunaan fungsi
membuat proses perulangan, akumulasi, dan pencacahan lebih terstruktur,
mudah diuji, serta tidak perlu ditulis ulang ketika digunakan untuk
data yang berbeda.