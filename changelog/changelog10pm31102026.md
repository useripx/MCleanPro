# Changelog — 10pm31102026

**Tanggal:** 31 Oktober 2026 (22:13 WIB)  
**Tipe Perubahan:** Pembaruan Branding, Pembersih Markdown & Coding, serta In-Place Cleaning  
**Penyusun:** AI Agent (Pair Programmer)  
**Otoritas:** Yogi Ario  

---

### 🚀 Perubahan & Penambahan Baru
1. **Fitur Pembersihan Langsung di Tempat (In-Place Cleaning):**
   - Menambahkan opsi `"Timpa Berkas Asli Langsung (In-Place)"` yang aktif secara default pada antarmuka aplikasi.
   - Saat tombol *"Bersihkan Berkas Terpilih"* atau *"Bersihkan Semua di Folder (Batch)"* ditekan, berkas target (misal: `README.md`, `Decision_Log.md`, dsb.) langsung dibersihkan di tempat secara atomik dan aman tanpa menduplikasi berkas menjadi `_clean.md` atau `_nowatermark.md`.
   - Item di daftar antrean secara instan diperbarui statusnya menjadi **`✅ Bersih`** dan panel detail langsung menyatakan bebas dari metadata/watermark.
2. **Pembaruan Logo Baru (`Material/logo.jpg`):**
   - Berkas [`Material/logo.jpg`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/Material/logo.jpg) (2048x2048) dikonversi menjadi ikon Windows multi-resolusi [`assets/icon.ico`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/assets/icon.ico).
   - Menambahkan fungsi resolusi path aset `sys._MEIPASS` agar logo [`assets/logo.png`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/assets/logo.png) dan ikon jendela tampil sempurna di dalam file executable PyInstaller tunggal.
3. **Pembersih Format Markdown (.md) & Berkas Coding:**
   - Dibuat modul [`src/cleaners/text_cleaner.py`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/src/cleaners/text_cleaner.py) dan didaftarkan ke dispatcher utama `clean_file()`.
   - Mendukung penuh format: `.md`, `.html`, `.css`, `.js`, `.ts`, `.py`, `.php`, `.java`, `.cpp`, `.json`, `.xml`, `.yaml`, `.sql`, `.sh`, dll.
   - Menghapus karakter steganografi AI tak kasat mata (seperti **`Variation Selector-16 (U+FE0F)`**, zero-width spaces `\u200B`, joiners `\u200D`, tags block) dengan menjaga kelestarian baris (`newline=""`) dan struktur kode.
4. **Verifikasi Pengujian Otomatis (100% PASS Gate):**
   - Total kasus uji meningkat menjadi **21 unit tests** (termasuk verifikasi in-place cleaning pada berkas markdown).
   - Hasil pengujian: **100% PASS (21 Lulus, 0 Gagal, 0 Error)** dicatat di [`Docs/Test_Report.md`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/Docs/Test_Report.md).
5. **Kompilasi Ulang Executable Portabel (.exe):**
   - Sukses dikompilasi ulang menjadi [**`dist/MetaClean.exe`**](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/dist/MetaClean.exe) (Ukuran: 35.92 MB).
