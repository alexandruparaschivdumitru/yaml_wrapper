from typing import List, Any
from typing import Union
from typing import cast
from src.modules.yaml_structures.exceptions.list_not_respect_integrity import ListNotRespectIntegriry

from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList

class ValueByPathReferenceSearcher:
    @staticmethod
    def search(filters: List[str], search_in_objects: list) -> Union[YamlDictionary, YamlList, None]:
        return ValueByPathReferenceSearcher._search_recursion(filters, search_in_objects, cast(Union[YamlDictionary, YamlList], {}))
    
    @staticmethod
    def _search_recursion(filters: List[str], search_in_objects: list, returned_value: Union[YamlDictionary, YamlList, None]) -> Union[YamlDictionary, YamlList, None]:
        if len(filters) == 0:
            return returned_value
        else:
            first_filter: str = filters.pop(0)
            first_search_in_objects: Union[YamlDictionary, YamlList] = search_in_objects[0]

            if first_filter != "[]":
                if isinstance(first_search_in_objects, YamlDictionary) and cast(YamlDictionary, first_search_in_objects).key == first_filter:
                    return  ValueByPathReferenceSearcher._search_recursion(filters,
                                                                           [cast(YamlDictionary, first_search_in_objects).value], 
                                                                           first_search_in_objects)
                elif isinstance(first_search_in_objects, list):
                    if not ValueByPathReferenceSearcher._check_list_integrity(first_search_in_objects, YamlDictionary):
                        raise ListNotRespectIntegriry("Items in list not respect integrity: they not have the same type.")
                    for item in first_search_in_objects: 
                        # TODO: Finish implementation 
                        value_to_return = ValueByPathReferenceSearcher._search_recursion(filters.copy(),
                                                                           [cast(YamlDictionary, first_search_in_objects).value], 
                                                                           first_search_in_objects)
                    
                    return ValueByPathReferenceSearcher._search_recursion(filters, 
                                                                          [cast(YamlDictionary, item).value],  
                                                                          first_search_in_objects)
                elif isinstance(first_search_in_objects, YamlList):
                    return  ValueByPathReferenceSearcher._search_recursion(filters,
                                                                           [cast(YamlDictionary, first_search_in_objects).value], 
                                                                           first_search_in_objects)
                else:
                    return ValueByPathReferenceSearcher._search_recursion([], [], None)
            else:
                if first_filter == "[]":
                    if not isinstance(first_search_in_objects, YamlList):
                        raise Exception
                return ValueByPathReferenceSearcher._search_recursion(filters,
                                                                           [cast(YamlList, first_search_in_objects).values], 
                                                                           first_search_in_objects)
    
    @staticmethod
    def _check_list_integrity(list_to_check: List[Any], type_of_list: type) -> bool:
        for item in list_to_check:
            if not isinstance(item, type_of_list):
                return False
        return True
                