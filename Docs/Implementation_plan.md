# Implementation Plan — MetaClean: Offline Metadata Inspector, Cleaner & AI Watermarks Remover

> **STATUS:** DISETUJUI (APPROVED)  
> **PROYEK:** MetaClean  
> **PEMILIK PROYEK:** Yogi Ario  
> **PENYUSUN:** AI Agent (Pair Programmer)  
> **TANGGAL PERSETUJUAN:** 31/10/2026  
> **BRANCH TERKAIT:** `develop` & `feature/metaclean-core`  
> **PRINSIP UTAMA:** *No Plan, No Code. No Approval, No Code. No Evidence, No Completion.*  

---

## 1. Ringkasan & Ruang Lingkup

### 1.1 Masalah / Latar Belakang
Pengguna sering kali membagikan gambar, dokumen, atau teks di internet tanpa menyadari bahwa file tersebut menyimpan metadata sensitif (seperti lokasi GPS rumah, identitas kamera, nama asli penulis, software yang digunakan, dan tanggal pembuatan). Selain itu, teks dan media yang dihasilkan oleh kecerdasan buatan (ChatGPT, Claude, dsb.) sering disisipi *watermark* tersembunyi (*invisible zero-width unicode characters*, *C2PA provenance manifests*, dan *steganography*).

Dibutuhkan sebuah aplikasi desktop Windows yang bekerja **100% offline** (tanpa koneksi internet, tanpa risiko kebocoran data) untuk:
1. Memeriksa dan menganalisis metadata secara transparan baik **per berkas (single file)** maupun **sekaligus dalam satu folder (batch folder scan)**.
2. Membersihkan metadata identitas secara *lossless* (kualitas visual/audio tidak berkurang) untuk satu berkas atau seluruh isi folder.
3. Mendeteksi dan menghapus tanda air tersembunyi AI (berbasis algoritma `guillaumemeyer/watermarks-remover`).
4. Berjalan sebagai file eksekusi mandiri tunggal (`.exe`) dengan ikon kustom `Material/img.png`.

### 1.2 Tujuan
Menghasilkan aplikasi desktop Windows berbasis Python (CustomTkinter) yang dikemas menjadi satu file eksekusi `.exe` portabel, responsif, modern, dan lulus uji otomatis 100% PASS.

### 1.3 Batasan Ruang Lingkup (In-Scope vs Out-of-Scope)
- **Dalam Lingkup (In-Scope):**
  - **Dukungan Pemrosesan File Tunggal & Folder Batch:**
    - Tombol "Pilih Berkas" untuk analisis per file.
    - Tombol "Pilih Folder" untuk memindai seluruh dokumen/gambar/media dalam satu folder (termasuk opsi subfolder).
    - Drag-and-drop file tunggal, multi-file, maupun folder langsung ke jendela aplikasi.
  - **Inspeksi Metadata:**
    - Gambar: JPEG, PNG, WEBP, TIFF (EXIF tags, GPS, kamera, software, dimensi).
    - Dokumen: PDF (Author, Creator, Producer, ModDate, CreationDate), DOCX (Word Core Properties), XLSX.
    - Audio & Video: MP3, MP4, WAV, MKV (ID3 metadata, encoder, bitrate, duration).
    - Teks: Karakter Unicode tak kasat mata (zero-width spaces, joiners, variation selectors).
  - **Pembersihan Metadata (Metadata Cleaner):**
    - Penghapusan seluruh tag EXIF/GPS/Device info pada gambar.
    - Penghapusan author/history pada PDF dan dokumen DOCX.
    - Pembersihan tag ID3/encoder pada media audio/video.
    - Mode pembersihan: Simpan sebagai file baru (misal `namafile_clean.ext`) atau simpan ke folder tujuan output khusus.
  - **AI Watermarks & Provenance Removal (`watermarks-remover`):**
    - Deteksi dan pembersihan steganografi Unicode teks AI (zero-width characters, variation selectors).
    - Deteksi dan pembersihan segmen metadata C2PA pada berkas media.
  - **Antarmuka Desktop GUI:**
    - CustomTkinter dengan Dark/Light Mode.
    - Tabel antrean berkas (menampilkan nama, tipe, status metadata, status watermark).
    - Panel inspeksi detail (key-value metadata per kategori).
    - Tombol aksi batch: "Bersihkan Semua Berkas di Folder", "Hapus Watermark", dan "Ekspor Laporan Metadata (JSON/TXT)".
  - **Packaging:**
    - Skrip otomatisasi build PyInstaller menjadi berkas `.exe` portabel.
    - Konversi otomatis aset mentah `Material/img.png` menjadi format ikon Windows `assets/icon.ico`.
