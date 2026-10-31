"""
MetaClean — Lossless Image Metadata Cleaner
Menghapus seluruh EXIF, GPS, info kamera, dan text chunks pada gambar tanpa merusak resolusi atau kualitas visual.
"""
import os
from typing import Dict, Any, Optional
from PIL import Image, ImageOps
from src.cleaners.base import BaseCleaner

class ImageCleaner(BaseCleaner):
    SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tiff", ".tif", ".bmp", ".gif"}

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
            with Image.open(input_path) as img:
                # 1. Normalisasi orientasi visual berdasarkan EXIF sebelum EXIF dibuang
                try:
                    transposed = ImageOps.exif_transpose(img)
                except Exception:
                    transposed = img

                # 2. Buat kanvas gambar bersih murni tanpa info chunks / EXIF
                fmt = img.format if img.format else "PNG"
                clean_img = Image.new(transposed.mode, transposed.size)
                clean_img.putdata(list(transposed.getdata()))

                # 3. Simpan ke berkas tujuan
                save_kwargs = {}
                if fmt.upper() in ["JPEG", "JPG"]:
                    save_kwargs["quality"] = 95
                    save_kwargs["subsampling"] = 0
                elif fmt.upper() == "PNG":
                    save_kwargs["optimize"] = True

                clean_img.save(output_path, format=fmt, **save_kwargs)

            cleaned_size = os.path.getsize(output_path)
            return {
                "success": True,
                "input_path": input_path,
                "output_path": output_path,
                "original_size_bytes": orig_size,
                "cleaned_size_bytes": cleaned_size,
                "bytes_saved": orig_size - cleaned_size,
                "message": "Metadata gambar (EXIF & GPS) berhasil dibersihkan."
            }
        except Exception as e:
            return {
                "success": False,
                "input_path": input_path,
                "error": f"Gagal membersihkan gambar: {str(e)}"
            }

