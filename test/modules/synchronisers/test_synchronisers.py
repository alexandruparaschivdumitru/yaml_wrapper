from unittest import TestCase
from src.modules.synchronisers.exceptions.not_synchronisable_object_exception import NotSynchronisableObjectException
from src.modules.synchronisers.synchroniser import Synchroniser
from src.modules.translators.from_yaml_traslator import FromYamlTraslator
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary

from src.utils.file.enums.file_type import FileType
from src.utils.file.file_utils import FileUtil

class TestSynchroniser(TestCase):
    def setUp(self) -> None:
        self.file_directory: str = "tmp/"
        self.file_name: str = "test_file_initializer"
        self.file_type: FileType = FileType.YAML
        self.file_path: str = self.file_directory + self.file_name + self.file_type.value
        
        self.file_content = [YamlDictionary(key='key', value='value')]
        
        FileUtil.create_empty_file(self.file_directory, self.file_name, self.file_type)        
        
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
    def test_synchronise(self):
        synchroniser: Synchroniser = Synchroniser(self.file_path)
        
        self.assertEqual(synchroniser.synchronise(self.file_content), {"key": "value"})
    
    def test_controll_file_synchronised(self):
        file_synchronised_path: str = "tmp/test_file_synchronized.yaml"
        FileUtil.create_file_from_path(file_synchronised_path) 
        
        synchroniser: Synchroniser = Synchroniser(file_synchronised_path)
        synchroniser.synchronise(self.file_content)
        
        from_yaml_traslator: FromYamlTraslator = FromYamlTraslator(file_synchronised_path)
        file_synchronised_content: list = from_yaml_traslator.translate()
        FileUtil.delete_file(file_synchronised_path)
        
        self.assertEqual(file_synchronised_content, [YamlDictionary(key='key', value='value')])
        
    def test_check_if_content_is_synchronizable(self):
        synchroniser: Synchroniser = Synchroniser(self.file_path)
        
        not_sync_content: list = [{"key": "key", "value":"value"}]
        
        with self.assertRaises(NotSynchronisableObjectException):
            synchroniser.synchronise(not_sync_content)