- **Di Luar Lingkup (Out-of-Scope):**
  - Koneksi ke server cloud / online API (Aplikasi murni offline).
  - Editing konten isi foto (seperti inpainting / crop visual gambar) — fokus pada metadata dan watermark steganografi.

---

## 2. Analisis Kondisi Saat Ini & Pilihan Solusi

### 2.1 Kondisi & Dependensi
- **Runtime:** Python 3.13.0 terpasang di sistem (`C:\laragon\bin\python\python-3.13`).
- **Aset:** `Material/img.png` (berkas mentah yang disediakan Mas Yogi Ario, terlindungi status READ-ONLY).
- **Pustaka Python Terpilih:**
  - `customtkinter`: GUI modern native look.
  - `Pillow`: Pengolahan gambar, ekstraksi EXIF, pembersihan tag gambar, dan konversi ikon `img.png` ke `.ico`.
  - `pypdf`: Ekstraksi dan sanitasi metadata PDF.
  - `mutagen`: Ekstraksi dan sanitasi metadata audio dan video.
  - `pyinstaller`: Pengemasan aplikasi menjadi `.exe`.

### 2.2 Pilihan Pendekatan Solusi (Trade-off Analysis)

#### Opsi A: Integrasi Core Standalone + CustomTkinter + PyInstaller (Direkomendasikan)
- **Kelebihan:** 
  - Tidak ada dependensi server lokal.
  - Sangat cepat, ukuran file wajar, performa native di Windows 10/11.
  - Modul engine (Inspector/Cleaner/Watermark) dibuat terpisah murni (Python standard + library ringan), sehingga sangat mudah diuji menggunakan `unittest` (100% PASS Gate).
- **Kekurangan:** Perlu penanganan kompatibilitas PyInstaller untuk CustomTkinter assets.
- **Mitigasi:** Telah disiapkan skrip build `build_exe.py` yang otomatis menyertakan folder tema CustomTkinter dan file ikon.

---

## 3. Daftar Berkas Target

### Berkas yang Akan Dibuat Baru:
1. `requirements.txt` — Daftar dependensi Python resmi.
2. `src/__init__.py`
3. `src/utils/icon_converter.py` — Pengonversi `Material/img.png` ke `assets/icon.ico`.
4. `src/inspectors/__init__.py`
5. `src/inspectors/base.py` — Base class inspector.
6. `src/inspectors/image_inspector.py` — Inspektor EXIF/GPS/Kamera.
7. `src/inspectors/pdf_inspector.py` — Inspektor PDF metadata.
8. `src/inspectors/audio_video_inspector.py` — Inspektor audio/video tags.
9. `src/inspectors/text_inspector.py` — Inspektor teks & invisible Unicode.
10. `src/cleaners/__init__.py`
11. `src/cleaners/base.py` — Base class cleaner.
12. `src/cleaners/image_cleaner.py` — Pembersih EXIF *lossless*.
13. `src/cleaners/pdf_cleaner.py` — Pembersih PDF metadata.
14. `src/cleaners/media_cleaner.py` — Pembersih media audio/video.
15. `src/watermarks/__init__.py`
16. `src/watermarks/ai_cleaner.py` — Pembersih invisible Unicode & C2PA provenance (dari `watermarks-remover`).
17. `src/gui/__init__.py`
18. `src/gui/app.py` — Jendela utama CustomTkinter, drag-and-drop, tab inspector & cleaner.
19. `src/main.py` — Entry point utama aplikasi.
20. `build_exe.py` — Skrip build PyInstaller otomatis dengan ikon kustom `icon.ico`.
21. `tests/test_inspectors.py` — Unit test ekstraksi metadata.
22. `tests/test_cleaners.py` — Unit test pembersihan metadata.
23. `tests/test_watermarks.py` — Unit test pembersihan AI watermark.

