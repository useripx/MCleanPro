"""
MetaClean — Modern Desktop GUI
Antarmuka pengguna grafis berbasis CustomTkinter dengan dukungan Dark/Light mode,
pemindaian berkas tunggal & batch satu folder, inspeksi detail, dan pembersihan instan.
"""
import os
import sys
import threading
from tkinter import filedialog, messagebox
import customtkinter as ctk

from src.utils.scanner import scan_files
from src.inspectors import inspect_file
from src.cleaners import clean_file
from src.watermarks import AIWatermarkCleaner
from src.utils.exporter import export_to_json, export_to_text

# Pengaturan Default Tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MetaCleanApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MetaClean — Offline Metadata & AI Watermarks Tool")
        self.geometry("1120x720")
        self.minsize(920, 620)

        # Ikon Aplikasi (dari assets/icon.ico yang dikonversi dari Material/img.png)
        icon_path = os.path.abspath("assets/icon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

        # Data State
        self.scanned_items = []  # List of inspection result dicts
        self.selected_item = None
        self.is_processing = False

        self._build_ui()

    def _build_ui(self):
        # 1. Header Frame
        self.header_frame = ctk.CTkFrame(self, corner_radius=10, height=75)
        self.header_frame.pack(fill="x", padx=15, pady=(15, 10))

        # Title & Subtitle
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="🛡️ MetaClean",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.title_label.pack(side="left", padx=(20, 10), pady=12)

        self.subtitle_label = ctk.CTkLabel(
            self.header_frame,
            text="Pemeriksa & Pembersih Metadata Offline + AI Watermark Remover | Dikembangkan untuk Yogi Ario",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.subtitle_label.pack(side="left", padx=5, pady=12)

        # Appearance Mode Toggle
        self.theme_switch = ctk.CTkSwitch(
            self.header_frame,
            text="Mode Gelap",
            command=self._toggle_theme
        )
        self.theme_switch.select()
        self.theme_switch.pack(side="right", padx=20, pady=12)

        # 2. Control & Action Bar (Pilih Berkas / Folder)
        self.control_frame = ctk.CTkFrame(self, corner_radius=8)
        self.control_frame.pack(fill="x", padx=15, pady=5)

        self.btn_add_files = ctk.CTkButton(
            self.control_frame,
            text="📄 Tambah Berkas...",
            width=140,
            command=self._on_choose_files
        )
        self.btn_add_files.pack(side="left", padx=(15, 5), pady=10)

        self.btn_add_folder = ctk.CTkButton(
            self.control_frame,
            text="📁 Pindai 1 Folder...",
            width=150,
            fg_color="#2b7a78",
            hover_color="#205e5c",
            command=self._on_choose_folder
        )
        self.btn_add_folder.pack(side="left", padx=5, pady=10)

        self.chk_recursive = ctk.CTkCheckBox(
            self.control_frame,
            text="Pindai Subfolder"
        )
        self.chk_recursive.select()
        self.chk_recursive.pack(side="left", padx=15, pady=10)

        self.btn_clear = ctk.CTkButton(
            self.control_frame,
            text="🗑️ Kosongkan Daftar",
            width=130,
            fg_color="#802b2b",
            hover_color="#5a1e1e",
            command=self._clear_list
        )
        self.btn_clear.pack(side="right", padx=15, pady=10)

        # 3. Main Workspace (Panels: File List on Left, Detail Viewer on Right)
        self.main_paned = ctk.CTkFrame(self, corner_radius=8)
        self.main_paned.pack(fill="both", expand=True, padx=15, pady=5)

        # 3A. Left Panel: File List
        self.left_panel = ctk.CTkFrame(self.main_paned, width=440)
        self.left_panel.pack(side="left", fill="both", expand=False, padx=(5, 5), pady=5)

        self.left_header = ctk.CTkLabel(
            self.left_panel,
            text="Daftar Berkas Terpindai",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.left_header.pack(anchor="w", padx=15, pady=(10, 5))

        self.file_scroll = ctk.CTkScrollableFrame(self.left_panel, width=420)
        self.file_scroll.pack(fill="both", expand=True, padx=10, pady=(5, 10))

        # 3B. Right Panel: Metadata & Watermark Details
        self.right_panel = ctk.CTkFrame(self.main_paned)
        self.right_panel.pack(side="right", fill="both", expand=True, padx=(5, 5), pady=5)

        self.right_header = ctk.CTkLabel(
            self.right_panel,
            text="Detail Hasil Inspeksi Metadata",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.right_header.pack(anchor="w", padx=15, pady=(10, 5))

        self.detail_scroll = ctk.CTkScrollableFrame(self.right_panel)
        self.detail_scroll.pack(fill="both", expand=True, padx=10, pady=(5, 10))

        self._show_empty_detail_message()

        # 4. Bottom Action Bar (Cleaning & Export Actions)
        self.bottom_bar = ctk.CTkFrame(self, corner_radius=8, height=60)
        self.bottom_bar.pack(fill="x", padx=15, pady=(5, 10))

        self.btn_clean_selected = ctk.CTkButton(
            self.bottom_bar,
            text="🛡️ Bersihkan Metadata Terpilih",
            font=ctk.CTkFont(weight="bold"),
            command=self._clean_selected_file
        )
        self.btn_clean_selected.pack(side="left", padx=(15, 8), pady=12)

        self.btn_clean_all = ctk.CTkButton(
            self.bottom_bar,
            text="⚡ Bersihkan Semua di Folder (Batch)",
            fg_color="#1d7874",
            hover_color="#155d5a",
            font=ctk.CTkFont(weight="bold"),
            command=self._clean_all_files
        )
        self.btn_clean_all.pack(side="left", padx=8, pady=12)

        self.btn_clean_ai = ctk.CTkButton(
            self.bottom_bar,
            text="🤖 Hapus Watermark AI",
            fg_color="#673ab7",
            hover_color="#512da8",
            font=ctk.CTkFont(weight="bold"),
            command=self._clean_ai_watermarks
        )
        self.btn_clean_ai.pack(side="left", padx=8, pady=12)

        self.btn_export = ctk.CTkButton(
            self.bottom_bar,
            text="💾 Ekspor Laporan...",
            fg_color="#37474f",
            hover_color="#263238",
            command=self._export_report
        )
        self.btn_export.pack(side="right", padx=15, pady=12)

        # 5. Status Bar
        self.status_bar = ctk.CTkLabel(
            self,
            text="Siap. Silakan tambahkan berkas atau pilih folder untuk memulai inspeksi.",
            font=ctk.CTkFont(size=11),
            text_color="gray",
            anchor="w"
        )
        self.status_bar.pack(fill="x", padx=20, pady=(0, 8))

    def _toggle_theme(self):
        if self.theme_switch.get():
            ctk.set_appearance_mode("Dark")
            self.theme_switch.configure(text="Mode Gelap")
        else:
            ctk.set_appearance_mode("Light")
            self.theme_switch.configure(text="Mode Terang")

    def _show_empty_detail_message(self):
        for widget in self.detail_scroll.winfo_children():
            widget.destroy()

        msg = ctk.CTkLabel(
            self.detail_scroll,
            text="Pilih salah satu berkas di daftar sebelah kiri\nuntuk melihat rincian metadata dan watermark secara mendalam.",
            font=ctk.CTkFont(size=13),
            text_color="gray",
            justify="center"
        )
        msg.pack(expand=True, pady=120)

    def _on_choose_files(self):
        filetypes = [
            ("Semua Berkas yang Didukung", "*.jpg;*.jpeg;*.png;*.webp;*.pdf;*.docx;*.mp3;*.mp4;*.txt;*.md"),
            ("Gambar (JPG, PNG, WEBP)", "*.jpg;*.jpeg;*.png;*.webp;*.tiff;*.bmp"),
            ("Dokumen (PDF, Word)", "*.pdf;*.docx"),
            ("Media (Audio & Video)", "*.mp3;*.mp4;*.wav;*.mkv;*.m4a"),
            ("Teks & Markdown", "*.txt;*.md;*.json;*.csv;*.py"),
            ("Seluruh Berkas (*.*)", "*.*")
        ]
        paths = filedialog.askopenfilenames(title="Pilih Berkas untuk Diperiksa", filetypes=filetypes)
        if paths:
            self._process_paths(list(paths))

    def _on_choose_folder(self):
        folder = filedialog.askdirectory(title="Pilih Folder untuk Batch Scan")
        if folder:
            self._process_paths([folder])

    def _process_paths(self, paths):
        if self.is_processing:
            messagebox.showwarning("Peringatan", "Proses pemindaian sedang berjalan, mohon tunggu.")
            return

        self.is_processing = True
        self.status_bar.configure(text="⏳ Sedang memindai berkas & memeriksa metadata...")

        def worker():
            recursive = bool(self.chk_recursive.get())
            discovered = scan_files(paths, recursive=recursive)

            new_results = []
            for item in discovered:
                info = inspect_file(item["path"])
                new_results.append(info)

            # Update UI on main thread
            self.after(0, lambda: self._on_scan_completed(new_results))

        threading.Thread(target=worker, daemon=True).start()

    def _on_scan_completed(self, new_results):
        self.is_processing = False
        self.scanned_items.extend(new_results)
        self._refresh_file_list()

        total = len(self.scanned_items)
        has_meta = sum(1 for x in self.scanned_items if x.get("has_metadata"))
        has_wm = sum(1 for x in self.scanned_items if x.get("has_ai_watermark"))

        self.status_bar.configure(
            text=f"Selesai memindai. Total: {total} berkas | {has_meta} berkas memiliki metadata | {has_wm} berkas terindikasi watermark AI"
        )

    def _refresh_file_list(self):
        for widget in self.file_scroll.winfo_children():
            widget.destroy()

        if not self.scanned_items:
            empty_lbl = ctk.CTkLabel(
                self.file_scroll,
                text="Belum ada berkas yang dimuat.",
                text_color="gray"
            )
            empty_lbl.pack(pady=40)
            self._show_empty_detail_message()
            return

        for idx, item in enumerate(self.scanned_items):
            item_frame = ctk.CTkFrame(self.file_scroll, corner_radius=6)
            item_frame.pack(fill="x", padx=5, pady=4)

            # Left indicators
            category = item.get("category", "file").upper()
            cat_badge = ctk.CTkLabel(
                item_frame,
                text=f"[{category}]",
                font=ctk.CTkFont(size=10, weight="bold"),
                text_color="#64b5f6"
            )
            cat_badge.pack(side="left", padx=(8, 4), pady=6)

            name = item.get("file_name", "Unknown")
            if len(name) > 28:
                display_name = name[:25] + "..."
            else:
                display_name = name

            btn_select = ctk.CTkButton(
                item_frame,
                text=display_name,
                fg_color="transparent",
                hover_color="#333333",
                anchor="w",
                font=ctk.CTkFont(size=12),
                command=lambda it=item: self._display_detail(it)
            )
            btn_select.pack(side="left", fill="x", expand=True, padx=4)

            # Badges
            if item.get("has_ai_watermark"):
                wm_badge = ctk.CTkLabel(
                    item_frame,
                    text="🤖 AI-WM",
                    font=ctk.CTkFont(size=10, weight="bold"),
                    text_color="#e040fb"
                )
                wm_badge.pack(side="right", padx=6)

            if item.get("has_metadata"):
                meta_badge = ctk.CTkLabel(
                    item_frame,
                    text="⚠️ Metadata",
                    font=ctk.CTkFont(size=10),
                    text_color="#ffb74d"
                )
                meta_badge.pack(side="right", padx=4)
            else:
                clean_badge = ctk.CTkLabel(
                    item_frame,
                    text="✅ Bersih",
                    font=ctk.CTkFont(size=10),
                    text_color="#81c784"
                )
                clean_badge.pack(side="right", padx=4)

    def _display_detail(self, item):
        self.selected_item = item

        for widget in self.detail_scroll.winfo_children():
            widget.destroy()

        # Header Info Card
        card = ctk.CTkFrame(self.detail_scroll, corner_radius=8)
        card.pack(fill="x", padx=5, pady=5)

        ctk.CTkLabel(
            card,
            text=f"📁 {item.get('file_name')}",
            font=ctk.CTkFont(size=15, weight="bold")
        ).pack(anchor="w", padx=12, pady=(10, 2))

        ctk.CTkLabel(
            card,
            text=f"Lokasi: {item.get('file_path')}",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        ).pack(anchor="w", padx=12, pady=2)

        size_kb = item.get("file_size", 0) / 1024
        ctk.CTkLabel(
            card,
            text=f"Ukuran: {size_kb:.1f} KB | Kategori: {item.get('category').upper()}",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        ).pack(anchor="w", padx=12, pady=(2, 10))

        # AI Watermark Alert Box if present
        if item.get("has_ai_watermark"):
            wm_box = ctk.CTkFrame(self.detail_scroll, corner_radius=8, fg_color="#3e1b4a")
            wm_box.pack(fill="x", padx=5, pady=5)

            ctk.CTkLabel(
                wm_box,
                text="⚠️ Tanda Air AI / Steganografi Terdeteksi!",
                font=ctk.CTkFont(size=13, weight="bold"),
                text_color="#ff80ab"
            ).pack(anchor="w", padx=12, pady=(8, 2))

            for wm in item.get("watermarks_detected", []):
                ctk.CTkLabel(
                    wm_box,
                    text=f"• {wm}",
                    font=ctk.CTkFont(size=11),
                    text_color="#f8bbd0"
                ).pack(anchor="w", padx=20, pady=1)

        # Categories & Tag Details
        categories = item.get("categories", {})
        if not categories:
            no_meta_lbl = ctk.CTkLabel(
                self.detail_scroll,
                text="✅ Tidak ditemukan metadata sensitif atau berkas sudah bersih murni.",
                font=ctk.CTkFont(size=12),
                text_color="#81c784"
            )
            no_meta_lbl.pack(pady=20)
            return

        for cat_name, cat_data in categories.items():
            cat_frame = ctk.CTkFrame(self.detail_scroll, corner_radius=8)
            cat_frame.pack(fill="x", padx=5, pady=5)

            ctk.CTkLabel(
                cat_frame,
                text=f"🔹 {cat_name}",
                font=ctk.CTkFont(size=13, weight="bold")
            ).pack(anchor="w", padx=12, pady=(8, 4))

            if isinstance(cat_data, dict):
                for k, v in cat_data.items():
                    row = ctk.CTkFrame(cat_frame, fg_color="transparent")
                    row.pack(fill="x", padx=15, pady=2)

                    ctk.CTkLabel(
                        row,
                        text=f"{k}:",
                        font=ctk.CTkFont(size=11, weight="bold"),
                        width=180,
                        anchor="w"
                    ).pack(side="left")

                    ctk.CTkLabel(
                        row,
                        text=str(v),
                        font=ctk.CTkFont(size=11),
                        anchor="w",
                        text_color="#b0bec5",
                        wraplength=400
                    ).pack(side="left", fill="x", expand=True)
            else:
                ctk.CTkLabel(
                    cat_frame,
                    text=str(cat_data),
                    font=ctk.CTkFont(size=11),
                    text_color="#b0bec5"
                ).pack(anchor="w", padx=15, pady=4)

    def _clear_list(self):
        self.scanned_items.clear()
        self.selected_item = None
        self._refresh_file_list()
        self.status_bar.configure(text="Daftar berkas telah dikosongkan.")

    def _clean_selected_file(self):
        if not self.selected_item:
            messagebox.showinfo("Petunjuk", "Silakan pilih berkas di daftar terlebih dahulu.")
            return

        path = self.selected_item.get("file_path")
        res = clean_file(path)

        if res.get("success"):
            out_file = os.path.basename(res.get("output_path"))
            messagebox.showinfo("Berhasil", f"Metadata berhasil dibersihkan!\nDisimpan sebagai:\n{out_file}")
            # Refresh inspection
            new_info = inspect_file(res.get("output_path"))
            self.scanned_items.append(new_info)
            self._refresh_file_list()
            self._display_detail(new_info)
        else:
            messagebox.showerror("Gagal", res.get("error", "Gagal membersihkan berkas."))

    def _clean_all_files(self):
        if not self.scanned_items:
            messagebox.showinfo("Petunjuk", "Tidak ada berkas di daftar untuk dibersihkan.")
            return

        confirm = messagebox.askyesno(
            "Konfirmasi Pembersihan Batch",
            f"Apakah Anda ingin membersihkan metadata dari {len(self.scanned_items)} berkas?\n\nBerkas bersih akan disimpan sebagai salinan baru (<nama>_clean.<ext>)."
        )
        if not confirm:
            return

        self.status_bar.configure(text="⚡ Sedang membersihkan seluruh berkas di folder...")

        def worker():
            success_count = 0
            new_items = []
            for item in self.scanned_items:
                path = item.get("file_path")
                res = clean_file(path)
                if res.get("success"):
                    success_count += 1
                    cleaned_info = inspect_file(res.get("output_path"))
                    new_items.append(cleaned_info)

            def on_finish():
                self.scanned_items.extend(new_items)
                self._refresh_file_list()
                self.status_bar.configure(text=f"Pembersihan batch selesai: {success_count} berkas berhasil dibersihkan.")
                messagebox.showinfo(
                    "Selesai",
                    f"Pembersihan Batch Berhasil!\n{success_count} dari {len(self.scanned_items)} berkas telah dibersihkan."
                )

            self.after(0, on_finish)

        threading.Thread(target=worker, daemon=True).start()

    def _clean_ai_watermarks(self):
        if not self.selected_item:
            messagebox.showinfo("Petunjuk", "Silakan pilih berkas teks/media di daftar untuk dibersihkan watermarknya.")
            return

        path = self.selected_item.get("file_path")
        res = AIWatermarkCleaner.clean_file(path)

        if res.get("success"):
            out_file = os.path.basename(res.get("output_path"))
            wm_count = res.get("watermarks_removed", "Semua")
            messagebox.showinfo(
                "Berhasil",
                f"Watermark AI ({wm_count} tanda air) berhasil dihapus!\nDisimpan sebagai:\n{out_file}"
            )
            new_info = inspect_file(res.get("output_path"))
            self.scanned_items.append(new_info)
            self._refresh_file_list()
            self._display_detail(new_info)
        else:
            messagebox.showerror("Gagal", res.get("error", "Gagal menghapus watermark."))

    def _export_report(self):
        if not self.scanned_items:
            messagebox.showinfo("Petunjuk", "Belum ada data metadata untuk diekspor.")
            return

        save_path = filedialog.asksaveasfilename(
            title="Simpan Laporan Metadata",
            defaultextension=".json",
            filetypes=[("Berkas JSON (*.json)", "*.json"), ("Laporan Teks (*.txt)", "*.txt")]
        )
        if not save_path:
            return

        ext = os.path.splitext(save_path)[1].lower()
        if ext == ".txt":
            ok = export_to_text(self.scanned_items, save_path)
        else:
            ok = export_to_json(self.scanned_items, save_path)

        if ok:
            messagebox.showinfo("Berhasil", f"Laporan metadata berhasil disimpan ke:\n{save_path}")
        else:
            messagebox.showerror("Gagal", "Gagal menyimpan berkas laporan.")

def main():
    app = MetaCleanApp()
    app.mainloop()

if __name__ == "__main__":
    main()

