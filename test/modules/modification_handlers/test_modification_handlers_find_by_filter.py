from unittest import TestCase
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary

from src.utils.file.file_utils import FileUtil
from src.modules.modification_handlers.modification_handler import ModificationHandler
from src.modules.modification_handlers.exceptions.filter_not_found_exception import FilterNotFoundException
class TestModificationHanldersAdd(TestCase):
    def setUp(self) -> None:
        self.file_path = "tmp/test_modification_handlers_check.yaml"
        FileUtil.create_file_from_path(self.file_path)
        self.modification_handler: ModificationHandler  = ModificationHandler(self.file_path)
        
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
    
    def test_find_by_filter(self):
        filter: str = "value"
        self.modification_handler.load()
        self.modification_handler.add(filter, [YamlDictionary("sub_key", "value")])
        
        self.assertEqual(self.modification_handler.find_by_filter(filter), YamlDictionary(filter, [YamlDictionary("sub_key", "value")]))
        
        
    def test_find_by_filter_not_found(self):
        filter: str = "value"
        self.modification_handler.load()
        self.modification_handler.add(filter, [YamlDictionary("sub_key", "value")])
        
        with self.assertRaises(FilterNotFoundException):
            self.modification_handler.find_by_filter("not_valid_filter")