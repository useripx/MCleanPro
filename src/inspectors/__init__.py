"""
MetaClean — Inspector Dispatcher
Menentukan dan menjalankan inspektor yang tepat untuk setiap berkas.
"""
from typing import Dict, Any, List
from src.inspectors.image_inspector import ImageInspector
from src.inspectors.pdf_inspector import PdfInspector
from src.inspectors.docx_inspector import DocxInspector
from src.inspectors.media_inspector import MediaInspector
from src.inspectors.text_inspector import TextInspector

ALL_INSPECTORS = [
    ImageInspector(),
    PdfInspector(),
    DocxInspector(),
    MediaInspector(),
    TextInspector()
]

def inspect_file(file_path: str) -> Dict[str, Any]:
    """Mendeteksi jenis file dan menjalankan inspektor yang sesuai."""
    for inspector in ALL_INSPECTORS:
        if inspector.can_inspect(file_path):
            return inspector.inspect(file_path)

    # Fallback untuk file yang belum didukung spesifik
    return {
        "file_path": file_path,
        "file_name": file_path.split("/")[-1].split("\\")[-1],
        "category": "unknown",
        "has_metadata": False,
        "metadata_count": 0,
        "categories": {
            "Info": {"Status": "Format berkas belum didukung untuk inspeksi mendalam."}
        },
        "has_ai_watermark": False,
        "watermarks_detected": []
    }

