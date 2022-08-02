from unittest import TestCase
from yaml import dump as upload_data # type: ignore
from yaml import Dumper # type: ignore
from src.modules.modification_handlers.modification_handler import ModificationHandler
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.utils.file.file_utils import FileUtil

class TestModificationHandlers(TestCase):
    def setUp(self) -> None:
        self.file_path = "tmp/test_modification_handlers.yaml"
        FileUtil.create_file_from_path(self.file_path)
        self.modification_handler: ModificationHandler  = ModificationHandler(self.file_path)
        
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
    def test_load(self) -> None:
        upload_data(self.file_path, {"key": "value"}, Dumper)
       
        self.assertEqual(self.modification_handler.load(), [YamlDictionary("key", "value")])
        
    def test_load_empty_file(self) -> None:
        self.modification_handler.load()
        
        self.assertEqual(self.modification_handler.load(), [])
        
    def test_check_true(self) -> None:
        upload_data(self.file_path, {"key": "value"}, Dumper)
        self.modification_handler.load()
        
        self.assertTrue(self.modification_handler.check("key", "value"))
    
    def test_check_false(self) -> None:
        upload_data(self.file_path, {"key": "value"}, Dumper)
        self.modification_handler.load()
        
        self.assertFalse(self.modification_handler.check("key", "value_1"))
        
    def test_update(self) -> None:
        upload_data(self.file_path, {"key": "value"}, Dumper)
        self.modification_handler.load()
        
        self.assertEqual(self.modification_handler.update("key", "value_1"), [YamlDictionary("key", "value_1")])
    
    def test_remove(self) -> None:
        upload_data(self.file_path, {"key": "value"}, Dumper)
        self.modification_handler.load()
        
        self.assertEqual(self.modification_handler.remove("key"), [])