### Berkas yang Dilindungi (READ-ONLY):
- `Material/img.png` — Dilarang diubah/dihapus.

---

## 4. Rencana Tahapan Implementasi (Batching)

### 📦 Batch 1: Fondasi Modul Engine & Automated Tests (100% PASS Gate)
- [ ] Buat file `requirements.txt`.
- [ ] Implementasikan `src/inspectors/` (Image, PDF, Media, Text).
- [ ] Implementasikan `src/cleaners/` (Image, PDF, Media).
- [ ] Implementasikan `src/watermarks/` (AI text steganography & C2PA cleaner).
- [ ] Buat suite pengujian lengkap di `tests/` dan jalankan hingga menghasilkan **100% PASS (0 GAGAL / 0 ERROR)**.
- [ ] Perbarui `Docs/Test_Report.md`.

### 📦 Batch 2: Antarmuka Desktop GUI (CustomTkinter)
- [ ] Konversi `Material/img.png` ke `assets/icon.ico` menggunakan skrip utilitas.
- [ ] Implementasikan `src/gui/app.py` dengan komponen:
  - Header & Status Bar.
  - Zona Drop File / Tombol Pilih Berkas & Folder.
  - Tabel Daftar Berkas & Pratinjau Metadata.
  - Tombol Aksi: "Bersihkan Metadata Terpilih", "Hapus Watermark AI", "Bersihkan Semua".
- [ ] Integrasikan GUI dengan modul engine dari Batch 1.
- [ ] Uji fungsionalitas GUI dan penanganan error file korup.

### 📦 Batch 3: Packaging Standalone Executable (.exe) & Rilis
- [x] Buat skrip `build_exe.py` untuk menjalankan PyInstaller dengan flag `--windowed --onefile --icon=assets/icon.ico`.
- [x] Eksekusi proses build dan verifikasi hasil di `dist/MetaClean.exe`.
- [x] Verifikasi bahwa `.exe` dapat dibuka secara mandiri dan seluruh fitur bekerja 100% offline.
- [x] Catat changelog final di `changelog/`.

### 📦 Batch 4: Pembaruan Logo ke Material/logo.jpg & Pembersih Format Markdown (.md) serta Berkas Coding (.html, .js, .py, dll.)
- [ ] **Pembaruan Logo Baru (Material/logo.jpg):**
  - Konversi aset `Material/logo.jpg` menjadi `assets/icon.ico` (multi-resolusi 16x16 hingga 256x256).
  - Buat berkas `assets/logo.png` untuk ditampilkan langsung pada header jendela GUI aplikasi.
  - Perbarui `build_exe.py` untuk mengemas aplikasi dengan ikon baru.
- [ ] **Perbaikan Pembersih Markdown (.md) & Seluruh Format Berkas Coding:**
  - Dukungan format: `.md`, `.html`, `.css`, `.js`, `.jsx`, `.ts`, `.tsx`, `.vue`, `.php`, `.py`, `.java`, `.c`, `.cpp`, `.cs`, `.go`, `.rs`, `.json`, `.xml`, `.yaml`, `.sql`, `.sh`.
  - Buat `src/cleaners/text_cleaner.py` untuk membersihkan steganografi AI (zero-width spaces, variation selector `\uFE0F`, dsb.) dari file `.md` dan seluruh berkas bahasa pemrograman / coding.
  - Daftarkan `TextCleaner` ke dalam `src/cleaners/__init__.py`.
  - Tambahkan unit test verifikasi pembersihan file markdown dan kode di `tests/test_cleaners.py`.
  - Eksekusi automated test suite hingga **100% PASS (0 GAGAL / 0 ERROR)**.
  - Re-build berkas executable `dist/MetaClean.exe`.

---

## 5. Rencana Pengujian & Kriteria Keberhasilan (100% PASS Gate)

