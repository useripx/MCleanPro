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
| **ADR-004** | 31/10/2026 | Packaging & Branding | Membangun Standalone `.exe` dengan Ikon Kustom `img.png` | `[APPROVED]` |

---

## 🏛️ Detail Rekaman Keputusan

### ADR-001 — Pemilihan Framework Desktop Python (CustomTkinter)
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Pengusul:** AI Agent & Yogi Ario
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Konteks:** Diperlukan aplikasi desktop yang ringan, modern, mudah dijalankan, dan mendukung tema Windows 10/11.
- **Keputusan:** Menggunakan `CustomTkinter` karena berbasis standar Tkinter namun memberikan komponen UI kontemporer, responsif, dan mudah dibundel ke `.exe`.

### ADR-002 — Lingkungan Eksekusi 100% Offline
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Konteks:** Menjamin keamanan privasi file pengguna agar tidak ada data atau metadata yang bocor ke internet.
- **Keputusan:** Seluruh pemrosesan metadata dan pembersihan watermark dijalankan secara lokal di memori komputer pengguna.

### ADR-003 — Integrasi Modul AI Watermark Remover
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Konteks:** Dokumen dan gambar hasil generasi AI modern sering disisipi *invisible steganographic tracking* (zero-width spaces/variation selectors) dan manifes C2PA.
- **Keputusan:** Mengintegrasikan logika algoritma pembersihan dari repositori `guillaumemeyer/watermarks-remover` ke dalam modul `src/watermarks/`.

### ADR-004 — Packaging Standalone Executable (.exe) & Ikon `img.png`
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Konteks:** Pengguna akhir menginginkan aplikasi praktis tanpa harus menginstal Python terlebih dahulu.
- **Keputusan:** Menggunakan `PyInstaller` dalam mode `--windowed` (tanpa jendela command prompt hitam), dan mengonversi berkas `Material/img.png` menjadi format Windows `.ico` untuk ikon jendela dan ikon aplikasi `.exe`.
