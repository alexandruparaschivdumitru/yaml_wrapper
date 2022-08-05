from typing import Any, List, Union, cast
from src.modules.modification_handlers.modification_handler import ModificationHandler
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList


class YamlWrapper:
    """Creates a wrap over the yaml file. The `safe_initialization` setted True, will be used if the yaml file if not exist will be created according to the file path,
    otherwise il will be raised the exception `FileNotFoundError`.
    
    
    Data types:
    - YamlDictionary: Dictionary with the format accepted by the Yaml Wrap library.
    - YamlList: List with the format accepted by the Yaml Wrap library.
    
    IMPORTANT NOTES:
    The main purpose of this class is to create an abstraction layer over the PyYaml library. It's important to remember that the format of file contenten used in PyYaml library is
    not compatible.
    For example if in PyYaml library a dictionary is rappresented ad `{"key", "value"}`, in YamlWrapper is rappresented by YamlDictionary("key", "value").
    
    """
    def __init__(self, file_path: str, safe_initialization: bool = True) -> None:
        self._file_name: str = file_path
        self._safe_initialization: bool = safe_initialization
        self._modification_handler: ModificationHandler = ModificationHandler(file_path, safe_initialization)
        
        self._modification_handler.load()
    
    def get_file_name(self) -> str:
        """Returns the name of the file.

        Returns:
            str: File name.
        """
        return self._file_name
    
    def get_file_content(self) -> list:
        """Returns the content of the file in a list that contains it in the format accepted by the Yaml Wrap library.

        Returns:
            list: Content of the file.
        """
        return self._modification_handler.get()
    
    def update(self, filter: str, value: Union[int, str, List[YamlDictionary], YamlList]) -> list:
        """Updates the value of the file, using a filter to determine the position of the value. After the update the file is synchronised automatically.

        Args:
            filter (str): Filter used to determine the position of the value.
            value (Union[int, str, List[YamlDictionary], YamlList]): Value to be updated.

        Returns:
            list: Content of the file updates.
        
        Filter format:
        - File content: [YamlDictionary("key",[YamlDictionary("sub_key", "value")]) -> filter: "key.sub_key"
        - File content: [YamlDictionary("key",YamlList([1, 2, 3])) -> filter: "key.[]"
        - File content: [YamlDictionary("key",YamlList([[YamlDictionary("sub_key_1", "value_1"), YamlDictionary("sub_key_2", "value_2")]])] -> filter: "key.[].sub_key_1"
        
        Note:
        The filter it must be in the following format:
        Supposte che file content is a dictionary with another dictionary as value, so the situation is [YamlDictionary("key", [YamlDictionary("sub_key", "value")])].])], 
        in order to change the value the filter must be in the following format: "key.sub_key".
        
        """
        return self._modification_handler.update(filter, value)
    
    def remove(self, filter: str) -> list:
        """Remove a value from the file, using a filter to determine the position. After the remove the file is synchronised automatically.

        Args:
            filter (str): Filter used to determine the position of the value.

        Returns:
            list: Content of the file updates, after the remove.
        Filter format:
        - File content: [YamlDictionary("key",YamlDictionary("sub_key", "value")) -> filter: "key.sub_key"
        For the remotion the filter must not contain `[]`. This because the list is completely removed, using the value of its key.
    
        Example:
        - List remotion:
            - File content: [YamlDictionary("key",YamlList([1, 2, 3]))
                - Filter: "key"
                - After remove: []
            - File content: [YamlDictionary("key",[YamlDictionary("sub_key_1", "value_1"), YamlDictionary("sub_key_2", "value_2") ]] 
                - Filter: "key.sub_key_1"
                - After remove: [YamlDictionary("key",[YamlDictionary("sub_key_2", "value_2")])] 
        """
        return self._modification_handler.remove(filter)   
    
    def clean_file(self) -> bool:
        """Delete all data in the file. ATTENTION: this operation is not reversible.

        Returns:
            bool: True if the file is cleaned, False otherwise.
        """
        pass