### 5.1 Pengujian Otomatis
- **Perintah:** `python -m unittest discover -s tests -p "*_test.py"`
- **Kasus Uji:**
  1. `test_image_exif_extraction`: Membaca EXIF gambar sampel.
  2. `test_image_cleaner_lossless`: Memastikan seluruh EXIF hilang dan dimensi/data gambar tetap utuh.
  3. `test_pdf_metadata_extraction_and_cleaning`: Membaca dan menghapus author/modDate PDF.
  4. `test_ai_unicode_watermark_removal`: Menghapus invisible characters (`\u200b`, `\u200d`, dsb.) dari string teks tanpa mengubah kata asli.
  5. `test_c2pa_manifest_removal`: Mendeteksi dan membersihkan struktur C2PA.
- **Kriteria Kelulusan:** `100% PASS (0 GAGAL / 0 ERROR)`.

---

## 6. Analisis Risiko & Mitigasi

- **Risiko 1: Kerusakan File Asli Saat Pembersihan:**
  - *Mitigasi:* Secara default, aplikasi selalu menyimpan file hasil pembersihan sebagai file baru (contoh: `namafile_clean.jpg`) di folder yang sama atau folder output pilihan pengguna. File asli tidak pernah diubah tanpa izin pengguna.
- **Risiko 2: Windows Defender False-Positive pada Executable Baru:**
  - *Mitigasi:* Menggunakan PyInstaller resmi dari virtual environment bersih tanpa library mencurigakan dan menyertakan manifest aplikasi yang valid.

---

## 7. Gerbang Persetujuan (Approval Gate)

> 🛑 **Dilarang keras mengeksekusi kode aplikasi sebelum Yogi Ario memberikan persetujuan eksplisit terhadap rencana ini.**

- [x] Batch 1-3 Disetujui & Selesai (31/10/2026)
- [x] **Batch 4: Pembaruan Logo (`Material/logo.jpg`) & Pembersih Markdown + Berkas Coding**
  - Status Persetujuan: **DISETUJUI (APPROVED)**
  - Tanggal Persetujuan: `31/10/2026 21:56 WIB`
  - Catatan Pemilik Proyek: *"oke gas tambahkan bisa html, dll yang berformat coding"*

---

## 8. Rencana Implementasi Pembaruan Mendatang (Batch 5: Mrclean v2.0)

> **STATUS:** DRAFT / MENUNGGU PERSETUJUAN (PENDING REVIEW)  
> **FITUR TARGET:** Pilihan Format Ekspor Laporan (Radio Button: PDF vs Markdown) & Fitur Edit Metadata Selektif (Misal: Ganti Author Saja)  
> **TIGA PRINSIP UTAMA:**  
> 1. *No Plan, No Code.*  
> 2. *No Approval, No Code.*  
> 3. *No Evidence, No Completion. Pekerjaan tidak boleh dinyatakan selesai tanpa bukti verifikasi yang sesuai.*  

### 8.1 Riset Kemampuan Berkas AI (Generative AI Provenance & Markers)
Berdasarkan investigasi standar industri (C2PA, DeepMind SynthID, OpenAI, Midjourney, Stable Diffusion):
- **Gambar:** Mengandung C2PA manifests (APP11 JUMBF), IPTC `trainedAlgorithmicMedia`, PNG text chunks (prompt & workflow node graph pada SD/ComfyUI), EXIF UserComment (Midjourney), dan SynthID (Google DeepMind).
- **Teks/Kode:** Mengandung invisible Unicode steganography (`\u200B`, `\uFE0F`, zero-width joiners), SynthID statistical tokens, header signature comments.
- **Dokumen (PDF/Word):** Menyematkan Author AI (`ChatGPT`, `Python-docx`, `ReportLab`), toolchain metadata, dan XMP metadata.
- **Audio/Video:** Menyematkan ID3 encoder signatures, SynthID audio inaudible frequencies, dan C2PA media manifests.

