"""
MetaClean — Base Cleaner Class
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class BaseCleaner(ABC):
    """Interface dasar untuk seluruh modul pembersih metadata."""

    @abstractmethod
    def can_clean(self, file_path: str) -> bool:
        """Menentukan apakah cleaner ini dapat menangani format berkas."""
        pass

    @abstractmethod
    def clean(self, input_path: str, output_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Membersihkan metadata dari berkas input dan menyimpannya ke output_path.
        Jika output_path None, membuat nama default: <nama>_clean.<ext>.
        Mengembalikan statistik pembersihan.
        """
        pass

