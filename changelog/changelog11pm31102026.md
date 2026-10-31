# Changelog — 31 Oktober 2026 (11:00 PM WIB)

> **PROYEK:** Mrclean (Offline Metadata & AI Watermarks Remover)  
> **VERSI RILIS:** v2.0  
> **BRANCH:** `develop`  
> **OTORITAS:** Yogi Ario  

---

## 🚀 Fitur Baru yang Ditambahkan

### 1. 💾 Dialog Pilihan Ekspor Laporan (Radio Button: PDF vs Markdown)
- Menambahkan modal dialog interaktif `ExportFormatDialog` (`src/gui/dialogs/export_dialog.py`) dengan opsi pilihan Radio Button:
  - `(•) Dokumen PDF (.pdf)`: Laporan cetak formal dengan kop/header resmi `Material/logo.jpg`, tabel ringkasan antrean berkas berpewarna modern, dan kartu rincian per berkas menggunakan `reportlab`.
  - `( ) Berkas Markdown (.md)`: Laporan tabel rapi GitHub-flavored Markdown lengkap dengan badge visual status (`✅ Bersih`, `⚠️ Metadata`, `🤖 AI-WM`) via `MarkdownExporter`.

### 2. ✏️ Editor Metadata Selektif / Granular (Preservative Metadata Editor)
- Tombol baru **"✏️ Edit Metadata"** pada panel aksi bawah aplikasi.
- Jendela modal form `MetadataEditDialog` (`src/gui/dialogs/edit_dialog.py`) yang terisi otomatis (*pre-filled*) dengan nilai metadata asli berkas.
- Memungkinkan pengguna mengubah atribut tertentu saja (misal mengganti **Author** menjadi `Yogi Ario`) dengan mempertahankan 100% atribut lain (kamera, ISO, tanggal, dimensi, copyright) tetap utuh.
- Modul backend editor:
  - `src/editors/image_editor.py`: Pengubah tag EXIF JPEG/PNG/TIFF via `piexif` & `Pillow`.
  - `src/editors/pdf_editor.py`: Pengubah metadata dokumen PDF via `pypdf`.
  - `src/editors/docx_editor.py`: Pengubah properti dokumen Word via `python-docx`.
  - `src/editors/media_editor.py`: Pengubah tag audio/video via `mutagen`.
  - `src/editors/__init__.py`: Dispatcher editor otomatis.

---

## 🧪 Verifikasi Pengujian (100% Automated Testing Gate)
- Menambahkan kasus uji unit test baru pada `tests/test_editors.py` dan `tests/test_exporters.py`.
- Seluruh suite pengujian otomatis (`python -m unittest discover -s tests -p "test_*.py" -v`) menghasilkan:
  **`HASIL: 27 Test Cases — 100% PASS (0 GAGAL / 0 ERROR)`**.

---

## 📦 Kompilasi & Pengemasan Executable
- Berhasil mengemas aplikasi menjadi berkas mandiri tunggal:
  - `dist/Mrclean.exe` (42.00 MB)
  - `Mrclean.exe` (salinan root direktori)
- Ikon kustom dan logo window berbasis `Material/logo.jpg`.
- Siap digunakan secara 100% offline tanpa dependensi eksternal.
