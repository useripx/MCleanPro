<p align="center">
  <img src="assets/logo.png" alt="MrClean Logo" width="160"/>
</p>

<h1 align="center">MrClean — Offline Metadata & AI Watermarks Remover</h1>

<p align="center">
  <b>Aplikasi Desktop Windows Portabel untuk Inspeksi, Pembersihan Metadata Lossless, Penghapusan Steganografi Tanda Air AI, dan Penyuntingan Metadata Selektif secara 100% Offline.</b>
</p>

<p align="center">
  <a href="https://github.com/useripx/MrClean-byArio"><img src="https://img.shields.io/github/repo-size/useripx/MrClean-byArio?style=for-the-badge&logo=github&color=0284c7" alt="Repo Size"/></a>
  <a href="https://github.com/useripx/MrClean-byArio/network/members"><img src="https://img.shields.io/github/forks/useripx/MrClean-byArio?style=for-the-badge&logo=git&color=10b981" alt="Forks"/></a>
  <a href="https://github.com/useripx/MrClean-byArio/stargazers"><img src="https://img.shields.io/github/stars/useripx/MrClean-byArio?style=for-the-badge&logo=star&color=f59e0b" alt="Stars"/></a>
  <a href="https://github.com/useripx/MrClean-byArio/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License"/></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Platform"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Network-100%25%20Offline-success?style=for-the-badge&logo=airplayvideo" alt="Offline"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Tests-27%2F27%20PASS%20(100%25)-brightgreen?style=for-the-badge&logo=checkmarx" alt="Tests"/></a>
</p>

---

## 📖 Tentang MrClean

**MrClean** adalah utilitas keamanan dan privasi berkas digital yang dirancang untuk membersihkan jejak privasi sensitif (seperti lokasi GPS, identitas kamera, nama asli pembuat dokumen, dan riwayat perangkat lunak) serta mendeteksi sekaligus menghapus **steganografi / tanda air tak terlihat yang disematkan oleh Artificial Intelligence** (ChatGPT, Claude, Midjourney, Stable Diffusion, dll.).

Aplikasi ini beroperasi **100% secara offline di memori lokal komputer**, menjamin tidak ada satu pun berkas atau metadata yang dikirimkan ke server cloud atau pihak ketiga.

---

## ✨ Fitur Unggulan (Core Capabilities)

### 1. 🛡️ 100% Offline & Aman (Zero Data Leakage)
Tidak memerlukan koneksi internet atau registrasi akun. Berkas Anda tetap berada di perangkat lokal Anda setiap saat.

### 2. 🔍 Inspeksi Metadata Komprehensif
Membaca seluruh lapis metadata teknis dan identitas:
- **Gambar (JPEG, PNG, WEBP, TIFF):** EXIF tags, koordinat GPS, merk & tipe kamera, lensa, eksposur, dan software pengolah.
- **Dokumen (PDF & DOCX Word):** Nama penulis (*Author*), judul dokumen (*Title*), subjek, kata kunci, nama aplikasi pembuat (*Producer/Creator*), dan riwayat revisi.
- **Media Audio & Video (MP3, MP4, WAV, M4A, FLAC):** Tag ID3, judul lagu, artis, album, tahun, genre, bitrate, dan encoder software.
- **Teks & Koding (.md, .html, .py, .js, .php, dll.):** Statistik karakter kasat mata vs karakter tersembunyi.

### 3. 🤖 Penghapus Tanda Air & Steganografi AI (AI Watermarks Remover)
Mengadopsi dan menyempurnakan algoritma deteksi steganografi modern:
- **Invisible Unicode Watermarks:** Menghapus karakter tak terlihat seperti *Zero-Width Spaces* (`\u200B`), *Zero-Width Joiners* (`\u200D`), *Non-Breaking Spaces*, dan *Variation Selector-16* (`\uFE0F`) tanpa merusak kata atau teks asli.
- **C2PA Content Credentials Manifests:** Membersihkan manifes metadata C2PA pada media sintetis.

### 4. ✏️ Editor Metadata Selektif / Granular (Preservative Editor) *(Baru di v2.0)*
Ingin mengganti nama pembuat dokumen tanpa merusak format aslinya? Fitur ini memungkinkan Anda menyunting field tertentu saja:
- **Contoh Kasus:** Mengubah field **Author** menjadi *"Yogi Ario"* pada dokumen PDF atau gambar JPEG, sementara nilai teknis kamera, tanggal asli, dimensi, dan resolusi **dipertahankan 100% utuh tanpa berubah**.
- Pilihan mode penyimpanan: **Langsung di Tempat (*In-Place*)** atau **Simpan sebagai Salinan Baru**.

### 5. 💾 Ekspor Laporan Hasil Analisis (Radio Button) *(Baru di v2.0)*
Menyediakan jendela dialog pilihan format ekspor laporan:
- **Dokumen PDF (.pdf):** Laporan cetak formal berstandar profesional lengkap dengan kop logo resmi, ringkasan statistik, dan kartu rincian properti per berkas.
- **Berkas Markdown (.md):** Laporan tabel terstruktur GitHub-flavored Markdown lengkap dengan badge status visual (`✅ Bersih`, `⚠️ Metadata`, `🤖 AI-WM`).

### 6. ⚡ Pemindaian & Pembersihan Massal (Batch Processing)
- Tombol **"Pindai 1 Folder..."** untuk memeriksa ratusan berkas dalam satu kali klik.
- Opsi centang **"Pindai Subfolder"** untuk pemindaian rekursif ke seluruh subdirektori.
- Tombol **"Bersihkan Semua di Folder (Batch)"** untuk proses sanitasi massal otomatis.

