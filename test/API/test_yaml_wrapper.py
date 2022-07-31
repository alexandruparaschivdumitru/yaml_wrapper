from unittest import TestCase
from unittest import skip
import os
import os.path as path

import yaml # type: ignore

from src.API.exceptions.empty_list_exception import EmptyListException
from src.API.exceptions.key_already_used_exception import KeyAlreadyUsedException
from src.API.exceptions.key_not_found_exception import KeyNotFoundException

from src.API.yaml_wrapper import YamlWrapper
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList
from src.utils.file.enums.file_type import FileType
from src.utils.file.file_utils import FileUtil

class TestYamlWrapper(TestCase):
    def setUp(self) -> None:
        self.yaml_file: YamlWrapper = YamlWrapper("yaml_file.yaml")
    
    @skip("WIP: Not implemented yet")
    def test_create_dictionary(self):
        dictionary: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
        self.assertIsInstance(dictionary, YamlDictionary)
    
    @skip("WIP: Not implemented yet")    
    def test_check_key_in_dictionary(self):
        dictionary: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
        self.assertEqual(dictionary.key, "name")
    
    @skip("WIP: Not implemented yet")
    def test_check_keyvalue_in_dictionary(self):
        dictionary: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
        self.assertEqual(dictionary.value, "key_value")
    
    @skip("WIP: Not implemented yet")    
    def test_create_two_dictionary(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name_2", "key_value_2")
        
        self.assertEqual(self.yaml_file.get_keys(), ["name_1", "name_2"])
        
    @skip("WIP: Not implemented yet")
    def test_create_two_dictionary_with_same_name(self):
        with self.assertRaises(KeyAlreadyUsedException):
            dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
            dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name", "key_value")
    
    @skip("WIP: Not implemented yet")
    def test_remove_dictionary(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name_2", "key_value_2")
        
        dictionary_removed: YamlDictionary = self.yaml_file.remove_dictionary("name_1")
        
        self.assertEqual(self.yaml_file.get_keys(), ["name_2"])
    
    @skip("WIP: Not implemented yet")
    def test_remove_nested_dictionary(self):
        dictionary_1: YamlDictionary = YamlDictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = YamlDictionary("name_2", "key_value_1")
        dictionary_3: YamlDictionary = self.yaml_file.create_dictionary("name_3", [dictionary_1, dictionary_2])
        
        self.yaml_file.remove_dictionary("name_3.name_1")
        self.assertEqual(self.yaml_file.get_value("name_3"), [dictionary_2])
    
    @skip("WIP: Not implemented yet")
    def test_remove_unexistent_dictionary(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name_2", "key_value_2")
        
        with self.assertRaises(KeyNotFoundException):
             dictionary_removed: YamlDictionary = self.yaml_file.remove_dictionary("name")
    
    @skip("WIP: Not implemented yet")
    def test_get_value(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = self.yaml_file.create_dictionary("name_2", "key_value_2")
        
        self.assertEqual(self.yaml_file.get_value("name_1"),  "key_value_1")
        
    @skip("WIP: Not implemented yet")
    def test_modify_dictionary(self):
        dictionary_1: YamlDictionary = self.yaml_file.create_dictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary =YamlDictionary("name_2", "key_value_2")
        
        self.yaml_file.modify_dictionary("name_1", dictionary_2), 
        self.yaml_file.get_value("name_1")
        self.assertEqual(self.yaml_file.get_value("name_1"), dictionary_2)
    
    @skip("WIP: Not implemented yet")    
    def test_create_list(self):
        dictionary_1: YamlDictionary = YamlDictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = YamlDictionary("name_2", "key_value_2")
        
        list_1: YamlList = self.yaml_file.create_new_list([dictionary_1, dictionary_2])
        
        self.assertFalse(self.yaml_file.is_empty())
    
    @skip("WIP: Not implemented yet")
    def test_remove_from_empty_list(self):
        dictionary_1: YamlDictionary = YamlDictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = YamlDictionary("name_2", "key_value_2")
        
        list_1: YamlList = self.yaml_file.create_new_list([dictionary_1, dictionary_2])
        
        with self.assertRaises(EmptyListException):
            self.yaml_file.remove_from_list("")
            self.yaml_file.remove_from_list("")
            self.yaml_file.remove_from_list("")
    
    @skip("WIP: Not implemented yet")
    def test_remove_dictionary_with_empty_list(self):
        dictionary_1: YamlDictionary = YamlDictionary("name_1", "key_value_1")
        dictionary_2: YamlDictionary = YamlDictionary("name_2", "key_value_2")
        
        self.yaml_file.create_dictionary("name", YamlList([dictionary_1, dictionary_2]))
        
        self.yaml_file.remove_from_list("name.name_1")
        self.yaml_file.remove_from_list("name.name_2")
        
        self.assertEqual(self.yaml_file.get_structure(), {})
    
    
class TestYamlWrapperIO(TestCase):
    
    @skip("WIP: Not implemented yet")
    def test_handle_no_existent_file(self):
        path_file: str = "yaml_file_1.yaml"
        yaml_file_not_existent: YamlWrapper = YamlWrapper(path_file)
        
        self.assertTrue(path.exists(path_file))
        
    @skip("WIP: Not implemented yet")    
    def test_read_from_file(self):
        path_file: str = "tmp/yaml_file_populated.yaml"
        FileUtil.create_file("tmp/", "yaml_file_populated", FileType.YAML, {'name': 'value'})
        read_from_file: YamlWrapper = YamlWrapper(path_file)
        FileUtil.delete_file("tmp/yaml_file_populated.yaml")
        self.assertNotEqual(read_from_file.get_structure(), {})