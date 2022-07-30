from io import TextIOWrapper
from yaml import dump as upload_data # type: ignore
from yaml import Dumper
from yaml import YAMLError
from typing import List, Union

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
        
        
    def translate(self, content_to_translate: list) -> dict:
        """Translates the content of the YamlWrapper to the format of yaml library.

        Returns:
            dict: Content translated in the format accepted by yaml library.
        """
        pass
    
    def _write_to_file(self, content_to_write: dict) -> None:
        try:
            upload_data(content_to_write, self._file, Dumper)
        except YAMLError:
            raise WritingYamlException("Error writing the content to the yaml file.")
    
    def _apply_rule_rec(self, objects: List[Union[YamlDictionary, YamlList]], returned_value: dict) -> dict:
        if len(objects) == 0:
            return returned_value
        else:
            first_element: Union[YamlDictionary, YamlList] = objects[0]
            if(isinstance(first_element, YamlDictionary)):
                #TODO: Continue implementing the rule
                returned_value[first_element.key] = self._define_rule_to_apply(first_element.value)
         
        return {} # TODO: remove this return during implementation            
    
    def _define_rule_to_apply(self, object: Union[int, 
                                            str, 
                                            List[YamlDictionary], 
                                            YamlDictionary, 
                                            List["YamlList"],  
                                            YamlList]) -> Union[int,str, dict, list]:
        
        # TODO: Implemet all rules of the recusion that are based value.
        # object is:                    RETURN:
        # - int                         - int
        # - str                         - str
        # - List[YamlDictionary]        - recusion([YamlDictionary], [])
        # - YamlDictionary              - returned_value.[YamlDictionary.key] =  define_rule(YamlDictionary.value]+)
        # - List["YamlList"]            - recusion([YamlList], [])
        # - YamlList                    - if list = generic list return list, else recusion([YamlDictionary] or [YamlList], [])
        return {}