# Changelog — 09 November 2026 (04:00 PM WIB)

> **PROYEK:** Mrclean (Offline Metadata & AI Watermarks Remover)  
> **VERSI RILIS:** Major Update v1  
> **BRANCH:** `fix/majorupdatev1`  
> **OTORITAS:** Yogi Ario  

---

## 🚀 Fitur Baru yang Ditambahkan (Major Update v1)

### 1. 🛡️ Privacy Risk Scoring Engine (0–100%) & Visual Badges
- Modul `src/inspectors/risk_scorer.py`: Menghitung skor kerentanan privasi berkas secara mendalam (GPS +40, Serial Number +30, Author +25, Path Lokal +25, AI Watermark +20, Model Kamera +15, Software +15, Tanggal +10).
- Klasifikasi status bahaya:
  - 🔴 **KRITIS (≥70%):** Berbahaya dibagikan ke publik.
  - 🟡 **SEDANG (30–69%):** Mengandung informasi perangkat atau software editor.
  - 🟢 **AMAN (<30%):** Bersih atau hanya spesifikasi teknis dasar.
- Visualisasi progress bar pada panel detail kanan dan badge warna pada antrean berkas panel kiri.
- Kolom baru `Skor Risiko Privasi` pada laporan ekspor PDF dan Markdown.

### 2. ⚡ Quick Clean Presets (Pembersihan Cepat Berbasis Profil)
- Modul `src/cleaners/preset_cleaner.py`:
  - 📱 **Media Sosial:** Menghapus GPS, Serial Number & Identitas Kamera, mengamankan orientasi dan profil sRGB.
  - 🎓 **Akademik:** Menghapus Author, Institusi, Catatan Revisi, dan Steganografi AI pada dokumen PDF/Word/Teks.
  - 💻 **Developer / OSS:** Menyamarkan path folder lokal komputer (`C:\Users\yogi\...`) dan membersihkan zero-width watermark dari source code.
- Opsi menu dropdown `[⚡ Profil Cepat...]` di panel aksi bawah GUI.

### 3. 🎨 Forensik AI Generatif & Pembersih C2PA
- Modul `src/inspectors/ai_forensics.py`: Mengekstrak teks prompt asli dan parameter generasi AI (Stable Diffusion, Midjourney, DALL-E, ComfyUI) serta manifes C2PA Adobe Content Credentials.
- Modul `src/cleaners/c2pa_cleaner.py`: Tombol khusus untuk menghapus seluruh jejak AI dan manifes C2PA tanpa merusak kualitas piksel gambar.
- Kartu UI khusus penampil prompt pada panel detail.

### 4. 🎭 Metadata Spoofing & Anonymizer (Generator Metadata Palsu)
- Modul `src/editors/spoofing.py`: Menginjeksi metadata sintetis kamera wajar (Canon EOS 5D Mark IV, Nikon D850, Sony A7R IV) dengan tanggal acak 30 hari terakhir untuk mencegah deteksi pembersihan metadata (*anti-stripper detection*).
- Tombol aksi `[🎭 Samarkan (Spoof)]` pada panel bawah GUI.

### 5. 🖱️ Integrasi Klik Kanan Windows Explorer (Shell Context Menu)
- Modul `src/utils/shell_integration.py`: Menambahkan pintasan *"🛡️ Bersihkan Metadata dengan Mrclean"* langsung di menu klik kanan file & folder Windows Explorer.
- Beroperasi 100% pada registri `HKEY_CURRENT_USER` sehingga aman dan **TIDAK memerlukan hak akses Administrator (UAC)**.
- Tombol toggle status integrasi pada header GUI.

### 6. 🧹 Kebijakan Kebersihan Branch `main` (Production-Only)
- Skrip otomatis `tools/sync_to_main.py`: Menjamin branch `main` 100% murni memuat kode aplikasi runtime (`src/`, `assets/`, `Material/`, `requirements.txt`, `README.md`, `LICENSE`, `build_exe.py`) dengan memangkas seluruh catatan internal pengembang (`Docs/`, `changelog/`, dll.).

---

## 🧪 Verifikasi Pengujian Otomatis (100% Automated Testing Gate)
- Menambahkan test suite baru:
  - `tests/test_risk_scorer.py`
  - `tests/test_presets.py`
  - `tests/test_ai_forensics.py`
  - `tests/test_spoofing.py`
  - `tests/test_shell_integration.py`
- Menjalankan seluruh test suite otomatis:
  ```bash
  python -m unittest discover -s tests -p "test_*.py" -v
  ```
- **Hasil:**
  **`40 Test Cases — 100% PASS (0 GAGAL / 0 ERROR)`**.
