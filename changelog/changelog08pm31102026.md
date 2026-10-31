# Changelog — 08pm31102026

**Tanggal:** 31 Oktober 2026 (20:55 WIB)  
**Tipe Perubahan:** Initial Setup / Tata Kelola & Perencanaan  
**Penyusun:** AI Agent (Pair Programmer)  
**Otoritas:** Yogi Ario  

---

### 🚀 Perubahan & Penambahan Baru
1. **Inisialisasi Tata Kelola Proyek:**
   - Dibuat berkas proteksi rahasia `.gitignore` dan `.env.example`.
   - Disiapkan folder `Material/` untuk aset mentah/branding `img.png` (status: READ-ONLY).
   - Diaktifkan berkas pengarah aturan `AGENTS.md` dan `GEMINI.md` di root proyek.
2. **Dokumentasi Proyek (`Docs/`):**
   - Mengadopsi kerangka kerja `Docs/universal-rule.md` yang disesuaikan untuk proyek desktop offline MetaClean.
   - Menginisialisasi `Docs/Task_Status.md` dan `Docs/Decision_Log.md`.
   - Mengisi `Docs/API_Contract.md` dengan status aplikasi desktop offline.
   - Menyusun `Docs/Implementation_plan.md` mencakup:
     - Modul Cek Metadata multi-format (Gambar, Dokumen, Audio/Video, Teks).
     - Modul Pembersihan Metadata (*Lossless Metadata Stripper*).
     - Modul Integrasi AI Watermark & Provenance Remover (berdasarkan `guillaumemeyer/watermarks-remover`).
     - GUI berbasis CustomTkinter dengan dukungan *drag-and-drop*.
     - Pengemasan aplikasi menjadi berkas `.exe` mandiri menggunakan PyInstaller dan ikon kustom `img.png`.
     - Test suite verifikasi 100% PASS.

---

### 📌 Status Approval Gate
- Menunggu tinjauan dan persetujuan eksplisit Mas Yogi Ario terhadap `Docs/Implementation_plan.md` sebelum penulisan kode aplikasi dimulai.
