"""
MetaClean — Icon & Logo Converter Utility
Mengonversi Material/logo.jpg (atau Material/img.png) menjadi format Windows .ico multi-resolusi
serta membuat assets/logo.png untuk ditampilkan di antarmuka GUI.
"""
import os
from PIL import Image

def convert_logo_to_assets(
    primary_input: str = "Material/logo.jpg",
    fallback_input: str = "Material/img.png",
    ico_output: str = "assets/icon.ico",
    png_output: str = "assets/logo.png"
) -> dict:
    """Mengonversi aset logo menjadi icon.ico dan logo.png."""
    input_path = primary_input if os.path.exists(primary_input) else fallback_input
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Berkas logo mentah tidak ditemukan: {primary_input} maupun {fallback_input}")

    os.makedirs(os.path.dirname(os.path.abspath(ico_output)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(png_output)), exist_ok=True)

    with Image.open(input_path) as img:
        # Konversi ke RGBA
        rgba_img = img.convert("RGBA")

        # 1. Simpan logo.png untuk GUI
        logo_png = rgba_img.resize((256, 256), Image.Resampling.LANCZOS)
        logo_png.save(png_output, format="PNG")

        # 2. Simpan icon.ico multi-ukuran untuk Windows & .exe
        icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        rgba_img.save(ico_output, format="ICO", sizes=icon_sizes)

    return {
        "source": input_path,
        "ico_path": ico_output,
        "png_path": png_output
    }

# Kompatibilitas mundur
def convert_png_to_ico(input_path: str = "Material/logo.jpg", output_path: str = "assets/icon.ico") -> str:
    res = convert_logo_to_assets(primary_input=input_path, ico_output=output_path)
    return res["ico_path"]

if __name__ == "__main__":
    res = convert_logo_to_assets()
    print(f"Ikon & Logo berhasil dibuat:")
    print(f" - Sumber : {res['source']}")
    print(f" - ICO    : {res['ico_path']}")
    print(f" - PNG    : {res['png_path']}")
