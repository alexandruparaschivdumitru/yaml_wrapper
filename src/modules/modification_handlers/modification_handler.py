from typing import Any
from src.modules.initialisers.initialiser import Initialiser

from src.modules.synchronisers.synchroniser import Synchroniser

class ModificationHandler:
    def __init__(self, file_path: str, synchroniser: Synchroniser, initialiser: Initialiser) -> None:
        self._file_path = file_path
        self._synchroniser = synchroniser
        self._initialiser = initialiser
    
    def load(self) -> list:
        """Read and return the contents of he file.

        Returns:
            list: Content of file.
        """
        pass
    