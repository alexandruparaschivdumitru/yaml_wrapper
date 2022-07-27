from typing import Any


class YamlWrapper:
    def __init__(self, file_name: str) -> None:
        pass
    
    def create_dictionary(self, key: str, value: Any) -> Any:
        """Creates a new dictionary. If the key passed is already used is raise an Error.

        Args:
            key (str): Key of the new dictionary
            value (Any): Dictionary value

        Returns:
            Any: Created dictionary.
        """
        pass
    
    def remove_dictionary(self, key: str) -> Any:
        pass
    
    def modify_dictionary(self, key: str,  filter: Any, new_value: Any) -> Any:
        pass

    def create_new_list(self, key: str, value: Any) -> Any:
        pass
    
    def add_to_list(self, key: str, value: Any) -> Any:
        pass
    
    def remove_from_list(self, key: str, filter: Any) -> Any:
        pass
    
    def is_empty(self, key: str) -> Any:
        pass
    
    def remove_list(self, key: str) -> Any:
        pass