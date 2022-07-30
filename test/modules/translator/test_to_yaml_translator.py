from io import TextIOWrapper
from unittest import TestCase
from yaml import Loader # type: ignore
from yaml import load as download_data # type: ignore
from yaml import dump as upload_data # type: ignore
from src.modules.translators.to_yaml_translator import ToYamlTranslator # type: ignore
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList
from src.utils.file.enums.file_type import FileType

from src.utils.file.file_utils import FileUtil # type: ignore

class TestToYamlTranslator(TestCase):
    def setUp(self) -> None:
        self.directory: str = "tmp/"
        self.file_name: str = "test_to_yaml_traslator_file"
        self.file_type: FileType = FileType.YAML
        self.file_path = self.directory + self.file_name + self.file_type.value
        FileUtil.create_empty_file(self.directory, self.file_name, self.file_type)
        
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
        
    def test_translate(self):
        content_to_write: list = [
                                YamlDictionary("name", "value"),
                                YamlDictionary("serials",YamlList([[
                                                                        YamlDictionary("address", "/dev/ttyACM0"),
                                                                        YamlDictionary("label", "Chinese_GPS"),
                                                                        YamlDictionary("speed", 9600)]]
                                                                    )
                                                ),
                                YamlDictionary("server", [YamlDictionary("host", "localhost"),
                                                             YamlDictionary("port", 4545)])
                                    ]
        
        file: TextIOWrapper = open(self.file_path, "w")
        translator: ToYamlTranslator = ToYamlTranslator(file)
        
        self.assertEqual(translator.translate(content_to_write), {'name': 'value',
                                   'serials': [{'label': 'Chinese_GPS', 'speed': 9600, 'address': '/dev/ttyACM0'}],
                                   'server': {'host': 'localhost', 'port': 4545}})
        
    def test_correct_write_in_yaml_file(self):
        content_to_write: list = [
                                YamlDictionary("name", "value"),
                                YamlDictionary("serials",YamlList([[
                                                                        YamlDictionary("address", "/dev/ttyACM0"),
                                                                        YamlDictionary("label", "Chinese_GPS"),
                                                                        YamlDictionary("speed", 9600)]]
                                                                    )
                                                ),
                                YamlDictionary("server", [YamlDictionary("host", "localhost"),
                                                             YamlDictionary("port", 4545)])
                                    ]
        
        file: TextIOWrapper = open(self.file_path, "w")
        translator: ToYamlTranslator = ToYamlTranslator(file)
        translator.translate(content_to_write)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
                file_read_content = download_data(file_read,Loader)
        
        self.assertEqual(file_read_content, {'name': 'value',
                                   'serials': [{'label': 'Chinese_GPS', 'speed': 9600, 'address': '/dev/ttyACM0'}],
                                   'server': {'host': 'localhost', 'port': 4545}})