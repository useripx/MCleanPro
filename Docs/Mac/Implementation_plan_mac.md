# Implementation Plan — Mrclean / MCleanPro Versi macOS

> **STATUS:** DRAFT UNTUK DITINJAU & DISETUJUI  
> **PROYEK:** Mrclean (MCleanPro macOS Release)  
> **PEMILIK PROYEK:** Yogi Ario  
> **PENYUSUN:** AI Agent (Pair Programmer)  
> **TANGGAL:** 6 November 2026  
> **BRANCH TARGET:** `develop` & `feature/macos-support`  
> **TIGA PRINSIP UTAMA (UNIVERSAL-RULE):**  
> 1. *No Plan, No Code.*  
> 2. *No Approval, No Code.*  
> 3. *No Evidence, No Completion. Pekerjaan tidak boleh dinyatakan selesai tanpa bukti verifikasi 100% PASS.*  

---

## 1. Ringkasan & Ruang Lingkup (Scope)

### 1.1 Masalah / Kebutuhan
Pengguna macOS (baik di arsitektur Intel maupun Apple Silicon M1/M2/M3/M4) membutuhkan aplikasi inspeksi metadata, pembersihan *lossless*, penghapusan steganografi AI, dan editor metadata yang berjalan secara **100% offline** tanpa ketergantungan pada runtime Python yang rumit bagi pengguna akhir.

### 1.2 Tujuan
Menyediakan bundel aplikasi mandiri macOS (**`Mrclean.app`**) dan paket installer Apple Disk Image (**`Mrclean.dmg`**) yang dapat diinstal dengan metode *Drag-and-Drop* ke folder `/Applications`, serta menyediakan pipa otomatisasi kompilasi cloud (**GitHub Actions**) agar proses build Mac dapat berjalan secara gratis tanpa mengharuskan kepemilikan laptop Mac fisik.

### 1.3 Batasan Ruang Lingkup (In-Scope vs Out-of-Scope)
- **Dalam Lingkup (In-Scope):**
  - **Generator Aset Apple (`.icns`):** Pembuatan skrip konversi aset resmi `Material/logo.jpg` menjadi format ikon standar Apple `assets/icon.icns` (multi-layer 16x16 hingga 1024x1024 Retina).
  - **Kompatibilitas GUI macOS:**
    - Penanganan pintasan keyboard macOS (`⌘ Command+C`, `⌘ Command+V`) pada form input `MetadataEditDialog`.
    - Integrasi font antarmuka native macOS (`SF Pro Text` / `.AppleSystemUIFont`).
    - Penanganan resolusi tinggi Retina Display (*HiDPI 2x*).
  - **Skrip Kompilasi Mac (`build_mac.py`):**
    - Otomatisasi PyInstaller dengan flag `--windowed --onedir` menghasilkan struktur bundel `Mrclean.app` lengkap dengan `Info.plist` dan ikon `.icns`.
    - Otomatisasi pengemasan `Mrclean.app` menjadi berkas installer disk image `dist/Mrclean-macOS.dmg` menggunakan utilitas native `hdiutil`.
  - **Otomatisasi CI/CD Cloud (GitHub Actions):**
    - Pembuatan workflow `.github/workflows/build-mac.yml` yang berjalan di runner `macos-latest` milik GitHub.
    - Menghasilkan artefak rilis `Mrclean-macOS.dmg` secara otomatis setiap kali ada tag rilis Git.
  - **Pengujian Unit Otomatis (100% PASS Gate):**
    - Memastikan seluruh 27 kasus uji unit test lulus tanpa galat di runner macOS.
- **Di Luar Lingkup (Out-of-Scope):**
  - Pembelian lisensi berbayar Apple Developer Program (\$99/tahun). Aplikasi akan didistribusikan dalam bentuk *Unsigned Independent Application* dengan panduan bypass Gatekeeper via klik kanan atau `xattr -cr`.
  - Distribusi via Mac App Store (karena memerlukan sandbox berbayar dari Apple).

---

