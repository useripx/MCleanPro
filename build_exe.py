"""
MetaClean — Build & Packaging Script (.exe)
Mengemas aplikasi MetaClean menjadi satu berkas executable portabel tunggal (.exe)
dengan menyertakan ikon kustom Material/img.png (assets/icon.ico) dan aset tema CustomTkinter.
"""
import os
import sys
import subprocess
from src.utils.icon_converter import convert_png_to_ico

# Pastikan output konsol aman di Windows CP1252
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def build():
    print("=" * 60)
    print("[*] MEMULAI PROSES BUILD METACLEAN KE STANDALONE .EXE")
    print("=" * 60)

    # 1. Pastikan icon.ico terbuat dari Material/img.png
    ico_path = os.path.abspath("assets/icon.ico")
    png_path = os.path.abspath("Material/img.png")
    
    if os.path.exists(png_path):
        print(f"[*] Mengonversi aset mentah {png_path} ke {ico_path}...")
        convert_png_to_ico(png_path, ico_path)
    else:
        print("[!] Peringatan: Material/img.png tidak ditemukan, menggunakan ikon default.")

    # 2. Perintah PyInstaller
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconsole",
        "--onefile",
        "--name=MetaClean",
        f"--icon={ico_path}",
        "--collect-all=customtkinter",
        "--add-data=assets;assets",
        "--clean",
        "-y",
        "src/main.py"
    ]

    print("\n[*] Menjalankan PyInstaller dengan konfigurasi:")
    print(" ".join(cmd))
    print("\n[*] Proses kompilasi sedang berjalan, mohon tunggu beberapa saat...\n")

    result = subprocess.run(cmd)

    if result.returncode == 0:
        exe_path = os.path.abspath("dist/MetaClean.exe")
        if os.path.exists(exe_path):
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print("=" * 60)
            print("[SUCCESS] BUILD BERHASIL 100%!")
            print(f"Berkas Executable : {exe_path}")
            print(f"Ukuran Berkas     : {size_mb:.2f} MB")
            print("Ikon Aplikasi     : Berbasis Material/img.png")
            print("Status Operasional: 100% Offline Standalone")
            print("=" * 60)
            return True
        else:
            print("[!] Berkas exe tidak ditemukan di dist/")
            return False
    else:
        print(f"[X] Gagal melakukan build. Kode keluar: {result.returncode}")
        return False

if __name__ == "__main__":
    success = build()
    sys.exit(0 if success else 1)
