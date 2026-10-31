# Task Status — MetaClean (Metadata & Watermark Remover Desktop)

> **STATUS PROYEK KESELURUHAN:** `In Progress`  
> **PROGRES GLOBAL:** `15%`  
> **PEMILIK PROYEK:** Yogi Ario  
> **TERAKHIR DIPERBARUI:** 31/10/2026 20:55 WIB  

---

## 1. Ringkasan Progres per Fase

| Fase | Nama Fase / Milestone | Bobot (%) | Status | Catatan Singkat |
| :---: | :--- | :---: | :---: | :--- |
| **Fase 1** | Setup Tata Kelola, Struktur Direktori & Aturan | 15% | `[COMPLETED]` | Git repo, .gitignore, Docs/, Material/ |
| **Fase 2** | Desain Arsitektur & Perencanaan (Implementation Plan) | 15% | `[IN PROGRESS]` | Penyusunan draf menunggu Approval Gate Mas Yogi |
| **Fase 3** | Implementasi Engine Inspektor, Cleaner & Watermark | 35% | `[NOT STARTED]` | Python backend logic |
| **Fase 4** | Implementasi GUI Desktop (CustomTkinter & Drag-Drop) | 20% | `[NOT STARTED]` | Antarmuka pengguna |
| **Fase 5** | Pengujian Otomatis 100% PASS, Build .exe & Rilis | 15% | `[NOT STARTED]` | PyInstaller bundling dengan img.png |
| **TOTAL** | | **100%** | **`15%`** | |

---

## 2. Rincian Checklist Tugas per Fase

### 📌 Fase 1: Setup Tata Kelola, Struktur Direktori & Aturan
- [x] Konfigurasi `.gitignore` dan `.env.example`.
- [x] Salin dan amankan aset desain mentah `img.png` ke folder `Material/` (READ-ONLY).
- [x] Inisialisasi berkas panduan AI `AGENTS.md` dan `GEMINI.md`.
- [x] Migrasi dan standarisasi kerangka kerja `Docs/universal-rule.md`.
- [x] Konfigurasi branch `main` dan `develop`.

### 📌 Fase 2: Desain Arsitektur & Perencanaan (Implementation Plan)
- [x] Penyusunan `Docs/Implementation_plan.md` mencakup Cek Metadata, Pembersih Metadata, Watermark Remover, GUI, dan packaging `.exe`.
- [ ] Peninjauan dan persetujuan eksplisit dari Mas Yogi Ario (*Approval Gate*).

### 📌 Fase 3: Implementasi Engine Core
- [ ] Modul `inspectors`: Ekstraksi EXIF gambar, GPS, metadata dokumen PDF/Word, dan audio/video tags.
- [ ] Modul `cleaners`: Pembersihan metadata *lossless* untuk gambar, dokumen, dan media.
- [ ] Modul `watermarks`: Deteksi dan pembersihan invisible Unicode steganography (berbasis `guillaumemeyer/watermarks-remover`) & metadata C2PA.

### 📌 Fase 4: Antarmuka Pengguna (GUI Desktop)
- [ ] Integrasi antarmuka CustomTkinter modern (Dark/Light mode).
- [ ] Fitur *drag-and-drop* file dan folder.
- [ ] Panel pratinjau tabel metadata dan tombol aksi cepat (Bersihkan Metadata / Hapus Watermark).

### 📌 Fase 5: Pengujian Otomatis & Packaging .exe
- [ ] Automated Test Suite di `tests/` dengan target `100% PASS (0 GAGAL / 0 ERROR)`.
- [ ] Konversi `Material/img.png` menjadi `assets/icon.ico`.
- [ ] Build standalone `.exe` menggunakan PyInstaller dengan ikon kustom `icon.ico`.
- [ ] Pengujian file `.exe` di lingkungan Windows offline.

---

## 3. Log Kendala & Masalah Aktif (Blocker Log)

| ID | Tanggal Ditemukan | Deskripsi Kendala / Blocker | Dampak | Rencana Penyelesaian | Status |
| :---: | :---: | :--- | :--- | :--- | :---: |
| - | - | Tidak ada kendala aktif saat ini. | - | - | `[RESOLVED]` |

---

## 4. Riwayat Sesi Pengerjaan Terakhir

- **31/10/2026 - 20:55 WIB:** Inisialisasi struktur proyek, migrasi tata kelola universal ke `Docs/`, penempatan aset `Material/img.png`, penyusunan `changelog08pm31102026.md`, dan perumusan `Implementation_plan.md`.
