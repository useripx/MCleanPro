"""
MetaClean — AI Watermarks & Provenance Remover
Diadaptasi dan terinspirasi dari https://github.com/guillaumemeyer/watermarks-remover
Menghapus steganografi tak terlihat pada teks (Zero-Width Chars, Variation Selectors)
serta manifes provenance C2PA pada berkas digital.
"""
import os
import re
from typing import Dict, Any, Tuple, Optional
from src.inspectors.text_inspector import is_invisible_char, get_char_name

# Daftar regex pattern untuk karakter watermark tersembunyi
# Termasuk: U+200B..U+200F, U+202A..U+202E, U+2060..U+2064, U+FEFF, U+180E, U+FE00..U+FE0F
RE_INVISIBLE_CHARS = re.compile(
    r"[\u200B-\u200F\u202A-\u202E\u2060-\u2064\uFEFF\u180E\uFE00-\uFE0F\U000E0100-\U000E01EF\U000E0000-\U000E007F]"
)

class AIWatermarkCleaner:
    """Modul pembersih watermark tersembunyi AI dan manifes provenance."""

    @staticmethod
    def clean_text_watermarks(text: str) -> Tuple[str, Dict[str, Any]]:
        """
        Menghapus karakter steganografi tak kasat mata dari sebuah string teks.
        Mengembalikan teks bersih dan statistik karakter yang dihapus.
        """
        removed_breakdown = {}
        total_removed = 0

        # Catat rincian sebelum dibersihkan
        for char in text:
            cp = ord(char)
            if is_invisible_char(cp):
                name = get_char_name(cp)
                removed_breakdown[name] = removed_breakdown.get(name, 0) + 1
                total_removed += 1

        # Hapus menggunakan regex
        cleaned_text = RE_INVISIBLE_CHARS.sub("", text)

        stats = {
            "total_watermarks_removed": total_removed,
            "original_length": len(text),
            "cleaned_length": len(cleaned_text),
            "breakdown": removed_breakdown
        }
        return cleaned_text, stats

    @staticmethod
    def clean_file(input_path: str, output_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Membersihkan berkas dari watermark AI:
        - Jika teks: membersihkan invisible unicode steganography.
        - Jika gambar/dokumen/media: membersihkan EXIF, C2PA manifest, dan metadata identitas.
        """
        if not os.path.exists(input_path):
            return {"success": False, "error": f"Berkas tidak ditemukan: {input_path}"}

        ext = os.path.splitext(input_path)[1].lower()
        if output_path is None:
            dirname, filename = os.path.split(input_path)
            name, file_ext = os.path.splitext(filename)
            output_path = os.path.join(dirname, f"{name}_nowatermark{file_ext}")

        # 1. Penanganan Khusus Berkas Teks
        if ext in {".txt", ".md", ".json", ".csv", ".py", ".html", ".xml", ".log"}:
            try:
                with open(input_path, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()

                cleaned_content, stats = AIWatermarkCleaner.clean_text_watermarks(content)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(cleaned_content)

                return {
                    "success": True,
                    "input_path": input_path,
                    "output_path": output_path,
                    "type": "text",
                    "watermarks_removed": stats["total_watermarks_removed"],
                    "breakdown": stats["breakdown"],
                    "message": f"Berhasil menghapus {stats['total_watermarks_removed']} karakter watermark tak terlihat."
                }
            except Exception as e:
                return {"success": False, "error": f"Gagal memproses berkas teks: {str(e)}"}

        # 2. Penanganan Berkas Biner (Gambar, PDF, Media)
        # Menjalankan pembersihan metadata & C2PA manifest
        from src.cleaners import clean_file as base_clean_file
        clean_res = base_clean_file(input_path, output_path)
        if clean_res.get("success"):
            clean_res["message"] = "Manifes C2PA, EXIF, dan metadata provenance berhasil dibersihkan."
        return clean_res

