"""
Unit Test: Metadata Cleaners
"""
import os
import shutil
import tempfile
import unittest
from PIL import Image
from pypdf import PdfWriter
from docx import Document
from src.cleaners import clean_file
from src.cleaners.image_cleaner import ImageCleaner
from src.cleaners.pdf_cleaner import PdfCleaner
from src.cleaners.docx_cleaner import DocxCleaner
from src.inspectors.image_inspector import ImageInspector
from src.inspectors.pdf_inspector import PdfInspector
from src.inspectors.docx_inspector import DocxInspector

class TestCleaners(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_image_cleaner(self):
        # Buat gambar dengan EXIF
        in_path = os.path.join(self.test_dir, "foto_exif.jpg")
        out_path = os.path.join(self.test_dir, "foto_clean.jpg")
        img = Image.new("RGB", (300, 200), color="green")
        exif = img.getexif()
        exif[0x010F] = "Canon"
        exif[0x0110] = "EOS R5"
        img.save(in_path, format="JPEG", exif=exif)

        cleaner = ImageCleaner()
        res = cleaner.clean(in_path, out_path)
        self.assertTrue(res["success"])
        self.assertTrue(os.path.exists(out_path))

        # Verifikasi hasil pembersihan dengan inspektor
        inspector = ImageInspector()
        inspect_res = inspector.inspect(out_path)
        # EXIF harus kosong
        self.assertNotIn("EXIF Kamera & Perangkat", inspect_res["categories"])
        # Dimensi gambar harus tetap utuh (300 x 200)
        self.assertIn("300 x 200 piksel", inspect_res["categories"]["Umum"]["Dimensi"])

    def test_pdf_cleaner(self):
        # Buat PDF dengan Author
        in_path = os.path.join(self.test_dir, "dokumen.pdf")
        out_path = os.path.join(self.test_dir, "dokumen_clean.pdf")
        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        writer.add_metadata({"/Author": "Secret Author", "/Producer": "Confidential"})
        with open(in_path, "wb") as f:
            writer.write(f)

        cleaner = PdfCleaner()
        res = cleaner.clean(in_path, out_path)
        self.assertTrue(res["success"])

        # Verifikasi hasil pembersihan
        inspector = PdfInspector()
        inspect_res = inspector.inspect(out_path)
        self.assertFalse(inspect_res["has_metadata"])

    def test_docx_cleaner(self):
        # Buat DOCX dengan Author
        in_path = os.path.join(self.test_dir, "surat.docx")
        out_path = os.path.join(self.test_dir, "surat_clean.docx")
        doc = Document()
        doc.add_paragraph("Isi surat rahasia.")
        doc.core_properties.author = "Yogi Ario"
        doc.save(in_path)

        cleaner = DocxCleaner()
        res = cleaner.clean(in_path, out_path)
        self.assertTrue(res["success"])

        # Verifikasi hasil pembersihan
        inspector = DocxInspector()
        inspect_res = inspector.inspect(out_path)
        self.assertFalse(inspect_res["has_metadata"])

    def test_dispatcher_clean(self):
        in_path = os.path.join(self.test_dir, "auto.jpg")
        img = Image.new("RGB", (100, 100), color="yellow")
        img.save(in_path, format="JPEG")

        res = clean_file(in_path)
        self.assertTrue(res["success"])
        self.assertTrue(os.path.exists(res["output_path"]))

if __name__ == "__main__":
    unittest.main()

