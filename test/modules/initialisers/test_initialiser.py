from unittest import TestCase
from src.modules.initialisers.initialiser import Initialiser
from src.modules.translators.from_yaml_traslator import FromYamlTraslator
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary

from src.utils.file.enums.file_type import FileType
from src.utils.file.file_utils import FileUtil

class TestInitialiser(TestCase):
    def setUp(self) -> None:
        self.file_directory: str = "tmp/"
        self.file_name: str = "test_file_initializer"
        self.file_type: FileType = FileType.YAML
        self.file_path: str = self.file_directory + self.file_name + self.file_type.value
        
        self.file_content = {"key": "value"}
        
        FileUtil.create_file(self.file_directory, self.file_name, self.file_type, self.file_content)        
        
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
    def test_read_from_file(self):
        initialiser: Initialiser = Initialiser(self.file_path)
        
        self.assertEqual(initialiser.initialise(), [YamlDictionary(key='key', value='value')])
    
    def test_file_not_found_exception(self):
        file_not_existent_path: str = "tmp/file_not_existent.yaml"
        
        with self.assertRaises(FileNotFoundError):
            initialiser: Initialiser = Initialiser(file_not_existent_path)
            initialiser.initialise()