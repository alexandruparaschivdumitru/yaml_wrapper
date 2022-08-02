from typing import Any, List, Union
from src.modules.initialisers.initialiser import Initialiser

from src.modules.synchronisers.synchroniser import Synchroniser
from src.modules.validators.yaml_object_path_validator import YamlObjectPathValidator
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList

class ModificationHandler:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._object: list = []
        self._synchroniser: Synchroniser = Synchroniser(file_path)
        self._initialiser: Initialiser = Initialiser(file_path)
        self._path_validator: YamlObjectPathValidator = YamlObjectPathValidator()
        
    
    def load(self) -> list:
        """Read and return the contents of he file.

        Returns:
            list: Content of file.
        """
        pass

    def get(self) -> list:
        pass
    
    def check(self, fiter: str, value: Union[str, int]) -> bool:
        pass
    
    def update(self, filter: str, update_data: Union[int, str, YamlDictionary, YamlList, List[YamlDictionary], List[YamlList]]) -> list:
        pass
    
    def remove(self, filter: str, value: str = "") -> list:
        pass