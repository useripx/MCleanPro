# MetaClean — Offline Metadata Inspector, Cleaner & AI Watermarks Remover

Aplikasi desktop Windows mandiri (100% offline) untuk memeriksa metadata, membersihkan metadata identitas, dan menghapus tanda air tak terlihat (*invisible AI steganography & provenance*) pada gambar, dokumen, teks, dan media audio/video.

---

## ✨ Fitur Utama

1. **Metadata Inspector (Pemeriksa Metadata):**
   - **Gambar (JPG, PNG, WEBP, TIFF):** Membaca EXIF, kamera, lensa, tanggal, software, dan lokasi GPS.
   - **Dokumen (PDF, DOCX, XLSX):** Membaca author, instansi pembuat, tanggal modifikasi, software pembuat.
   - **Audio & Video (MP3, MP4, WAV, MKV):** Membaca tag ID3, judul, artis, bitrate, encoder.
   - **Teks:** Mendeteksi karakter tak kasat mata (*zero-width characters*).

2. **Metadata Cleaner (Pembersih Metadata):**
   - Menghapus seluruh tag EXIF, GPS, riwayat penulis, dan identitas perangkat secara *lossless* tanpa mengurangi kualitas visual/suara berkas asli.
   - Mendukung pembersihan batch (satu folder sekaligus).

3. **AI Watermarks & Provenance Remover:**
   - Diintegrasikan dari algoritma [`guillaumemeyer/watermarks-remover`](https://github.com/guillaumemeyer/watermarks-remover).
   - Menghapus karakter Unicode tersembunyi (zero-width spaces, variation selectors, homoglyphs) pada teks AI.
   - Menghapus manifes C2PA (*Coalition for Content Provenance and Authenticity*) dari aset media.

4. **Desktop GUI Modern & Standalone `.exe`:**
   - Tampilan bersih berbasis *CustomTkinter* (mendukung Dark Mode).
   - Fitur *Drag and Drop* berkas/folder langsung ke jendela aplikasi.
   - Dikemas menjadi satu berkas `.exe` portabel menggunakan ikon kustom `Material/img.png`.

---

## 🏛️ Tata Kelola & Aturan Kerja
Proyek ini mengadopsi standar kerja ketat yang tercantum pada [`Docs/universal-rule.md`](Docs/universal-rule.md).
Seluruh AI Agent dan pengembang wajib membaca dan mematuhi panduan tersebut.

