from typing import Any, Union
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList


class YamlWrapper:
    def __init__(self, file_name: str) -> None:
        pass
    
    def create_dictionary(self, key: str, value: Union[str, YamlDictionary]) -> YamlDictionary:
        """Creates a new dictionary. If the key passed is already used is raise an Error.

        Args:
            key (str): Key of the new dictionary
            value (Any): Dictionary value

        Returns:
            Any: Created dictionary.
        """
        pass
    
    def remove_dictionary(self, key: str) -> YamlDictionary:
        pass
    
    def get_value(self) -> Union[YamlDictionary, YamlList]:
        pass
    
    def modify_dictionary(self, key: str,  filter: Any, new_value: Union[str, YamlDictionary, YamlList]) -> YamlDictionary:
        pass

    def create_new_list(self, key: str, value: Union[YamlDictionary, YamlList]) -> YamlList:
        pass
    
    def add_to_list(self, value:  Union[YamlDictionary, YamlList]) -> YamlList:
        pass
    
    def remove_from_list(self, key: str, filter: Any) -> YamlList:
        pass
    
    def is_empty(self, key: str) -> bool:
        pass
    
    def remove_list(self, key: str) -> YamlList:
        pass