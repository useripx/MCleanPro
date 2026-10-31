# AGENTS.md — [Isi Manual: Nama Modul / Folder Source]

> **STATUS:** ATURAN TEKNIS MODULAR (SCOPED AGENT RULES)  
> **LOKASI PENEMPATAN:** Letakkan berkas ini di dalam folder source/modul terkait (misal: `src/modules/<nama-modul>/AGENTS.md` atau `src/gui/AGENTS.md`).  
> **HIERARKI TATA KELOLA:** Berkas ini menginduk langsung ke [`Docs/universal-rule.md`](universal-rule.md) dan [`Root AGENTS.md`](../AGENTS.md). **Jika terjadi kontradiksi antara aturan modul ini dengan aturan root, aturan universal root dan persetujuan Yogi Ario selalu menjadi acuan tertinggi.**  
> **PRINSIP UTAMA:** *High Cohesion, Loose Coupling. No Plan, No Code. No Evidence, No Completion.*

---

## 1. Identitas & Ruang Lingkup Modul

- **Nama Modul / Sub-Aplikasi:** `[Isi Manual: misal: inspectors, cleaners, watermarks]`
- **Bahasa & Runtime:** Python 3.13
- **Tanggung Jawab Utama (Single Responsibility):**
  [Isi Manual: Jelaskan 1-2 kalimat fungsi spesifik modul ini bagi keseluruhan sistem.]
- **Batasan Ruang Lingkup:**
  - **In-Scope (Termasuk):** [Isi Manual: Fitur/logika yang menjadi hak modul ini]
  - **Out-of-Scope (Dilarang di Modul Ini):** [Isi Manual: Logika yang harus didelegasikan ke modul lain]

---

## 2. Enkapsulasi & Batasan Dependensi (Dependency Boundaries)

1. **Modul yang Diizinkan Diimpor:**
   - Modul standar Python atau modul internal yang didefinisikan secara resmi.
2. **Larangan Impor Liar:**
   - Dilarang keras mengimpor dependensi yang tidak relevan dengan tanggung jawab modul.
3. **Penyimpanan State:**
   - Modul ini mengelola state lokalnya sendiri tanpa mencemari global state aplikasi.

---

## 3. Pola Arsitektur Internal Folder

```text
[Nama Modul]/
├── __init__.py
├── base.py                        # Kelas dasar / interface
├── handlers.py                    # Implementasi handler per format
└── tests/                         # Pengujian unit khusus modul ini
```

---

## 4. Konvensi Penamaan & Standar Kode Lokal

- **Penamaan Berkas:** `snake_case.py`
- **Penamaan Interface / Class:** `PascalCase`
- **Penamaan Fungsi / Variabel:** `snake_case`

---

## 5. Pengujian Mandiri Lokal (Local Test Suite)

- **Perintah Uji Lokal:** `python -m unittest discover -s tests`
- **Target Kelulusan:** `100% PASS (0 GAGAL / 0 ERROR)`
