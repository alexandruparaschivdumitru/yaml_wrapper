from unittest import TestCase

from src.modules.converters.to_json_converter import ToJsonConverter
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList

class TestToJsonConverter(TestCase):
    def test_empty_conversion(self):
        empty_list: list = []
        conversion: str = "{}"
        
        
        self.assertEqual(ToJsonConverter.convert(empty_list), conversion)
        
    def test_key_conversion(self):
        value_to_convert: list = [YamlDictionary("key_1", "value_1"), YamlDictionary("key_2", "value_2")]
        conversion: str = "{\"key_1\": \"value_1\", \"key_2\": \"value_2\"}"
        
        self.assertEqual(ToJsonConverter.convert(value_to_convert), conversion)
        
    
    def test_key_with_list_conversion(self):
        value_to_convert: list = [YamlDictionary("key_1", YamlList([1, 2, 3]))]
        conversion: str = "{\"key_1\": [1, 2, 3]}"
        
        self.assertEqual(ToJsonConverter.convert(value_to_convert), conversion)
        
    def test_key_with_list_of_dictionaries_with_one_item_conversion(self):
        value_to_convert: list = [
            YamlDictionary("key_1", YamlList([
                                                [
                                                    YamlDictionary("sub_key_1", "value_1"), 
                                                    YamlDictionary("sub_key_2", "value_2")
                                                ]
                                            ])
                                    
                        )]
        conversion: str = "{\"key_1\": [{\"sub_key_1\": \"value_1\", \"sub_key_2\": \"value_2\"}]}"
        
        self.assertEqual(ToJsonConverter.convert(value_to_convert), conversion)
        
    def test_key_with_list_of_dictionaries_with_more_items_conversion(self):
        value_to_convert: list = [
            YamlDictionary("key_1", YamlList([
                                                [
                                                    YamlDictionary("sub_key_1_A", "value_1"), 
                                                    YamlDictionary("sub_key_2_A", "value_2")
                                                ],
                                                [
                                                    YamlDictionary("sub_key_1_B", "value_1"), 
                                                    YamlDictionary("sub_key_2_B", "value_2")
                                                ]
                                            ])
                                    
                        )]
        conversion: str = "{\"key_1\": [{\"sub_key_1_A\": \"value_1\", \"sub_key_2_A\": \"value_2\"}, {\"sub_key_1_B\": \"value_1\", \"sub_key_2_B\": \"value_2\"}]}"
        
        self.assertEqual(ToJsonConverter.convert(value_to_convert), conversion)