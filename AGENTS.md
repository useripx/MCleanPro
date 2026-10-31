# AGENTS.md — Pedoman AI Agent untuk Proyek MetaClean

> **PERINGATAN WAJIB:**  
> Seluruh AI Agent (Antigravity, Gemini, Claude, Cursor, dll.) **WAJIB** membaca dan mematuhi seluruh aturan kerja yang tercantum di [`Docs/universal-rule.md`](Docs/universal-rule.md) sebelum melakukan tindakan apa pun pada repositori ini.

---

## 🏛️ Ringkasan Aturan Penting

1. **Approval Gate (Pilar 1):** Dilarang keras membuat atau mengedit kode aplikasi sebelum rencana implementasi tertulis ([Docs/Implementation_plan.md](Docs/Implementation_plan.md)) disetujui secara eksplisit oleh **Yogi Ario**.
2. **Branching (Pilar 2):** Branch `main` terkunci untuk produksi. Semua pekerjaan dilakukan di branch `develop` atau `feature/*`.
3. **Asset Protection (Pilar 4):** Folder [`Material/`](Material/) bersifat **READ-ONLY**. Berkas `img.png` adalah aset asli dan tidak boleh diubah/dihapus.
4. **Dokumentasi (Pilar 5):** Wajib memperbarui [`Docs/Task_Status.md`](Docs/Task_Status.md) dan [`Docs/Decision_Log.md`](Docs/Decision_Log.md), serta membuat catatan bertimestamp di [`changelog/`](changelog/).
5. **Testing Gate (Pilar 6):** Fitur hanya boleh dinyatakan selesai jika seluruh pengujian di [`tests/`](tests/) menghasilkan **100% PASS (0 GAGAL / 0 ERROR)**.
6. **Chat Backup (Pilar 8):** Di setiap akhir respon, tanyakan secara proaktif kepada Mas Yogi Ario apakah ingin mencadangkan riwayat percakapan ke `Docs/chat/riwayat<ddmmyyyy>.md`.
