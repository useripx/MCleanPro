# Decision Log (ADR) — MetaClean

> **STATUS DOKUMEN:** CATATAN KEPUTUSAN ARSITEKTUR AKTIF (ACTIVE ARCHITECTURE DECISION RECORD)  
> **PEMILIK PROYEK:** Yogi Ario  
> **OTORITAS:** Seluruh keputusan arsitektur kritis wajib disetujui secara tertulis oleh Yogi Ario sebelum diterapkan.  

---

## 📑 Indeks Rekaman Keputusan

| ID Keputusan | Tanggal | Topik / Fitur | Keputusan Singkat | Status |
| :---: | :---: | :--- | :--- | :---: |
| **ADR-001** | 31/10/2026 | Pemilihan Framework GUI & Runtime | Menggunakan Python 3.13 Desktop dengan CustomTkinter | `[APPROVED]` |
| **ADR-002** | 31/10/2026 | Lingkungan Eksekusi & Privasi | Beroperasi 100% Offline (Tanpa Jaringan / API Eksternal) | `[APPROVED]` |
| **ADR-003** | 31/10/2026 | Integrasi AI Watermark Remover | Mengadopsi modul dari `guillaumemeyer/watermarks-remover` | `[APPROVED]` |
| **ADR-004** | 31/10/2026 | Packaging & Branding | Membangun Standalone `.exe` dengan Ikon Kustom `img.png` | `[SUPERSEDED]` |
| **ADR-005** | 31/10/2026 | Branding Baru & Dukungan File Coding | Menggunakan `Material/logo.jpg` & Menambahkan `TextCleaner` untuk Markdown dan Seluruh Bahasa Pemrograman | `[APPROVED]` |

---

## 🏛️ Detail Rekaman Keputusan

### ADR-001 — Pemilihan Framework Desktop Python (CustomTkinter)
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Keputusan:** Menggunakan `CustomTkinter` karena berbasis standar Tkinter namun memberikan komponen UI kontemporer, responsif, dan mudah dibundel ke `.exe`.

### ADR-002 — Lingkungan Eksekusi 100% Offline
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Keputusan:** Seluruh pemrosesan metadata dan pembersihan watermark dijalankan secara lokal di memori komputer pengguna.

### ADR-003 — Integrasi Modul AI Watermark Remover
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Keputusan:** Mengintegrasikan logika algoritma pembersihan steganografi tersembunyi (zero-width spaces/variation selectors) dari repositori `guillaumemeyer/watermarks-remover`.

### ADR-004 — Packaging Awal dengan `img.png`
- **Status:** `[SUPERSEDED oleh ADR-005]`
- **Tanggal Usulan:** 31/10/2026
- **Keterangan:** Digantikan oleh ADR-005 karena Mas Yogi Ario menetapkan penggunaan `Material/logo.jpg`.

### ADR-005 — Branding Baru `Material/logo.jpg` & Pembersih Format Markdown serta Coding
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Pengusul:** Yogi Ario & AI Agent
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Konteks:** Mas Yogi menginstruksikan logo aplikasi diganti dengan `Material/logo.jpg` dan ditemukan kebutuhan pembersihan metadata/steganografi pada berkas Markdown (`.md`) serta berkas kode pemrograman (`.html`, `.js`, `.py`, `.php`, dll.).
- **Keputusan:**
  1. Menggunakan `Material/logo.jpg` sebagai sumber utama ikon Windows `assets/icon.ico` dan menampilkan `assets/logo.png` pada header GUI aplikasi.
  2. Mengimplementasikan `TextCleaner` yang mencakup pembersihan steganografi AI (`\uFE0F`, zero-width spaces, joiners) pada file Markdown dan seluruh format coding, serta mendaftarkannya ke dispatcher utama `clean_file()`.
- **Dampak:** Seluruh berkas teks dan koding dapat dibersihkan sekali klik baik secara per-file maupun batch satu folder.
