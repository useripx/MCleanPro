# UNIVERSAL-RULE.md — Kerangka Standar Kerja Pengembangan Proyek & AI Agent

> **STATUS:** DOKUMEN STANDAR UNIVERSAL (MASTER FRAMEWORK)  
> **PROYEK:** MetaClean — Offline Metadata Inspector, Cleaner & AI Watermarks Remover  
> **OTORITAS TERTINGGI:** Yogi Ario (PROJECT OWNER / LEAD DEVELOPER)  
> **TARGET PENGGUNA:** Seluruh Pengembang (Human Developer) & AI Agent (Antigravity, Gemini, Claude, Cursor, dll.)  
> **REUSABILITAS:** Wajib diterapkan pada proyek yang dikelola oleh: Yogi Ario.  

---

## 📖 Pendahuluan & Filosofi Kerja

Dokumen ini adalah **pedoman tata kelola universal (Universal Governance Framework)** yang dirancang untuk menjaga kualitas, keamanan, transparansi, dan kerapian pengerjaan software engineering dari awal hingga rilis produksi.

### 🧭 Core Philosophy: Consistent Standards, Variable Intelligence

> **"AI may vary in intelligence. Project standards must remain consistent."**

Kualitas penalaran, kemampuan mempertahankan konteks, dan keandalan eksekusi setiap AI Agent dapat berbeda-beda. Karena itu, proses pengembangan tidak boleh bergantung pada asumsi bahwa AI Agent akan selalu memahami instruksi atau menghasilkan pekerjaan dengan kualitas yang sama. **Standar kerja, gerbang persetujuan, dokumentasi, dan bukti pengujian harus tetap konsisten**, siapa pun AI Agent atau pengembang yang mengerjakannya.

Prinsip operasional yang menjadi dasar kerangka ini:

- **No Plan, No Code.** Rencana tertulis harus tersedia sebelum perubahan dilakukan.
- **No Approval, No Code.** Perubahan yang memerlukan persetujuan tidak boleh dijalankan sebelum persetujuan eksplisit diberikan.
- **No Evidence, No Completion.** Pekerjaan tidak boleh dinyatakan selesai tanpa bukti verifikasi yang sesuai.
- **No Superfluous AI Boilerplate:** Jangan menambahkan elemen formalitas tambahan, blok komentar yang tidak perlu, atau *boilerplate* artifisial yang tidak ada pada panduan penugasan agar tetap natural, otentik, dan tidak tampak seperti hasil generasi instan AI.

Setiap AI Agent atau pengembang yang memulai sesi pada repositori ini **WAJIB membaca, memahami, dan mematuhi 8 Pilar Standar Kerja** berikut tanpa terkecuali.

---

## 🏛️ Delapan Pilar Standar Kerja Universal

```mermaid
graph TD
    P1["1. ZERO-CODE Approval Gate"] --> Flow["Alur Kerja Terstruktur"]
    P2["2. Git Branching Strategy"] --> Flow
    P3["3. Zero Secret Leakage"] --> Flow
    P4["4. Asset & Design Protection"] --> Flow
    P5["5. Documentation Protocol"] --> Flow
    P6["6. 100% Automated Testing Gate"] --> Flow
    P7["7. Lean & Resilient Architecture"] --> Flow
    P8["8. Proactive & Consultative Comms"] --> Flow
    Flow --> Success["Software Berkualitas Tinggi & Bebas Masalah"]
```

---

### 🛑 Pilar 1: ZERO-CODE Sebelum Persetujuan Rencana (Approval Gate)

**Prinsip Inti:** *No Plan, No Code. No Approval, No Code. No Evidence, No Completion.*

1. **Dilarang Keras Menyentuh Kode Terlebih Dahulu:**
   - Jangan pernah membuat, mengedit, atau menghapus file kode aplikasi sebelum menyusun rencana kerja tertulis dan memperoleh **persetujuan eksplisit** dari Yogi Ario.
2. **Format Wajib Implementation Plan:**
   Setiap kali ada instruksi, fitur baru, atau perbaikan bug, buatlah dokumen rencana (*Implementation Plan*) yang memuat:
   - **Tujuan & Ruang Lingkup:** Apa yang ingin dicapai.
   - **Analisis & Pilihan Solusi:** Tawarkan opsi jika ada trade-off teknis.
   - **Daftar File Target:** File mana yang akan dibuat, dimodifikasi, atau diuji.
   - **Alur Pengujian:** Bagaimana cara membuktikan bahwa fitur bekerja dan bebas regresi.
