from unittest import TestCase

from src.API.exceptions.key_already_used_exception import KeyAlreadyUsedException
from src.API.exceptions.key_not_found_exception import KeyNotFoundException

from src.API.yaml_wrapper import YamlWrapper
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList

class TestYamlWrapper(TestCase):
    def setUp(self) -> None:
        self.yaml_file: YamlWrapper = YamlWrapper("yaml_file.yaml")
    
    def test_create_dictionary(self):
        dictionary: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
        self.assertIsInstance(dictionary, YamlDictionary)
        
    def test_check_key_in_dictionary(self):
        dictionary: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
        self.assertEqual(dictionary.key, "name")
    
    def test_check_keyvalue_in_dictionary(self):
        dictionary: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
        self.assertEqual(dictionary.value, "key_value")
        
    def test_create_two_dictionary(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name_2", "key_value_2")
        
        self.assertEqual(self.yaml_file.get_keys(), ["name_1", "name_2"])
        
    def test_create_two_dictionary_with_same_name(self):
        with self.assertRaises(KeyAlreadyUsedException):
            dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
            dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
    
    def test_remove_dictionary(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name_2", "key_value_2")
        
        dictionary_removed: YamlDictionary = self.yaml_file.remove_dictionary("name_1")
        
        self.assertEqual(self.yaml_file.get_keys(), ["name_2"])
    
    def test_remove_nested_dictionary(self):
        dictionary_1: YamlDictionary = YamlDictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = YamlDictionary("name_2", "key_value_1")
        dictionary_3: YamlDictionary = self.yaml_file.create_dictionary("name_3", [dictionary_1, dictionary_2])
        
        self.yaml_file.remove_dictionary("name_3.name_1")
        self.assertEqual(self.yaml_file.get_value("name_3"), [dictionary_2])
    
    def test_remove_unexistent_dictionary(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name_2", "key_value_2")
        
        with self.assertRaises(KeyNotFoundException):
             dictionary_removed: YamlDictionary = self.yaml_file.remove_dictionary("name")
    
    def test_get_value(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name_2", "key_value_2")
        
        self.assertEqual(self.yaml_file.get_value("name_1"),  "key_value_1")
        
    def test_modify_dictionary(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary =YamlDictionary("name_2", "key_value_2")
        
        self.yaml_file.modify_dictionary("name_1", dictionary_2), 
        self.yaml_file.get_value("name_1")
        self.assertEqual(self.yaml_file.get_value("name_1"), dictionary_2)
        
    def test_create_list(self):
        dictionary_1: YamlDictionary = YamlDictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = YamlDictionary("name_2", "key_value_2")
        
        list_1: YamlList = self.yaml_file.create_new_list([dictionary_1, dictionary_2])
        
        self.assertFalse(self.yaml_file.is_empty())
        