### 7. 🎨 Antarmuka Modern & Mode Gelap
- Tampilan antarmuka desktop modern berbasis **CustomTkinter**.
- Tombol switch **Mode Gelap (Dark Mode)** dan **Mode Terang (Light Mode)**.
- Status badge visual yang informatif untuk setiap antrean berkas.

---

## 🚀 Panduan Memulai Cepat

### Menggunakan Versi Standalone (.exe)
Bagi pengguna akhir, Anda tidak perlu menginstal Python. Cukup unduh dan jalankan file eksekusi:
1. Buka folder `dist/` atau direktori utama repositori.
2. Klik dua kali pada berkas `Mrclean.exe`.
3. Aplikasi langsung terbuka dan siap digunakan secara offline!

---

## 🛠️ Instalasi & Menjalankan dari Kode Sumber (Developer)

### Prasyarat
- **Sistem Operasi:** Windows 10 / 11
- **Python:** Versi 3.10 atau yang lebih baru (Disarankan Python 3.13)
- **Git**

### Langkah Pemasangan:
```bash
# 1. Clone repositori ini
git clone https://github.com/useripx/MrClean-byArio.git
cd MrClean-byArio

# 2. Buat virtual environment (opsional namun disarankan)
python -m venv venv
venv\Scripts\activate

# 3. Pasang seluruh dependensi resmi
pip install -r requirements.txt

# 4. Jalankan aplikasi GUI
python src/main.py
```

---

## 🧪 Pengujian Otomatis (100% PASS Gate)

Repositori ini menerapkan standar rekayasa ketat (**Pilar 6: 100% Automated Testing Gate**). Seluruh fungsi modul dilengkapi dengan suite pengujian otomatis:

```bash
# Jalankan seluruh unit test suite
python -m unittest discover -s tests -p "test_*.py" -v
```

Hasil Pengujian:
```text
Ran 27 tests in 0.889s
OK (27 PASSED | 0 FAILED | 0 ERRORS)
```

---

## 📦 Mengemas Ulang Executable (.exe)

Untuk mengompilasi ulang aplikasi menjadi berkas `.exe` portabel tunggal berlogo resmi:

```bash
python build_exe.py
```
Hasil kompilasi otomatis tersedia di:
- `dist/Mrclean.exe`
- `Mrclean.exe` (salinan root)

---

## 📁 Struktur Direktori Repositori

```text
MrClean-byArio/
├── .gitignore                     # Perlindungan keamanan & eksklusi berkas sementara
├── .env.example                   # Template konfigurasi standar
├── README.md                      # Dokumentasi utama proyek
├── AGENTS.md                      # Pedoman AI Agent
├── GEMINI.md                      # Pedoman Gemini AI
├── requirements.txt               # Daftar pustaka Python resmi
├── build_exe.py                   # Skrip otomatisasi kompilasi PyInstaller .exe
│
├── Material/                      # [READ-ONLY] Aset mentah asli (logo.jpg & img.png)
│   ├── logo.jpg
│   └── img.png
│
├── assets/                        # Aset produksi aplikasi
│   ├── icon.ico                   # Ikon multi-resolusi untuk jendela & file .exe
│   └── logo.png                   # Logo header antarmuka GUI
│
├── Docs/                          # Dokumentasi tata kelola & laporan teknis
│   ├── universal-rule.md          # 8 Pilar standar kerja universal
│   ├── Task_Status.md             # Pelacak progres fase pengerjaan
│   ├── Decision_Log.md            # Catatan keputusan arsitektur (ADR-001 s.d ADR-006)
│   ├── Implementation_plan.md     # Rencana induk implementasi
│   ├── Test_Report.md             # Laporan resmi pengujian 100% PASS
│   └── chat/                      # Arsip cadangan riwayat obrolan AI
│
├── changelog/                     # Catatan pembaruan bertimestamp flat
│   ├── changelog08pm31102026.md
│   ├── changelog09pm31102026.md
│   ├── changelog10pm31102026.md
│   └── changelog11pm31102026.md
│
├── src/                           # Kode sumber aplikasi utama
│   ├── main.py                    # Entry point aplikasi
│   ├── gui/                       # Antarmuka pengguna (CustomTkinter)
│   │   ├── app.py
│   │   └── dialogs/               # Modal dialogs (Export Dialog & Metadata Edit Dialog)
│   ├── inspectors/                # Ekstraktor metadata (Image, PDF, Docx, Media, Text)
│   ├── cleaners/                  # Pembersih metadata lossless (Image, PDF, Docx, Media, Text)
│   ├── editors/                   # Editor metadata selektif / preservative
│   ├── watermarks/                # Pembersih tanda air & steganografi AI (C2PA & Unicode)
│   └── utils/                     # Util penolong (Scanner, Exporter MD & PDF, Icon Converter)
│
└── tests/                         # Suite pengujian otomatis (27 Kasus Uji)
```

---

## 👤 Pemilik Proyek & Pengembang

Proyek ini dikembangkan dan dikelola oleh:
* **Yogi Ario** — *Lead Developer & Project Owner*
* GitHub: [@useripx](https://github.com/useripx)
* Repositori Resmi: [MrClean-byArio](https://github.com/useripx/MrClean-byArio)

---

## 📄 Lisensi

Didistribusikan di bawah Lisensi MIT. Lihat berkas `LICENSE` untuk informasi lebih lanjut.
