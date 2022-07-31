from io import TextIOWrapper
from yaml import dump as upload_data # type: ignore
from yaml import Dumper
from yaml import YAMLError
from typing import Any, List, Union, cast
from src.modules.translators.exceptions.rule_not_found_exception import RuleNotFoundException

from src.modules.translators.exceptions.writing_yaml_exception import WritingYamlException
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList


class ToYamlTranslator:
    """Translator from the format of Yaml wrapper, to the format of yaml library.
    """
    def __init__(self , file: TextIOWrapper) -> None:
        self._file: TextIOWrapper = file
        
    def __del__(self):
        self._file.close()
        
        
    def translate(self, content_to_translate: list) -> Union[dict, list]:
        """Translates the content of the YamlWrapper to the format of yaml library.

        Returns:
            dict: Content translated in the format accepted by yaml library.
        """
        content_to_write: Union[dict, list] = self._apply_rule_rec(content_to_translate, {})
        self._write_to_file(content_to_write)
        return content_to_write
    
    def _write_to_file(self, content_to_write: Union[dict, list]) -> None:
        try:
            upload_data(content_to_write, self._file, Dumper)
        except YAMLError:
            raise WritingYamlException("Error writing the content to the yaml file.")
        
    
    
    # TODO: handle case that are not correct.
    def _apply_rule_rec(self, objects: Union[List[YamlDictionary], List[YamlList], Any], returned_value: dict):
        if len(objects) == 0:
            return returned_value
        else:
            first_object: Union[YamlDictionary, YamlList] = objects.pop(0)
            
            if isinstance(first_object, YamlDictionary):
                if isinstance(first_object.value, str) or isinstance(first_object.value, int):
                    
                    returned_value[first_object.key] = first_object.value 
                    
                elif isinstance(first_object.value, list) and isinstance(first_object.value[0], YamlDictionary):
                   
                    returned_value[first_object.key] = self._apply_rule_rec(first_object.value, {})
                    
                else:
                    returned_value[first_object.key] = self._apply_rule_rec([first_object.value], {})

                return  self._apply_rule_rec(objects, returned_value)
            else:
                if  isinstance(first_object, YamlList) and  isinstance(first_object.values[0], YamlDictionary):
                    
                    return [self._apply_rule_rec(first_object.values, {})]
                else:
                    return first_object.values
                