3. **Gerbang Persetujuan (Approval Gate):**
   - AI Agent wajib berhenti dan menunggu konfirmasi Yogi Ario (misal: pesan "Oke disetujui", "Lanjut", atau respon positif serupa) sebelum menyentuh kode.

---

### 🌿 Pilar 2: Protokol Branching Git & Kontrol Rilis

**Prinsip Inti:** *Branch `main` adalah Mahkota Produksi — Hanya Yogi Ario yang Boleh Me-Merge.*

```mermaid
gitGraph
    commit id: "Init"
    branch develop
    checkout develop
    commit id: "Setup Fondasi"
    branch feature/fitur-baru
    checkout feature/fitur-baru
    commit id: "Buat View & Logic"
    commit id: "Uji 100% PASS"
    checkout develop
    merge feature/fitur-baru id: "Merge Feature"
    checkout main
    merge develop id: "Manual Release" tag: "v1.0.0"
```

1. **Branch `main` (Produksi Tertutup):**
   - Berisi kode stabil rilis produksi.
   - **DILARANG KERAS** melakukan commit atau push langsung ke `main` oleh AI Agent atau developer.
   - Merge dari `develop` ke `main` dilakukan **secara manual oleh Yogi Ario**.
2. **Branch `develop` (Branch Integrasi Utama):**
   - Seluruh pembaruan, perbaikan, dan fitur baru yang telah lulus uji wajib digabungkan ke `develop` dan di-push ke `origin develop`.
3. **Branch Fitur (`feature/<nama-fitur>` / `fix/<nama-bug>`):**
   - Setiap pekerjaan mandiri wajib dibuatkan branch tersendiri yang bercabang dari `develop`.
   - Setelah pekerjaan selesai dan lulus uji 100%, branch fitur digabungkan (*merge*) kembali ke `develop`.

---

### 🔐 Pilar 3: Keamanan Kunci Rahasia & Tata Kelola `.env` (Zero Secret Leakage)

**Prinsip Inti:** *Kunci API dan Kredensial Pribadi adalah Aset Paling Sensitif.*

1. **Perlindungan `.gitignore` Sejak Menit Pertama:**
   - File konfigurasi rahasia (`.env`, `.env.local`), file kunci lokal (`Docs/api`, `secrets.json`, file service account), dan database lokal **wajib langsung dimasukkan ke `.gitignore`** sebelum commit perdana.
2. **Larangan Kebocoran Kunci:**
   - Jangan pernah menuliskan nilai kunci API atau token rahasia ke dalam prompt obrolan publik, commit message, atau file kode yang ditrack oleh Git.
3. **Template Konfigurasi Bersih (`.env.example`):**
   - Selalu sediakan dan perbarui file `.env.example` berisi nama variabel tanpa nilai rahasia (gunakan dummy placeholder seperti `your_api_key_here`).

---

### 🎨 Pilar 4: Proteksi Integritas Aset & Desain (`Material/` / Raw Assets)

**Prinsip Inti:** *Aset Asli Tim UI/UX adalah Bahan Rujukan Murni (Read-Only).*

1. **Status READ-ONLY untuk Folder Desain:**
   - Folder prototipe mentah (seperti `Material/`, `img.png`) yang disediakan Yogi Ario dilarang keras diubah, ditimpa, atau dihapus oleh AI Agent / Backend Developer.
2. **Pola Adopsi Bersih:**
   - Kode tampilan diadopsi/disalin secara terstruktur ke folder `assets/` produksi (misal icon `.ico` yang dikonversi dari `Material/img.png`), lalu dihubungkan dengan logic dinamis.

---

### 📝 Pilar 5: Protokol Dokumentasi Wajib (Documentation-First)

**Prinsip Inti:** *Kode Tanpa Dokumentasi adalah Utang Teknis di Masa Depan.*

Setiap repositori wajib memiliki folder `Docs/` dan folder `changelog/` yang selalu diperbarui:

