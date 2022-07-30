from io import TextIOWrapper
from yaml import load as download_data # type: ignore
from yaml import Loader # type: ignore
from typing import List, Any

from src.modules.translators.enums.rule_type import ListRuleType, RuleType
from src.modules.translators.utils.rule_util import RuleFromValueUtil
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList


class FromYamlTraslator:
    """ Translator from the format of yaml library, to the format accepeted from the YamlWrapper
    """
    def __init__(self , file: TextIOWrapper) -> None:
        self._file: TextIOWrapper = file
        
    def __del__(self):
        self._file.close()
        
    def translate(self)-> list:
        """Returns a dict in the right format for YamlWrapper, with the content of yaml file

        Returns:
            list: Yaml file content in right format
        """
        data_from_file: dict =  self._read_from_file()
        
        keys: list = []
        for key in data_from_file.keys():
            keys.append(key)
        rules_applied: list = self._apply_rule_rec(keys, data_from_file, [])
        
        return rules_applied
    
    def _read_from_file(self) -> dict:
        data_from_file: dict = download_data(self._file, Loader)
        
        if data_from_file is None:
            return {}
        
        return data_from_file
    
    def _convert_dict_keys_to_dict(self, keys: Any) -> list:
        dict_keys_accumulator: list = []
        for key in keys:
            dict_keys_accumulator.append(key)
        
        return dict_keys_accumulator
            
    def _apply_rule_rec(self, keys: List[str], data: dict, returned_value: list ) -> list:  
           
        if len(keys) == 0:
             return returned_value
        else:
            
            first_key: str = keys[0]
            
            rule_to_apply: RuleType = RuleFromValueUtil.define_rule_from_value(data[first_key])
            
            if rule_to_apply == RuleType.INT_RULE or rule_to_apply == RuleType.STR_RULE:
                returned_value.append(YamlDictionary(first_key, data[first_key]))
                
            elif rule_to_apply == RuleType.LIST_DICT_RULE:
                
                sub_keys: list = self._convert_dict_keys_to_dict(data[first_key].keys())
                returned_value.append(YamlDictionary(first_key, self._apply_rule_rec(sub_keys, data[first_key], [])))
            
            elif rule_to_apply == RuleType.LIST_RULE:
                data_copy = data[first_key]
                list_type: ListRuleType = RuleFromValueUtil.define_list_rule_type_from_value(data_copy)
        
                if list_type == ListRuleType.DICT_TYPE:
                    accumulator: List[Any] = []
                    
                    for item in  range(0, len(data[first_key])):
                        sub_keys_list : list = self._convert_dict_keys_to_dict(data[first_key][item].keys())
                       
                        accumulator.append(self._apply_rule_rec(sub_keys_list, data[first_key][item], []))
                    
                    returned_value.append(YamlDictionary(first_key, YamlList(accumulator)))

                else:
                       
                    returned_value.append(YamlDictionary(first_key, YamlList(data[first_key][item])))
     
                 
        return self._apply_rule_rec(keys[1:], data, returned_value)            