from io import TextIOWrapper
from unittest import TestCase

from src.modules.translator.from_yaml_traslator import FromYamlTraslator
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
    
    def test_conversion(self):
        token_to_traslate: dict = {'name': 'Argos - UniUD Sailing Lab',
                                   'serials': [{'label': 'Chinese_GPS', 'speed': 9600, 'address': '/dev/ttyACM0'}],
                                   'server': {'host': 'localhost', 'port': 4545}}
        
        file: TextIOWrapper = open(self.file_path + self.file_name + self.file_type.value, "r") #TODO: handle the problem with the file close.
        traslator: FromYamlTraslator = FromYamlTraslator(file) # TODO: Change to a ChainMap
        file.close()
        content_traslated: dict = {1: YamlDictionary("name", "value"),
                                   2: YamlDictionary("serials",YamlList([[YamlDictionary("label", "Chinese_GPS"),
                                                                       YamlDictionary("speed", 9600),
                                                                       YamlDictionary("address", "/dev/ttyACM0")]]
                                                                    )
                                                ),
                                   3: YamlDictionary("server", [YamlDictionary("host", "localhost"),
                                                             YamlDictionary("port", 4545)])
                                   }
        
        #print(content_traslated)
        for i in range (1,4):
            print(content_traslated[i].key)
        self.assertNotEqual(traslator.translate(), content_traslated)