| Nama Berkas                   | Lokasi                              | Fungsi & Aturan Pembaruan                                                                                            |
| ------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **`Task_Status.md`**          | `Docs/Task_Status.md`               | Melacak status seluruh fase proyek, persentase progres, dan checklist tugas real-time.                               |
| **`Decision_Log.md`**         | `Docs/Decision_Log.md`              | Mencatat seluruh keputusan teknis/arsitektur (ID, Tanggal, Topik, Keputusan, Rationale, Status Persetujuan).         |
| **`API_Contract.md`**         | `Docs/API_Contract.md`              | Kontrak spesifikasi endpoint REST API (Dicatat sebagai aplikasi desktop offline 100%).                              |
| **Changelog Bertimestamp**    | `changelog/changelog<jam><ampm><ddmmyyyy>.md` | Catatan perubahan bertimestamp waktu lokal per batch rilis atau tugas selesai. **Wajib flat** (disimpan langsung di dalam folder `changelog/`, dilarang membuat subfolder). Format: 2 digit jam (`03am` / `02pm`, huruf am/pm kecil) dan 8 digit tanggal (`ddmmyyyy`). Contoh: `changelog/changelog08pm31102026.md`. |
| **Panduan Khusus / Tutorial** | `Docs/<nama-modul>.md`              | Tutorial langkah-demi-langkah dari awal sampai akhir untuk setup pihak ketiga / konfigurasi modul khusus.            |
| **Cadangan Riwayat Chat**     | `Docs/chat/riwayat<ddmmyyyy>.md`    | Arsip komprehensif riwayat dialog interaktif antara pengguna dan AI Agent dari awal hingga akhir sesi.               |

---

### 🧪 Pilar 6: Gerbang Verifikasi Pengujian (100% Automated Testing Gate)

**Prinsip Inti:** *Jangan Pernah Bilang Selesai Jika Belum Terbukti Lulus Uji.*

1. **Wajib Memiliki Test Suite Otomatis:**
   - Setiap proyek wajib memiliki skrip verifikasi mandiri (unit test, integration test, atau end-to-end suite) di folder `tests/` menggunakan `unittest` atau `pytest`.
2. **Definisi Selesai (Definition of Done - DoD):**
   - Suatu tugas hanya boleh dilaporkan selesai jika test suite telah dijalankan di terminal/editor dan menghasilkan:
     **`HASIL: 100% PASS (0 GAGAL / 0 ERROR)`**.
3. **Pencegahan Regresi:**
   - Setiap penambahan fitur baru wajib disertai penambahan kasus uji pada test suite.

---

### ⚡ Pilar 7: Kedisiplinan Arsitektur & Provider (Lean & Resilient)

**Prinsip Inti:** *Sederhana, Cepat, Andal, dan Tanpa Ketergantungan Berlebihan.*

1. **Kunci Provider Tunggal / Efisien (Anti-Bloat):**
   - Menggunakan ekosistem Python standar dan pustaka teruji tanpa dependensi berlebih.
2. **Mekanisme Ketahanan (Fallback Multi-Tingkat):**
   - Parsing file dilengkapi penanganan error gracefully (jika ada file korup, enkripsi, atau format tak dikenal).
3. **Pemisahan Tanggung Jawab (Separation of Concerns):**
   - Pisahkan GUI (`src/gui/`), Logika Inspeksi (`src/inspectors/`), Pembersihan (`src/cleaners/`), dan Watermark (`src/watermarks/`).
4. **Hierarki Aturan Kode Sumber & Scoped AI Agent:**
   - Root `Docs/universal-rule.md` dan `AGENTS.md` menjadi otoritas makro tata kelola.

---

### 🤝 Pilar 8: Standar Komunikasi & Konsultasi AI Agent

**Prinsip Inti:** *AI Agent adalah Rekan Berpikir (Pair Programmer) yang Ramah, Jelas, dan Edukatif.*

1. **Proaktif Memberikan Solusi Berbasis Opsi:**
   - Menghadirkan opsi beserta trade-off teknis yang jelas.
2. **Bimbingan Setup Mandiri:**
   - Menyediakan instruksi instalasi dan packaging `.exe` yang terperinci.
3. **Gaya Bahasa:**
   - Ramah, profesional, ringkas, dan menggunakan tautan markdown yang dapat diklik (`[file.ext](file:///path/to/file)`).
