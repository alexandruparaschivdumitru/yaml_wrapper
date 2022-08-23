from unittest import TestCase
from src.modules.modification_handlers.exceptions.key_already_used_exception import KeyAlreadyUsedException
from src.modules.modification_handlers.modification_handler import ModificationHandler
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.utils.file.file_utils import FileUtil

class TestModificationHanldersAdd(TestCase):
    def setUp(self) -> None:
        self.file_path = "tmp/test_modification_handlers_check.yaml"
        FileUtil.create_file_from_path(self.file_path)
        self.modification_handler: ModificationHandler  = ModificationHandler(self.file_path)
        
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
    def test_add_with_existing_key(self):
        key: str = "key"
        self.modification_handler.load()
        self.modification_handler._object = [YamlDictionary(key, "value")]
        with self.assertRaises(KeyAlreadyUsedException):
            self.modification_handler.add(key, "value")
    
    def test_add_dictionary(self):
        key: str = "key"
        self.modification_handler.load()
        self.modification_handler.add(key, [YamlDictionary("sub_key", "value")])
        
        self.assertEqual(self.modification_handler.get(), [
            YamlDictionary("key", [YamlDictionary("sub_key", "value")])
            ])