## 2. Analisis Pilihan Solusi Kompilasi (Trade-Off Analysis)

| Pilihan Pendekatan | Kelebihan | Kekurangan | Rekomendasi |
| :--- | :--- | :--- | :---: |
| **Opsi 1: Kompilasi Lokal di Laptop Mac Fisik** | Pengujian instan langsung di layar nyata Mac; verifikasi UI interaktif langsung. | Membutuhkan perangkat keras Mac fisik; tidak semua pengembang memiliki Mac. | Opsional jika Mas Yogi memiliki Mac |
| **Opsi 2: Otomatisasi Cloud via GitHub Actions (macOS Runner)** | **100% Gratis**, tidak butuh laptop Mac fisik, otomatis mengompilasi biner Apple Silicon/Intel setiap push/release, langsung menghasilkan berkas `.dmg` siap unduh di halaman GitHub Releases. | Perlu konfigurasi file alur kerja YAML dan menunggu antrean build cloud (~3-5 menit). | **SANGAT DIREKOMENDASIKAN (PRIMARY)** |

---

## 3. Daftar Berkas Target yang Akan Dibuat / Dimodifikasi

### 3.1 Berkas Baru:
1. `src/utils/mac_icon_converter.py` — Skrip pembangun ikon `.icns` Apple dari `Material/logo.jpg`.
2. `build_mac.py` — Skrip kompilasi mandiri PyInstaller untuk macOS menghasilkan `dist/Mrclean.app` dan `dist/Mrclean-macOS.dmg`.
3. `.github/workflows/build-mac.yml` — Alur kerja GitHub Actions untuk build dan rilis otomatis macOS di cloud.
4. `Docs/Mac/Project_Overview_Mac.md` — Spesifikasi teknis kebutuhan pengembang Mac (Sudah dibuat).
5. `Docs/Mac/Implementation_plan_mac.md` — Rencana kerja ini.
6. `tests/test_mac_support.py` — Pengujian unit khusus kompatibilitas pathing POSIX dan resolusi aset macOS.

### 3.2 Berkas yang Dimodifikasi:
1. `src/gui/app.py` — Menambahkan deteksi platform (`sys.platform == 'darwin'`) untuk binding tombol `⌘ Command` dan font Mac.
2. `src/gui/dialogs/edit_dialog.py` — Menambahkan binding tombol `⌘ Command` untuk navigasi form input.
3. `Docs/Task_Status.md` & `Docs/Decision_Log.md` — Pencatatan status fase dan ADR-007 (Dukungan Ekosistem macOS).

### 3.3 Berkas Terlindungi (READ-ONLY):
- `Material/logo.jpg` & `Material/img.png` — Tetap tidak boleh diubah/dihapus (Pilar 4).

---

## 4. Tahapan Rencana Kerja (Batching)

### 📦 Batch 1: Penyiapan Generator Ikon Apple (`assets/icon.icns`)
- [ ] Buat modul `src/utils/mac_icon_converter.py`.
- [ ] Implementasikan pembuatan folder `assets/icon.iconset/` dengan 10 ukuran ikon standar Apple:
  - `icon_16x16.png`, `icon_16x16@2x.png` (32x32)
  - `icon_32x32.png`, `icon_32x32@2x.png` (64x64)
  - `icon_128x128.png`, `icon_128x128@2x.png` (256x256)
  - `icon_256x256.png`, `icon_256x256@2x.png` (512x512)
  - `icon_512x512.png`, `icon_512x512@2x.png` (1024x1024)
- [ ] Fallback generator: Pada sistem non-Mac, gunakan modul murni Pillow untuk membuat `.icns` sederhana, atau di Mac gunakan `iconutil -c icns assets/icon.iconset`.

### 📦 Batch 2: Penyesuaian Antarmuka & Pintasan Keyboard macOS
- [ ] Tambahkan helper platform di `src/gui/app.py`:
  ```python
  IS_MAC = sys.platform == "darwin"
  ```
