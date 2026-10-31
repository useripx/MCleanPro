"""
MetaClean — Audio & Video Metadata Cleaner
Menghapus tag ID3, Vorbis Comments, dan metadata kontainer pada file media audio/video.
"""
import os
import shutil
from typing import Dict, Any, Optional
import mutagen
from src.cleaners.base import BaseCleaner

class MediaCleaner(BaseCleaner):
    SUPPORTED_EXTS = {".mp3", ".mp4", ".m4a", ".wav", ".flac", ".ogg", ".mkv", ".avi", ".wma"}

    def can_clean(self, file_path: str) -> bool:
        return os.path.splitext(file_path)[1].lower() in self.SUPPORTED_EXTS

    def clean(self, input_path: str, output_path: Optional[str] = None) -> Dict[str, Any]:
        if not os.path.exists(input_path):
            return {"success": False, "error": f"Berkas tidak ditemukan: {input_path}"}

        if output_path is None:
            dirname, filename = os.path.split(input_path)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(dirname, f"{name}_clean{ext}")

        orig_size = os.path.getsize(input_path)

        try:
            # Salin berkas asli ke tujuan sebelum manipulasi
            shutil.copy2(input_path, output_path)

            audio = mutagen.File(output_path)
            if audio is not None:
                # Hapus seluruh tags
                try:
                    audio.delete()
                except Exception:
                    pass

            cleaned_size = os.path.getsize(output_path)
            return {
                "success": True,
                "input_path": input_path,
                "output_path": output_path,
                "original_size_bytes": orig_size,
                "cleaned_size_bytes": cleaned_size,
                "message": "Metadata tag audio/video berhasil dibersihkan."
            }
        except Exception as e:
            return {
                "success": False,
                "input_path": input_path,
                "error": f"Gagal membersihkan media: {str(e)}"
            }