4. **Kewajiban Menanyakan Pencadangan Riwayat Chat di Akhir Respon:**
   - **Wajib di Setiap Akhir Respon:** Bertanya proaktif di penutup:
     > *"Apakah Anda ingin saya mencadangkan riwayat percakapan sesi ini ke `Docs/chat/riwayat<ddmmyyyy>.md`?"*

---

## 📁 Struktur Standar Proyek MetaClean

```text
cek metadata/
├── .gitignore                     # Perlindungan awal (.env, build, dist, caches, venv)
├── .env.example                   # Template konfigurasi tanpa kunci rahasia
├── README.md                      # Dokumentasi pengenalan, arsitektur, dan panduan menjalankan
├── AGENTS.md                      # Indeks aturan kerja AI (merujuk ke Docs/universal-rule.md)
├── GEMINI.md                      # Indeks aturan kerja Gemini (merujuk ke Docs/universal-rule.md)
│
├── Material/                      # [READ-ONLY] Aset mentah dari Yogi Ario (img.png)
│   └── img.png
│
├── assets/                        # Aset produksi aplikasi (icon.ico, UI icons)
│   └── icon.ico                   # Konversi dari img.png untuk window & .exe
│
├── Docs/                          # Seluruh dokumentasi formal proyek
│   ├── chat/                      # Arsip berkala riwayat percakapan sesi AI
│   │   └── riwayat<ddmmyyyy>.md   # Berkas riwayat chat per tanggal
│   ├── universal-rule.md          # Dokumen aturan master ini
│   ├── Task_Status.md             # Pelacak progres fase dan checklist tugas
│   ├── Decision_Log.md            # Catatan riwayat keputusan arsitektur
│   ├── API_Contract.md            # Kontrak spesifikasi (Aplikasi Desktop Offline)
│   ├── Implementation_plan.md     # Rencana induk implementasi proyek
│   ├── Test_Report.md             # Laporan hasil verifikasi pengujian (100% PASS)
│   └── AGENTS-module-template.md  # Template aturan teknis untuk modul independen
│
├── changelog/                     # [FLAT] Catatan perubahan bertimestamp
│   └── changelog<jam><ampm><ddmmyyyy>.md
│
├── src/                           # Kode sumber aplikasi utama
│   ├── gui/                       # Antarmuka desktop CustomTkinter
│   ├── inspectors/                # Ekstraktor metadata (Gambar, Dokumen, Audio, Video)
│   ├── cleaners/                  # Pembersih metadata (Lossless metadata stripper)
│   ├── watermarks/                # Pembersih watermark AI & invisible steganography
│   └── utils/                     # Util penolong (konversi icon, ekspor JSON/CSV)
│
└── tests/                         # Suite pengujian otomatis (wajib 100% PASS)
```

---

## 📋 Checklist Kepatuhan AI Agent (Pre-Flight Checklist)

Sebelum AI Agent melaporkan suatu tugas selesai kepada Yogi Ario, lakukan verifikasi mandiri:

- [ ] Apakah rencana implementasi telah disetujui Yogi Ario sebelum kode disentuh? (**Pilar 1**)
- [ ] Apakah branch kerja saat ini adalah `develop` atau `feature/*`, bukan commit langsung ke `main`? (**Pilar 2**)
- [ ] Apakah seluruh perubahan telah di-push/digabungkan ke `develop`? (**Pilar 2**)
- [ ] Apakah file sensitif dan build output terlindungi oleh `.gitignore`? (**Pilar 3**)
- [ ] Apakah folder aset mentah (`Material/`) tetap utuh tanpa modifikasi? (**Pilar 4**)
- [ ] Apakah `Docs/Task_Status.md` dan `Docs/Decision_Log.md` telah diperbarui? (**Pilar 5**)
- [ ] Apakah changelog bertimestamp (`changelog/changelog<jam><ampm><ddmmyyyy>.md`) sudah dibuat secara flat tanpa subfolder? (**Pilar 5**)
- [ ] Apakah suite pengujian telah dijalankan dan terbukti **100% PASS**? (**Pilar 6**)
- [ ] Apakah di akhir respons telah menanyakan pencadangan riwayat chat ke `Docs/chat/riwayat<ddmmyyyy>.md`? (**Pilar 8**)

