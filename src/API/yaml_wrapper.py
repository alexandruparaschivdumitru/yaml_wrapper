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
            YamlDictionary: Created dictionary.
        """
        pass
    
    def remove_dictionary(self, key: str) -> YamlDictionary:
        """Remove a dictionary. 

        Args:
            key (str): Key of the dictionry to remove.

        Returns:
            YamlDictionary: Dictionary removed.
        """
        pass
    
    def get_value(self) -> Union[YamlDictionary, YamlList]:
        """Returns the value of a dictionary

        Returns:
            Union[YamlDictionary, YamlList]: Value returned.
        """
        pass
    
    def modify_dictionary(self, key: str,  filter: Any, new_value: Union[str, YamlDictionary, YamlList], new: bool = True) -> YamlDictionary:
        """Modify dictionary. The valaue to modify is determined using the filter.

        Args:
            key (str): Key of the dictionary
            filter (Any): Filter criteria
            new_value (Union[str, YamlDictionary, YamlList]): Update value
            new (bool): If True returns the modified dictinary, else returns the old.

        Returns:
            YamlDictionary: If new parameter is `True` it returns the modified dictionary, else returns the old one.
        """
        pass

    def create_new_list(self, value: Union[YamlDictionary, YamlList]) -> YamlList:
        """Creates a new list.

        Args:
            value (Union[YamlDictionary, YamlList]): List value.

        Returns:
            YamlList: Return the new list.
        """
        pass
    
    def add_to_list(self, value:  Union[YamlDictionary, YamlList]) -> YamlList:
        """Adds an intem to the list.

        Args:
            value (Union[YamlDictionary, YamlList]): Item to add.

        Returns:
            YamlList: Returns the updated list.
        """
        pass
    
    def remove_from_list(self, filter: Any) -> YamlList:
        """Removes ad item from the list.

        Args:
            filter (Any): Filter that determinates the item to remove.

        Returns:
            YamlList: Return the updated list.
        """
        pass
    
    def is_empty(self) -> bool:
        """Check if a list is empty.

        Args:
            key (str): _description_

        Returns:
            bool: Returns `True` if a list is empty, else returns `False`.
        """
        pass
    
    def remove_list(self) -> YamlList:
        """Removes all items from a list.

        Returns:
            YamlList: Return the list deleted.
        """
        pass