### 8.2 Modul 1: Dialog Pilihan Format Ekspor Laporan (Radio Button)
- **Tujuan:** Memberikan kemudahan bagi pengguna saat mengekspor laporan inspeksi berkas melalui dialog popup interaktif.
- **Komponen UI:**
  - Jendela modal popup CustomTkinter saat tombol *"💾 Ekspor Laporan..."* ditekan.
  - Radio button group:
    - `(•) Dokumen PDF (.pdf)`: Laporan formal siap cetak dengan kop/header logo resmi `Material/logo.jpg`, tabel ringkasan antrean berkas, dan kartu detail per berkas.
    - `( ) Berkas Markdown (.md)`: Laporan terstruktur berformat GitHub-flavored Markdown dengan tabel dan badge status visual (`✅ Bersih`, `⚠️ Metadata`, `🤖 AI-WM`).
  - Tombol aksi: `[ Batal ]` dan `[ Lanjutkan Ekspor ]`.
- **Modul Backend:**
  - `src/utils/md_exporter.py`: Engine penyusun teks laporan Markdown berformat rapi.
  - `src/utils/pdf_exporter.py`: Engine penyusun dokumen PDF menggunakan pustaka `reportlab`.

### 8.3 Modul 2: Fitur Edit Metadata Selektif / Granular (Metadata Editor)
- **Tujuan:** Memungkinkan pengguna menyunting nilai atribut metadata tertentu secara selektif (misalnya hanya mengganti field **Author / Pembuat** saja) sementara atribut lainnya (kamera, tanggal, resolusi, copyright) **dipertahankan 100% utuh**.
- **Cakupan Pengubahan per Format Berkas:**
  - **Gambar (JPEG, PNG, TIFF):** Tag EXIF `Artist / Author`, `ImageDescription / Title`, `Copyright`, `Software`, `DateTimeOriginal`.
  - **Dokumen PDF:** Metadata dokumen `Author`, `Title`, `Subject`, `Keywords`, `Creator`.
  - **Dokumen Word (.docx):** Properti inti `Author`, `Title`, `Subject`, `Keywords`, `Category`, `Comments`.
  - **Media Audio/Video (MP3, MP4):** Tag ID3 `Title`, `Artist`, `Album`, `Year`, `Genre`.
- **Komponen UI:**
  - Tombol baru *"✏️ Edit Metadata"* di panel kontrol bawah aplikasi.
  - Jendela form modal yang dinamis menampilkan nilai saat ini (pre-filled), pengguna hanya mengubah field yang diinginkan.
  - Opsi penyimpanan: Simpan langsung di tempat (*In-Place*) atau simpan sebagai salinan (*Copy*).
  - Refresh otomatis pada daftar berkas dan panel detail setelah penyimpanan berhasil.
- **Modul Backend:**
  - `src/editors/base.py` & `src/editors/__init__.py`: Interface dan dispatcher editor.
  - `src/editors/image_editor.py`, `pdf_editor.py`, `docx_editor.py`, `media_editor.py`.

### 8.4 Rencana Verifikasi Pengujian (100% PASS Gate - No Evidence, No Completion)
- Kasus uji unit test baru pada `tests/test_editors.py`, `tests/test_md_exporter.py`, dan `tests/test_pdf_exporter.py`.
- Wajib menyertakan bukti log eksekusi terminal bahwa suite pengujian menghasilkan **100% PASS (0 GAGAL / 0 ERROR)** sebelum pengemasan executable `.exe`.

### 8.5 Gerbang Persetujuan & Status Penyelesaian Batch 5
- [x] Modul 1 (Ekspor Radio Button: PDF vs Markdown) Disetujui Mas Yogi Ario
- [x] Modul 2 (Editor Metadata Selektif) Disetujui Mas Yogi Ario
- [x] Izin Eksekusi Pengkodean Diberikan Mas Yogi Ario (31/10/2026 22:47 WIB)
- [x] Verifikasi 27 Kasus Uji Otomatis: **100% PASS (0 GAGAL / 0 ERROR)**
- [x] Re-Packaging Executable: Berhasil dikompilasi ke `dist/Mrclean.exe` & `Mrclean.exe` (42.00 MB)

---

## 9. Rencana Implementasi Branch `fix/select-item` (Fitur Pemilihan Multi-Berkas)