- [ ] Jika `IS_MAC` aktif:
  - Atur shortcut: Tambahkan binding `<Command-KeyPress>` selain `<Control-KeyPress>`.
  - Sesuaikan font default ke `SF Pro Text` atau `.AppleSystemUIFont`.
  - Nonaktifkan window border yang tidak kompatibel dengan macOS Cocoa.

### 📦 Batch 3: Skrip Build PyInstaller macOS (`build_mac.py`)
- [ ] Buat skrip `build_mac.py` dengan konfigurasi PyInstaller:
  ```python
  cmd = [
      sys.executable, "-m", "PyInstaller",
      "--windowed",
      "--name=Mrclean",
      "--icon=assets/icon.icns",
      "--collect-all=customtkinter",
      "--collect-all=reportlab",
      "--add-data=assets:assets",
      "--clean", "-y",
      "src/main.py"
  ]
  ```
- [ ] Integrasikan perintah `hdiutil create` bawaan macOS untuk mengemas `dist/Mrclean.app` menjadi berkas installer siap unduh: `dist/Mrclean-macOS.dmg`.

### 📦 Batch 4: Otomatisasi Cloud via GitHub Actions CI/CD
- [ ] Buat berkas `.github/workflows/build-mac.yml`:
  - Runner: `macos-latest` (Apple Silicon M1/M2 / Sonoma).
  - Step 1: Checkout repository.
  - Step 2: Setup Python 3.13 dan pasang dependensi `requirements.txt`.
  - Step 3: Jalankan unit test (`python -m unittest discover -s tests -p "test_*.py" -v`) untuk membuktikan **100% PASS Gate**.
  - Step 4: Jalankan `python build_mac.py` untuk membangun `Mrclean.app` dan `Mrclean-macOS.dmg`.
  - Step 5: Unggah berkas `.dmg` ke GitHub Artifacts / GitHub Releases.

---

## 5. Rencana Pengujian & Kriteria Keberhasilan (100% PASS Gate)

- **Kasus Uji:**
  - Seluruh 27 unit test yang sudah ada wajib tetap lulus 100% PASS.
  - Penambahan unit test `tests/test_mac_support.py` untuk memverifikasi resolusi path macOS (`assets:assets` vs `assets;assets`) dan ketersediaan generator `.icns`.
- **Kriteria Kelulusan (Definition of Done):**
  - **100% PASS (0 GAGAL / 0 ERROR)** pada terminal pengujian.
  - Terciptanya installer `Mrclean-macOS.dmg` yang valid.

---

## 6. Analisis Risiko & Mitigasi

| Risiko | Dampak | Mitigasi Teknis |
| :--- | :--- | :--- |
| **Peringatan Keamanan Apple Gatekeeper** | Aplikasi diblokir saat pertama dibuka di Mac | Sertakan panduan resmi di `Docs/Mac/Project_Overview_Mac.md` dan `README.md` (Klik Kanan -> Open, atau `xattr -cr`). |
| **Pemisah Path PyInstaller (Windows `;` vs Mac `:`)** | Build error jika memakai sintaks Windows | Gunakan separator dinamis: `os.pathsep` (`";"` di Windows, `":"` di macOS). |
| **Ketiadaan Tkinter di Python Mac Bawaan** | Galat `ModuleNotFoundError: _tkinter` | Pada workflow CI/CD GitHub Actions, gunakan setup resmi Python yang sudah menyertakan Tcl/Tk. |

---

## 7. Gerbang Persetujuan (Approval Gate)

> 🛑 **Sesuai Pilar 1: Dilarang keras menulis atau mengubah kode aplikasi sebelum rencana implementasi ini disetujui secara eksplisit oleh Mas Yogi Ario.**

- [ ] Dokumen Rincian Spesifikasi Mac (`Docs/Mac/Project_Overview_Mac.md`) Disetujui
- [ ] Rencana Implementasi macOS (`Docs/Mac/Implementation_plan_mac.md`) Disetujui
- [ ] Izin Eksekusi Pengkodean Versi macOS Diberikan oleh Mas Yogi Ario
