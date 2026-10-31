# Changelog — 10pm31102026

**Tanggal:** 31 Oktober 2026 (22:04 WIB)  
**Tipe Perubahan:** Pembaruan Branding & Perbaikan Pembersihan Markdown/Coding  
**Penyusun:** AI Agent (Pair Programmer)  
**Otoritas:** Yogi Ario  

---

### 🚀 Perubahan & Penambahan Baru
1. **Pembaruan Logo Baru (`Material/logo.jpg`):**
   - Berkas [`Material/logo.jpg`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/Material/logo.jpg) (2048x2048) ditetapkan sebagai logo resmi aplikasi.
   - Dikonversi menjadi ikon Windows multi-resolusi [`assets/icon.ico`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/assets/icon.ico) (16x16 hingga 256x256).
   - Dibuat aset visual [`assets/logo.png`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/assets/logo.png) dan disematkan langsung di header antarmuka CustomTkinter di sebelah teks **MetaClean**.
2. **Pembersih Format Markdown (.md) & Seluruh Berkas Coding:**
   - Dibuat modul [`src/cleaners/text_cleaner.py`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/src/cleaners/text_cleaner.py) dan didaftarkan ke dispatcher utama `clean_file()`.
   - Mengatasi kendala di mana berkas `.md` (seperti `README.md` dengan karakter `\uFE0F` Variation Selector-16) sebelumnya ditolak oleh tombol *"Bersihkan Metadata Terpilih"*.
   - Mendukung penuh seluruh format bahasa pemrograman dan markup:
     - Markdown: `.md`, `.markdown`
     - Web Front-End: `.html`, `.htm`, `.css`, `.scss`, `.js`, `.jsx`, `.ts`, `.tsx`, `.vue`, `.svelte`
     - Back-End & Bahasa Umum: `.py`, `.php`, `.java`, `.c`, `.cpp`, `.cs`, `.go`, `.rs`, `.rb`, `.swift`, `.kt`, `.dart`
     - Data & Config: `.json`, `.xml`, `.yaml`, `.yml`, `.toml`, `.ini`, `.sql`, `.sh`, `.bat`, `.ps1`
   - Membersihkan seluruh tanda steganografi tak kasat mata (`\uFE0F`, zero-width spaces `\u200B`, `\u200D`, tags block) tanpa mengubah sintaks kode atau teks asli.
3. **Verifikasi Pengujian Otomatis (100% PASS Gate):**
   - Total kasus uji meningkat menjadi **20 unit tests** (termasuk verifikasi pembersihan Markdown dengan `\uFE0F`, HTML, dan script Python).
   - Hasil pengujian: **100% PASS (20 Lulus, 0 Gagal, 0 Error)** dicatat di [`Docs/Test_Report.md`](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/Docs/Test_Report.md).
4. **Kompilasi Ulang Executable Portabel (.exe):**
   - Sukses dikompilasi ulang menjadi [**`dist/MetaClean.exe`**](file:///e:/Dokumen/UNP/Teknik%20Informatika/Projek/cek%20metadata/dist/MetaClean.exe) (Ukuran: 35.92 MB) dengan logo dan modul pembersih koding terbaru.