> **STATUS:** DRAFT UNTUK DITINJAU & DISETUJUI  
> **PROYEK:** Mrclean (MCleanPro)  
> **PEMILIK PROYEK:** Yogi Ario  
> **BRANCH:** `fix/select-item`  
> **TANGGAL:** 9 November 2026  
> **TIGA PRINSIP UTAMA:**  
> 1. *No Plan, No Code.*  
> 2. *No Approval, No Code.*  
> 3. *No Evidence, No Completion.*  

### 9.1 Masalah & Kebutuhan
Saat ini pengguna hanya dapat memilih satu per satu berkas (*single select*) untuk dibersihkan, atau harus langsung membersihkan seluruh isi folder sekaligus (*all items*). Pengguna membutuhkan fleksibilitas untuk **mencentang beberapa berkas tertentu saja** (misal 3 dari 10 berkas) untuk diproses secara bersamaan.

### 9.2 Rancangan Solusi & Antarmuka (UI/UX)
1. **Master Control "Pilih Semua" (Select All Header):**
   - Pada header panel daftar berkas sebelah kiri, ditambahkan kontrol:
     - Checkbox Master: `[ ] Pilih Semua` yang otomatis mencentang atau membatalkan centang pada seluruh berkas di daftar.
     - Label indikator jumlah: `(X dari Y berkas dipilih)`.
2. **Checkbox per Baris Berkas (Row Checkboxes):**
   - Menambahkan komponen `ctk.CTkCheckBox` di setiap baris berkas di panel kiri.
   - Mengklik nama berkas tetap membuka pratinjau detail di panel kanan.
   - State berkas terpilih disimpan dalam himpunan `self.selected_file_paths = set()`.
3. **Eksekusi Aksi Pembersihan Multi-Berkas:**
   - Tombol **"🛡️ Bersihkan Berkas Terpilih"**:
     - Jika ada beberapa berkas yang dicentang, tombol akan membersihkan seluruh berkas terpilih tersebut dalam alur kerja batch berlatar belakang (*threading*).
     - Menampilkan konfirmasi dan laporan keberhasilan: *"X berkas berhasil dibersihkan."*
   - Tombol **"🤖 Hapus Watermark AI Saja"**:
     - Mendukung pembersihan tanda air pada seluruh berkas yang dicentang.
   - **Mekanisme Fallback:** Jika tidak ada checkbox yang dicentang namun ada satu berkas yang sedang aktif dilihat di panel detail, aksi otomatis berlaku pada berkas aktif tersebut.

### 9.3 Daftar Berkas yang Terlibat
- `src/gui/app.py` — Implementasi state selection, checkbox per baris, select-all control, dan modifikasi handler pembersihan.
- `tests/test_multi_select.py` — Pengujian unit logika batch pembersihan untuk daftar berkas terpilih.
- `Docs/Task_Status.md` & `Docs/Decision_Log.md` — Pembaruan status tugas dan pencatatan ADR.

### 9.4 Rencana Pengujian (100% PASS Gate)
- Menjalankan seluruh test suite yang ada (27 tests) ditambah kasus uji baru untuk memastikan tidak ada regresi dan hasil pengujian **100% PASS (0 GAGAL / 0 ERROR)**.

