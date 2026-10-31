# API Contract — MetaClean

> **STATUS DOKUMEN:** APLIKASI DESKTOP STANDALONE OFFLINE  
> **PEMILIK PROYEK:** Yogi Ario  
> **CATATAN ARSITEKTUR:**  
> Aplikasi **MetaClean** adalah aplikasi desktop murni (*Single-Player Desktop Offline*) yang beroperasi 100% secara lokal pada sistem operasi pengguna. Aplikasi ini **TIDAK** membuka port jaringan, tidak mengonsumsi endpoint REST API eksternal, dan tidak mengirim data apa pun ke internet.

---

## 1. Antarmuka Data Internal (Internal Data Contract)

Meskipun tidak memiliki API web, pertukaran data antar modul (GUI, Inspector, Cleaner, Watermark Engine) menggunakan format objek dictionary / JSON standar berikut:

### 1.1 Struktur Hasil Ekstraksi Metadata (Metadata Inspection Result)

```json
{
  "file_path": "C:/Users/.../foto.jpg",
  "file_name": "foto.jpg",
  "file_size_bytes": 2048500,
  "file_type": "image/jpeg",
  "has_metadata": true,
  "has_ai_watermark": false,
  "categories": {
    "General": {
      "Format": "JPEG",
      "Dimensions": "4032 x 3024",
      "Color Mode": "RGB"
    },
    "EXIF": {
      "Camera Make": "Apple",
      "Camera Model": "iPhone 13",
      "Software": "iOS 17.5",
      "Date Taken": "2026:08:12 14:22:05"
    },
    "GPS": {
      "Latitude": "-0.9471° S",
      "Longitude": "100.3543° E",
      "Altitude": "12.4 m"
    }
  }
}
```

### 1.2 Struktur Hasil Pembersihan (Cleaning Result)

```json
{
  "success": true,
  "original_file": "foto.jpg",
  "output_file": "foto_clean.jpg",
  "tags_removed_count": 18,
  "original_size": 2048500,
  "cleaned_size": 2041200,
  "message": "Metadata berhasil dibersihkan tanpa penurunan kualitas konten."
}
```
