# Tugas Kecil 2 IF2211 Strategi Algoritma - 15-Puzzle Solver
## Deskripsi program
15-Puzzle Solver adalah program untuk menghasilkan solusi dari konfigurasi 15-Puzzle tertentu. Program berbasis command line ini menggunakan pembangkitan kemungkinan solusi dari puzzle sejalan dengan algoritma _branch and bound_. Penjelasan tentang algoritma tersebut dapat ditemukan pada salindia [Algoritma Branch & Bound Bagian 1](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2020-2021/Algoritma-Branch-and-Bound-2021-Bagian1.pdf).

## Persyaratan penggunaan
Agar dapat menggunakan program, dibutuhkan interpreter Python 3. Program ini dibuat dengan Python versi 3.9.5. Karena itu, direkomendasikan pada sistem sudah ter-install Python versi 3.9.5 atau yang lebih baru.

## Cara Penggunaan Program
Untuk penggunaan program, lakukan clone terlebih dahulu pada repository ini dengan membuka command line atau terminal lalu mengeksekusi perintah berikut
    
    git clone https://github.com/VanillaMacchiato/Tucil3_13520153.git
    cd Tucil3_13520153
    python src/main.py

Setelah itu, program akan terbuka. Pengguna dapat memilih untuk memasukkan konfigurasi 15-Puzzle secara manual atau dari file. Program yang sudah dimasukkan konfigurasi akan berjalan dan mencari solusi jika ada.

## Konfigurasi File
Jika ingin membuat konfigurasi file, dapat menggunakan format 4x4 yang dipisahkan dengan spasi. Ganti tile kosong dengan 0. Contoh:

    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 0


## Identitas Pembuat
NIM: 13520153

Nama: Vito Ghifari