### 9.5 Gerbang Persetujuan (Approval Gate)
- [x] Rencana Fitur Pemilihan Multi-Berkas Disetujui Mas Yogi Ario
- [x] Izin Eksekusi Pengkodean pada Branch `fix/select-item` Diberikan Mas Yogi Ario
- [x] Verifikasi 29 Kasus Uji Otomatis: **100% PASS (0 GAGAL / 0 ERROR)**
- [x] Re-Packaging Executable: Berhasil dikompilasi ke `dist/Mrclean.exe` & `Mrclean.exe` (42.00 MB)
- [x] Berhasil di-merge ke branch `develop` (Pull Request #1)

---

## 10. Rencana Implementasi Branch `fix/majorupdatev1` (Major Update v1 & Kebijakan Kebersihan Branch `main`)

> **STATUS:** DRAFT UNTUK DITINJAU & DISETUJUI  
> **PROYEK:** Mrclean (MCleanPro)  
> **PEMILIK PROYEK:** Yogi Ario  
> **BRANCH:** `fix/majorupdatev1`  
> **TANGGAL:** 09 November 2026  
> **TIGA PRINSIP UTAMA:**  
> 1. *No Plan, No Code.*  
> 2. *No Approval, No Code.*  
> 3. *No Evidence, No Completion.*  

### 10.1 Kebijakan Kebersihan Branch `main` (Production-Only Repository)
Sesuai arahan Mas Yogi Ario, branch `main` **WAJIB BERSIH** hanya memuat berkas-berkas esensial aplikasi (Production-Ready):
- **Diperbolehkan di `main`:** `src/`, `assets/`, `Material/`, `requirements.txt`, `README.md`, `LICENSE`, `build_exe.py`.
- **Dilarang di `main` (Hanya sampai `develop`):** `Docs/` (Task Status, Decision Log, Plans, Chat Logs, Mac), `changelog/`, `AGENTS.md`, `GEMINI.md`.
- **Mekanisme Eksekusi:** Menyiapkan skrip rilis otomatis `tools/sync_to_main.py` yang otomatis mengisolasi dan memangkas folder catatan pengembangan saat perilisan ke `main`.

### 10.2 Rincian Fitur Utama yang Dikembangkan
1. **🛡️ Privacy Risk Scoring Engine (0–100%) & Visual Badges:**
   - Mesin pembobot kerentanan privasi (`src/inspectors/risk_scorer.py`).
   - Tingkat bahaya: 🔴 KRITIS (≥70%), 🟡 SEDANG (30–69%), 🟢 AMAN (0–29%).
   - Tampilan visual bar di panel detail, badge warna di daftar antrean, dan kolom skor pada laporan ekspor PDF & Markdown.
2. **⚡ Quick Clean Presets (Pembersihan Cepat Berbasis Profil):**
   - Modul `src/cleaners/preset_cleaner.py` dengan preset: Media Sosial (jaga orientasi & sRGB), Akademik/Jurnal (bersihkan author & steganografi AI), dan Developer/OSS (bersihkan header & path lokal).
3. **🤖 AI Generative & C2PA Forensics (Prompt Viewer & Stripper):**
   - Deteksi prompt Midjourney, Stable Diffusion, DALL-E, dan manifes C2PA Adobe (`src/inspectors/ai_forensics.py`).
   - Tombol pembersih khusus C2PA & Prompt AI (`src/cleaners/c2pa_cleaner.py`).
4. **🎭 Metadata Spoofing & Anonymizer (Generator Metadata Palsu):**
   - Modul `src/editors/spoofing.py` untuk menginjeksi metadata sintetis acak dan wajar agar berkas tidak dicurigai sistem *exif-stripper detection*.
5. **🖱️ Integrasi Klik Kanan Windows Explorer (Shell Context Menu):**
   - Modul `src/utils/shell_integration.py` yang mendaftarkan shortcut pembersihan langsung di menu klik kanan Windows Explorer (beroperasi 100% pada `HKCU` tanpa butuh akses Administrator).

### 10.3 Tahapan Pengerjaan Bertahap (Execution Batches)
- **Batch 1:** Engine Privacy Risk Scoring + Integrasi UI & Exporters + Unit Test.
- **Batch 2:** Quick Clean Presets Engine + UI Toolbar + Unit Test.
- **Batch 3:** AI Generative & C2PA Forensics + Prompt Viewer + Unit Test.
- **Batch 4:** Metadata Spoofing & Anonymizer + Dialog GUI + Unit Test.
- **Batch 5:** Integrasi Klik Kanan Windows Explorer (HKCU) + Unit Test.
- **Batch 6:** Setup Skrip Rilis Bersih Branch `main` (`tools/sync_to_main.py`).
- **Batch 7:** Verifikasi Pengujian Otomatis 100% PASS Gate & Build `dist/Mrclean.exe`.

### 10.4 Gerbang Persetujuan (Approval Gate)
- [ ] Rencana Implementasi Major Update v1 Disetujui Mas Yogi Ario
- [ ] Kebijakan Kebersihan Branch `main` Disetujui Mas Yogi Ario
- [ ] Izin Eksekusi Pengkodean pada Branch `fix/majorupdatev1` Diberikan Mas Yogi Ario




