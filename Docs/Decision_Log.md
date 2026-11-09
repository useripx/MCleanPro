# Decision Log (ADR) — MetaClean

> **STATUS DOKUMEN:** CATATAN KEPUTUSAN ARSITEKTUR AKTIF (ACTIVE ARCHITECTURE DECISION RECORD)  
> **PEMILIK PROYEK:** Yogi Ario  
> **OTORITAS:** Seluruh keputusan arsitektur kritis wajib disetujui secara tertulis oleh Yogi Ario sebelum diterapkan.  

---

## 📑 Indeks Rekaman Keputusan

| ID Keputusan | Tanggal | Topik / Fitur | Keputusan Singkat | Status |
| :---: | :---: | :--- | :--- | :--- |
| **ADR-001** | 31/10/2026 | Pemilihan Framework GUI & Runtime | Menggunakan Python 3.13 Desktop dengan CustomTkinter | `[APPROVED]` |
| **ADR-002** | 31/10/2026 | Lingkungan Eksekusi & Privasi | Beroperasi 100% Offline (Tanpa Jaringan / API Eksternal) | `[APPROVED]` |
| **ADR-003** | 31/10/2026 | Integrasi AI Watermark Remover | Mengadopsi modul dari `guillaumemeyer/watermarks-remover` | `[APPROVED]` |
| **ADR-004** | 31/10/2026 | Packaging & Branding | Membangun Standalone `.exe` dengan Ikon Kustom `img.png` | `[SUPERSEDED]` |
| **ADR-005** | 31/10/2026 | Branding Baru & Dukungan File Coding | Menggunakan `Material/logo.jpg` & Menambahkan `TextCleaner` untuk Markdown dan Seluruh Bahasa Pemrograman | `[APPROVED]` |
| **ADR-006** | 31/10/2026 | Ekspor PDF/MD & Editor Metadata Selektif | Modal Radio Button Ekspor (PDF/Markdown) & Engine Edit Metadata Parsial Preservative | `[APPROVED]` |
| **ADR-007** | 09/11/2026 | Multi-Item Selection & Batch Cleaning Selektif | Checkbox baris antrean, Master Checkbox 'Pilih Semua', dan Dynamic Counter aksi | `[APPROVED]` |
| **ADR-008** | 09/11/2026 | Privacy Risk Scoring Engine (0-100%) | Penilaian skor ancaman privasi berkas berbasis sensitivitas data (GPS, Serial, Author) | `[APPROVED]` |
| **ADR-009** | 09/11/2026 | Quick Clean Presets (Profil Cepat) | Profil pembersihan sekali klik: Media Sosial, Akademik, dan Developer/OSS | `[APPROVED]` |
| **ADR-010** | 09/11/2026 | AI Generative Forensics & C2PA Cleaner | Detektor prompt Midjourney/SD/DALL-E dan pembersih manifes C2PA Adobe | `[APPROVED]` |
| **ADR-011** | 09/11/2026 | Metadata Spoofing & Anonymizer | Injeksi profil kamera sintetis realistis (Canon, Nikon, Sony) untuk kamuflase | `[APPROVED]` |
| **ADR-012** | 09/11/2026 | Integrasi Menu Klik Kanan Windows Explorer | Pendaftaran shortcut shell di level HKCU tanpa memerlukan hak Administrator | `[APPROVED]` |
| **ADR-013** | 09/11/2026 | Kebijakan Kebersihan Branch `main` | Branch main diisolasi khusus untuk kode produksi; catatan pengembang di-prune | `[APPROVED]` |

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
- **Keputusan:** Menggunakan `Material/logo.jpg` sebagai sumber utama ikon Windows `assets/icon.ico` dan menambahkan `TextCleaner` untuk format koding dan Markdown.

### ADR-006 — Dialog Ekspor Radio Button (PDF/Markdown) & Editor Metadata Preservative
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 31/10/2026
- **Penyetuju Resmi:** Yogi Ario (31/10/2026)
- **Keputusan:** Menyediakan `ExportFormatDialog` (PDF & Markdown) dan modul `src/editors/` untuk pengubahan metadata selektif.

### ADR-007 — Multi-Item Selection & Batch Cleaning Selektif
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 09/11/2026
- **Penyetuju Resmi:** Yogi Ario (09/11/2026)
- **Keputusan:** Menambahkan checkbox per baris dan Master Checkbox 'Pilih Semua' serta counter dinamis untuk pembersihan batch selektif.

### ADR-008 — Privacy Risk Scoring Engine (0-100%)
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 09/11/2026
- **Penyetuju Resmi:** Yogi Ario (09/11/2026)
- **Keputusan:** Mengembangkan `src/inspectors/risk_scorer.py` untuk mengukur tingkat kerentanan privasi berkas ke dalam tingkatan Kritis (≥70%), Sedang (30-69%), dan Aman (<30%) dengan representasi meter visual di GUI dan laporan ekspor.

### ADR-009 — Quick Clean Presets (Profil Cepat)
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 09/11/2026
- **Penyetuju Resmi:** Yogi Ario (09/11/2026)
- **Keputusan:** Mengembangkan `src/cleaners/preset_cleaner.py` dengan profil Media Sosial, Akademik, dan Developer/OSS untuk pembersihan instan berbasis skenario.

### ADR-010 — AI Generative Forensics & C2PA Cleaner
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 09/11/2026
- **Penyetuju Resmi:** Yogi Ario (09/11/2026)
- **Keputusan:** Mengembangkan `src/inspectors/ai_forensics.py` dan `src/cleaners/c2pa_cleaner.py` untuk mengekstrak prompt asli (Stable Diffusion, Midjourney, DALL-E) dan menghapus manifes C2PA Adobe.

### ADR-011 — Metadata Spoofing & Anonymizer
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 09/11/2026
- **Penyetuju Resmi:** Yogi Ario (09/11/2026)
- **Keputusan:** Mengembangkan `src/editors/spoofing.py` untuk menginjeksi metadata kamera sintetis acak dan wajar agar berkas tidak terdeteksi sebagai berkas yang metadatanya sengaja dihapus (*anti-stripper detection*).

### ADR-012 — Integrasi Menu Klik Kanan Windows Explorer
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 09/11/2026
- **Penyetuju Resmi:** Yogi Ario (09/11/2026)
- **Keputusan:** Mengembangkan `src/utils/shell_integration.py` untuk mendaftarkan pintasan klik kanan di `HKEY_CURRENT_USER` tanpa butuh akses Administrator.

### ADR-013 — Kebijakan Kebersihan Branch `main`
- **Status:** `[APPROVED]`
- **Tanggal Usulan:** 09/11/2026
- **Penyetuju Resmi:** Yogi Ario (09/11/2026)
- **Keputusan:** Mengisolasi branch `main` khusus untuk berkas produksi bersih melalui skrip otomatis `tools/sync_to_main.py` yang memangkas folder catatan pengembang (`Docs/`, `changelog/`, dll.).
