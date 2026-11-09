"""
MetaClean — Release Sync to Main Script
Menyinkronkan kode aplikasi terbaru dari branch 'develop' ke branch 'main'
dengan memastikan branch 'main' 100% BERSIH (hanya memuat berkas produksi,
tanpa folder catatan pengembang seperti Docs/, changelog/, dll.).
"""
import os
import sys
import subprocess

PRUNE_TARGETS = [
    "Docs",
    "changelog",
    ".gemini",
    "AGENTS.md",
    "GEMINI.md"
]

def run_git(args, check=True):
    res = subprocess.run(["git"] + args, capture_output=True, text=True, encoding="utf-8")
    if check and res.returncode != 0:
        print(f"[ERROR] Perintah 'git {' '.join(args)}' gagal: {res.stderr.strip()}")
        sys.exit(res.returncode)
    return res

def sync_to_main():
    print("=" * 60)
    print("[*] MEMULAI SINKRONISASI RILIS BERSIH KE BRANCH 'main'")
    print("=" * 60)

    # 1. Pastikan working tree bersih
    status_res = run_git(["status", "--porcelain"])
    if status_res.stdout.strip():
        print("[!] Peringatan: Terdapat perubahan yang belum di-commit. Silakan commit terlebih dahulu.")
        return False

    current_branch_res = run_git(["rev-parse", "--abbrev-ref", "HEAD"])
    source_branch = current_branch_res.stdout.strip()
    print(f"[*] Branch sumber saat ini: {source_branch}")

    # 2. Beralih ke branch main
    print("[*] Berpindah ke branch 'main'...")
    run_git(["checkout", "main"])

    # 3. Merge perubahan dari branch sumber
    print(f"[*] Menggabungkan kode dari {source_branch} ke main...")
    merge_res = run_git(["merge", source_branch, "--no-commit", "--no-ff"], check=False)
    if merge_res.returncode != 0:
        print(f"[!] Merge conflict terdeteksi. Silakan periksa manual.")
        return False

    # 4. Hapus berkas non-produksi (Docs, changelog, agent rules) dari main
    print("[*] Memangkas folder catatan pengembang dari branch main:")
    for target in PRUNE_TARGETS:
        if os.path.exists(target):
            print(f"    - Menghapus {target}/...")
            if os.path.isdir(target):
                subprocess.run(["git", "rm", "-rf", "--ignore-unmatch", target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                subprocess.run(["git", "rm", "-f", "--ignore-unmatch", target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 5. Commit perubahan bersih pada main
    print("[*] Membuat commit rilis produksi bersih di branch 'main'...")
    run_git(["commit", "-m", "release: clean production build (pruned dev docs and internal notes)"])

    print("\n" + "=" * 60)
    print("[SUCCESS] BRANCH 'main' BERHASIL DISINKRONKAN SECARA BERSIH!")
    print("Berkas di main sekarang hanya memuat runtime produksi:")
    subprocess.run(["git", "ls-tree", "--name-only", "HEAD"])
    print("=" * 60)

    # 6. Kembali ke branch pengembang semula
    print(f"[*] Kembali ke branch kerja: {source_branch}...")
    run_git(["checkout", source_branch])
    return True

if __name__ == "__main__":
    success = sync_to_main()
    sys.exit(0 if success else 1)
