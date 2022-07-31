from io import TextIOWrapper
from unittest import TestCase
from src.modules.translators.from_yaml_traslator import FromYamlTraslator
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList
from src.utils.file.enums.file_type import FileType
from src.utils.file.file_utils import FileUtil

class TestFromYamlTraslator(TestCase):
    def setUp(self) -> None:
        self.file_path: str = "tmp/"
        self.file_name: str = "traslator_file"
        self.file_type: FileType = FileType.YAML
        self.file_content: dict = {'name': 'value',
                                   'serials': [{'label': 'Chinese_GPS', 'speed': 9600, 'address': '/dev/ttyACM0'}],
                                   'server': {'host': 'localhost', 'port': 4545}}
        FileUtil.create_file(self.file_path, self.file_name, self.file_type, self.file_content)
    
    def tearDown(self) -> None:
        file_path: str = "tmp/traslator_file.yaml"
        FileUtil.delete_file(file_path)
    
    def test_translate(self):
        file: TextIOWrapper = open(self.file_path + self.file_name + self.file_type.value, "r")
        translator: FromYamlTraslator = FromYamlTraslator(file)
        
        content_traslated: dict = [ YamlDictionary("name", "value"),
                                    YamlDictionary("serials",YamlList([[
                                                                        YamlDictionary("address", "/dev/ttyACM0"),
                                                                        YamlDictionary("label", "Chinese_GPS"),
                                                                        YamlDictionary("speed", 9600)]]
                                                                    )
                                                ),
                                    YamlDictionary("server", [YamlDictionary("host", "localhost"),
                                                             YamlDictionary("port", 4545)])
                                    ]
   
        # NOTE: This test can fail due to the order of "serials" value.
        self.assertEqual(translator.translate(), content_traslated)