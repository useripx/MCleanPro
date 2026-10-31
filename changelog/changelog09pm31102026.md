# Changelog — 09pm31102026

**Tanggal:** 31 Oktober 2026 (21:33 WIB)  
**Tipe Perubahan:** Rilis Fitur & Packaging Executable  
**Penyusun:** AI Agent (Pair Programmer)  
**Otoritas:** Yogi Ario  

---

### 🚀 Perubahan & Penambahan Baru
1. **Engine Core Inspektor & Pembersih Metadata:**
   - Dibuat modul ekstraksi metadata `src/inspectors/` untuk Gambar (EXIF, GPS, Kamera), Dokumen PDF (Author, Producer, Tanggal), Dokumen Word DOCX (Core Properties, Revisions), Media Audio/Video (mutagen tags), dan Teks.
   - Dibuat modul pembersihan *lossless* `src/cleaners/` yang mengosongkan tag metadata tanpa menurunkan kualitas visual/audio.
   - Dibuat modul `src/watermarks/` berbasis `guillaumemeyer/watermarks-remover` untuk mendeteksi dan membersihkan *invisible Unicode steganography* (zero-width spaces, joiners, variation selectors) serta tanda provenance C2PA.
2. **Scanner Berkas & Folder Batch:**
   - Implementasi `src/utils/scanner.py` yang mendukung pemilihan berkas individual maupun pemindaian seluruh dokumen/gambar dalam 1 folder sekaligus (termasuk opsi rekursif subfolder).
   - Implementasi utilitas ekspor laporan ke format `.json` dan `.txt` (`src/utils/exporter.py`).
3. **Antarmuka Desktop GUI Modern (`src/gui/app.py`):**
   - Menggunakan CustomTkinter dengan dukungan Dark/Light mode otomatis.
   - Dilengkapi tombol pemindaian berkas ("📄 Tambah Berkas...") dan folder ("📁 Pindai 1 Folder...").
   - Menampilkan daftar antrean file beserta status metadata dan indikator watermark AI.
   - Panel inspeksi detail kartu interaktif untuk melihat seluruh tag metadata per kategori.
   - Aksi pembersihan sekali klik: Bersihkan Metadata Terpilih, Bersihkan Semua Berkas di Folder (Batch), dan Hapus Watermark AI.
4. **Verifikasi Pengujian Otomatis (100% PASS Gate):**
   - 17 unit test dibuat di `tests/` mencakup seluruh scanner, inspector, cleaner, watermark engine, dan exporter.
   - Hasil pengujian: **100% PASS (17 Lulus, 0 Gagal, 0 Error)** dicatat di `Docs/Test_Report.md`.
5. **Kompilasi Standalone Executable (.exe):**
   - Berkas mentah `Material/img.png` berhasil dikonversi ke format Windows multi-ukuran `assets/icon.ico`.
   - Berhasil dikompilasi menggunakan PyInstaller menghasilkan file tunggal portabel di `dist/MetaClean.exe` (35.91 MB) dengan ikon kustom `Material/img.png`.
