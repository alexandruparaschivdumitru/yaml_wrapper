from unittest import TestCase

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
        self.file_path = "tmp/test_API.yaml"
    
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
    def test_get_file_name(self) -> None:
        FileUtil.create_file_from_path(self.file_path)
        yaml_wrapper = YamlWrapper(self.file_path)
        self.assertEqual(yaml_wrapper.get_file_name(), self.file_path)
    
    def test_get_file_content(self) -> None:
        
        FileUtil.create_file("tmp/", "test_API", FileType.YAML, {"key": "value"})
        yaml_wrapper = YamlWrapper(self.file_path)
        self.assertEqual(yaml_wrapper.get_file_content(), [YamlDictionary("key", "value")])
    
    def test_update(self) -> None:
        FileUtil.create_file("tmp/", "test_API", FileType.YAML, {"key": "value"})
        yaml_wrapper = YamlWrapper(self.file_path)
        yaml_wrapper.update("key", "new_value")
        self.assertEqual(yaml_wrapper.get_file_content(), [YamlDictionary("key", "new_value")])
    
    def test_remove(self) -> None:
        FileUtil.create_file("tmp/", "test_API", FileType.YAML, {"key": "value"})
        yaml_wrapper = YamlWrapper(self.file_path)
        yaml_wrapper.remove("key")
        self.assertEqual(yaml_wrapper.get_file_content(), [])