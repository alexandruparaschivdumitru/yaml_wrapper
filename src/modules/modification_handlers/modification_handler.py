from typing import Any, List, Union, cast
from src.modules.initialisers.initialiser import Initialiser
from src.modules.modification_handlers.exceptions.filter_not_found_exception import FilterNotFoundException
from src.modules.modification_handlers.exceptions.not_safe_load_exception import NotSafeLoadException
from src.modules.modification_handlers.exceptions.not_valid_filter_exception import NotValidFilterException
from src.modules.modification_handlers.exceptions.not_valid_update_exception import NotValidUpdateException
from src.modules.modification_handlers.utils.searchers.value_by_path_boolean_searcher import ValueByPathBooleanSearcher
from src.modules.modification_handlers.utils.searchers.value_by_path_reference_searcher import ValueByPathReferenceSearcher

from src.modules.synchronisers.synchroniser import Synchroniser
from src.modules.validators.yaml_object_path_validator import YamlObjectPathValidator
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList

class ModificationHandler:
    """`ModificationHandler` class handles all the possible modification that are allowed using the `YamlDictionary` and `YamlList` classes.
        IMPORTANT NOTES:
        - When an instance of this class is created the content of file is not automatically loaded. This is done only when the `load` method is called.
        - It's IMPORTANT to remember that this class has an internal state, so all the modifications automaticaly update the internal state of the object,
        and the file content.
        
        
    """
    def __init__(self, file_path: str, safe_load: bool = True) -> None:
        self._file_path = file_path
        self._object: list = []
        self._safe_load: bool = safe_load
        self._loaded: bool = False
        self._synchroniser: Synchroniser = Synchroniser(file_path)
        self._initialiser: Initialiser = Initialiser(file_path)
        self._path_validator: YamlObjectPathValidator = YamlObjectPathValidator()
        
    
    def load(self) -> list:
        """Reads the file and creates the object with the readed information, then returns a copy of the created object.

        Returns:
            list: Copy of created object with the content of file.
        """
        self._loaded = True
        self._object = self._initialiser.initialise()
        return self._object.copy()

    def get(self) -> list:
        """Returns a copy of the contents of the file.

        Returns:
            list: Copy of object with content of file.
        """
        self._check_safe_load()
        
        return self._object.copy() 
    
    def check(self, filter: str, value: Union[str, int]) -> bool:
        """Checks if a value exist, using a filter to determine the position of the value.

        Args:
            filter (str): Filter used to determine the position of the value.
            value (Union[str, int]): Value to be checked.

        Returns:
            bool: True if the value exist, False otherwise.
        """
        self._check_safe_load()
        if not self._path_validator.validate(filter):
            raise NotValidFilterException("The filter is not valid.")
        
        search_in_object: list = self._object.copy()
        filter_splitted: list = filter.split(".")
        return ValueByPathBooleanSearcher.search(filter_splitted, value, search_in_object)
        
    
    def update(self, filter: str, update_data: Union[int, str, YamlDictionary, YamlList, List[YamlDictionary], List[YamlList]]) -> Any:
        """Updates a value in the file, using a filter to determine the position of the value.

        Args:
            filter (str): Filter used to determine the position of the value.
            update_data (Union[int, str, YamlDictionary, YamlList, List[YamlDictionary], List[YamlList]]): Data to be updated.

        Returns:
            list: Copy of object with updated value.
        """
        self._check_safe_load()
        filter_splitted: list = filter.split(".")
        #ValueByPathReferenceSearcher.search(filter_splitted, self._object)
        try:
            object_to_modify: Union[YamlDictionary, YamlList, None] = ValueByPathReferenceSearcher.search(filter_splitted, self._object)
            if object_to_modify is None:
                raise FilterNotFoundException("Filter not found.")
        except Exception:
            raise NotValidFilterException("The filter is not valid.")
        
        self._check_if_update_is_valid(object_to_modify, update_data)

        if isinstance(object_to_modify, YamlDictionary):
            cast(YamlDictionary, object_to_modify).value = cast(Union[int, str, YamlDictionary, YamlList, List[YamlDictionary]], update_data)
        else: 
             cast(YamlList, object_to_modify).values = cast(Union[List[YamlDictionary], List[Any]],update_data)
        return self._object.copy()
    
    def remove(self, filter: str, value: str = "") -> list:
        """ Removes a value from the file, using a filter to determine the position of the value.

        Args:
            filter (str): Filter used to determine the position of the value.
            value (str, optional): If the item to remove is from a `YamlList`, the value is used to filter between equal values, otherwise if the item is a `YamlDictionary` the content of value is ignored. Defaults to "".

        Returns:
            list: Copy of object with the item removed.
        """
        self._check_safe_load()
        
        return self._object.copy()
    
    def _check_safe_load(self) -> None:
        if not self._loaded and self._safe_load:
            raise NotSafeLoadException("The file is not loaded, and the safe load is enabled.")
        
    def _check_if_update_is_valid(self, 
                                value_to_update: Union[YamlDictionary, YamlList], 
                                update: Union[int, 
                                              str, 
                                              YamlDictionary, 
                                              YamlList, 
                                              List[YamlDictionary], 
                                              List[YamlList], 
                                              List[Any]]) -> None:
        
        if isinstance(value_to_update, YamlDictionary):
            if not (isinstance(update, int) or
                    isinstance(update, str) or
                    isinstance(update, YamlDictionary) or
                    isinstance(update, YamlList) or
                    all(isinstance(item, YamlDictionary) for item in update)):
                raise NotValidUpdateException("The update is not valid.")
        else:
            if not (isinstance(update, List)):
                raise NotValidUpdateException("The update is not valid.")
                   