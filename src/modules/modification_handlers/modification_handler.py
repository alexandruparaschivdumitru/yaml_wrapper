from typing import Any
from src.modules.initialisers.initialiser import Initialiser

from src.modules.synchronisers.synchroniser import Synchroniser
from src.modules.validators.yaml_object_path_validator import YamlObjectPathValidator

class ModificationHandler:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._synchroniser: Synchroniser = Synchroniser(file_path)
        self._initialiser: Initialiser = Initialiser(file_path)
        self._path_validator: YamlObjectPathValidator = YamlObjectPathValidator()
        
    
    def load(self) -> list:
        """Read and return the contents of he file.

        Returns:
            list: Content of file.
        """
        pass
    