# Changelog — 09 November 2026 (03:00 PM WIB)

> **PROYEK:** Mrclean (Offline Metadata & AI Watermarks Remover)  
> **VERSI RILIS:** v2.1  
> **BRANCH:** `fix/select-item`  
> **OTORITAS:** Yogi Ario  

---

## 🚀 Fitur Baru yang Ditambahkan

### 1. ☑️ Multi-Item Selection & Batch Cleaning Selektif
- Menambahkan **Checkbox Individual** pada setiap baris item berkas dalam daftar antrean (`src/gui/app.py`).
- Menambahkan **Master Checkbox `[ ] Pilih Semua`** pada bagian atas panel daftar berkas, memungkinkan pengguna mencentang atau mengosongkan semua berkas sekaligus dengan satu klik.
- Menambahkan **Dynamic Selection Counter**:
  - Menampilkan jumlah berkas yang sedang dicentang `(X dari Y terpilih)`.
  - Tombol aksi utama otomatis berubah label sesuai jumlah berkas yang dipilih:
    - `🛡️ Bersihkan Berkas Terpilih (N)`
    - `🤖 Hapus Watermark AI Saja (N)`
- Integrasi fallback cerdas: Jika tidak ada berkas yang dicentang, tombol pembersihan tetap dapat beroperasi pada berkas yang sedang aktif/disorot (*highlighted*).
- Pembersihan batch selektif dijalankan di background thread dengan konfirmasi dialog dan indikator progres.

---

## 🧪 Verifikasi Pengujian (100% Automated Testing Gate)
- Menambahkan test suite baru `tests/test_multi_select.py` yang menguji:
  1. Pembersihan metadata *in-place* hanya pada subset berkas yang dipilih (File A & B dibersihkan, File C tidak tersentuh).
  2. Pembersihan watermark AI steganografi hanya pada berkas yang dipilih (File D dibersihkan, File E tidak tersentuh).
- Menjalankan seluruh test suite otomatis:
  ```bash
  python -m unittest discover -s tests -p "test_*.py" -v
  ```
- **Hasil:**
  **`29 Test Cases — 100% PASS (0 GAGAL / 0 ERROR)`**.

---

## 📦 Kompilasi & Pengemasan
- Skrip build `build_exe.py` siap dijalankan untuk menghasilkan build executable mandiri v2.1.
