"""
MetaClean — Icon Converter Utility
Mengonversi Material/img.png menjadi format Windows .ico multi-resolusi untuk aplikasi desktop & .exe
"""
import os
from PIL import Image

def convert_png_to_ico(input_path: str = "Material/img.png", output_path: str = "assets/icon.ico") -> str:
    """Mengonversi berkas PNG menjadi berkas ICO multi-ukuran."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Berkas gambar mentah tidak ditemukan: {input_path}")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with Image.open(input_path) as img:
        # Konversi ke RGBA untuk transparansi
        rgba_img = img.convert("RGBA")
        icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        rgba_img.save(output_path, format="ICO", sizes=icon_sizes)
        
    return output_path

if __name__ == "__main__":
    out = convert_png_to_ico()
    print(f"Icon berhasil dibuat di: {out}")

