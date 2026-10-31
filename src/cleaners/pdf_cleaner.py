"""
MetaClean — PDF Document Metadata Cleaner
Menghapus author, creator, producer, tanggal modifikasi/pembuatan, dan data XMP pada dokumen PDF.
"""
import os
from typing import Dict, Any, Optional
from pypdf import PdfReader, PdfWriter
from src.cleaners.base import BaseCleaner

class PdfCleaner(BaseCleaner):
    def can_clean(self, file_path: str) -> bool:
        return os.path.splitext(file_path)[1].lower() == ".pdf"

    def clean(self, input_path: str, output_path: Optional[str] = None) -> Dict[str, Any]:
        if not os.path.exists(input_path):
            return {"success": False, "error": f"Berkas tidak ditemukan: {input_path}"}

        if output_path is None:
            dirname, filename = os.path.split(input_path)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(dirname, f"{name}_clean{ext}")

        orig_size = os.path.getsize(input_path)

        try:
            reader = PdfReader(input_path)
            writer = PdfWriter()

            # Salin seluruh halaman
            for page in reader.pages:
                writer.add_page(page)

            # Kosongkan metadata dokumen & hapus dictionary /Info
            writer._info = None

            # Tulis ke file tujuan
            with open(output_path, "wb") as f_out:
                writer.write(f_out)

            cleaned_size = os.path.getsize(output_path)
            return {
                "success": True,
                "input_path": input_path,
                "output_path": output_path,
                "original_size_bytes": orig_size,
                "cleaned_size_bytes": cleaned_size,
                "message": "Metadata PDF (Author, Producer, Tanggal) berhasil dikosongkan."
            }
        except Exception as e:
            return {
                "success": False,
                "input_path": input_path,
                "error": f"Gagal membersihkan PDF: {str(e)}"
            }
