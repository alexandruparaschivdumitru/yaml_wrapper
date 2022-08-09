from io import TextIOWrapper
from unittest import TestCase
from unittest import skip
from src.modules.translators.from_yaml_traslator import FromYamlTraslator
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList
from src.utils.file.enums.file_type import FileType
from src.utils.file.file_utils import FileUtil

class TestFromYamlTraslator(TestCase):
    def setUp(self) -> None:
        self.file_directory: str = "tmp/"
        self.file_name: str = "traslator_file"
        self.file_type: FileType = FileType.YAML
        self.file_path: str = self.file_directory + self.file_name + self.file_type.value
    
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
    
    def test_general_translate(self):
        file_content: dict = { 
                                'name': 'value',
                                'serials': [{'label': 'Chinese_GPS', 'speed': 9600, 'address': '/dev/ttyACM0'}],
                                'server': {'host': 'localhost', 'port': 4545}
                            }
        
        FileUtil.create_file(self.file_directory, self.file_name, self.file_type, file_content)
        translator: FromYamlTraslator = FromYamlTraslator(self.file_directory + self.file_name + self.file_type.value)
        
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
    
    def test_translate_empty_file(self):
        FileUtil.create_empty_file(self.file_directory, self.file_name, self.file_type)
        translator: FromYamlTraslator = FromYamlTraslator(self.file_directory + self.file_name + self.file_type.value)
        
        self.assertEqual(translator.translate(), [])
    
    def test_translate_file_with_list(self):
        file_content = [1, 2, 3]
        FileUtil.create_file(self.file_directory, self.file_name, self.file_type, file_content)
        translator: FromYamlTraslator = FromYamlTraslator(self.file_directory + self.file_name + self.file_type.value)
        
        self.assertEqual(translator.translate(), [YamlList(file_content)])
    
    def test_list_with_dict(self):
        file_content = [{"key_1_A": "key_1_A_value",
                         "key_2_A": "key_2_A_value"
                         },
                        {"key_1_B": "key_1_B_value",
                         "key_2_B": "key_2_B_value"}
                        
                        ]
        file_content_translated: list = [YamlList(
                                                    [
                                                        [YamlDictionary("key_1_A", "key_1_A_value"),YamlDictionary("key_2_A", "key_2_A_value"),],
                                                        [YamlDictionary("key_1_B", "key_1_B_value"),YamlDictionary("key_2_B", "key_2_B_value"),],
                                                    ]
                                                )]
        FileUtil.create_file(self.file_directory, self.file_name, self.file_type, file_content)
        translator: FromYamlTraslator = FromYamlTraslator(self.file_directory + self.file_name + self.file_type.value)
        
        self.assertEqual(translator.translate(), file_content_translated)
    
    def test_dict_with_one_key(self):
        file_content: dict = {"key": {"sub_key_1": "value_1", "sub_key_2": "value_2"}}
        file_content_translated: list = [YamlDictionary("key", [YamlDictionary("sub_key_1", "value_1"), 
                                                                YamlDictionary("sub_key_2", "value_2")]
                                                        )
                                        ]
        
        FileUtil.create_file(self.file_directory, self.file_name, self.file_type, file_content)
        translator: FromYamlTraslator = FromYamlTraslator(self.file_directory + self.file_name + self.file_type.value)
        
        self.assertEqual(translator.translate(), file_content_translated)
        
    def test_dict_with_multiple_keys(self):
        file_content: dict = {"key_1": "key_1_value",
                              "key_2": 2,
                              "key_3": {"sub_key_1": "value_1", "sub_key_2": "value_2"}
                              }
        
        
        file_content_translated: list = [YamlDictionary("key_1", "key_1_value"),
                                         YamlDictionary("key_2", 2),
                                         YamlDictionary("key_3", [YamlDictionary("sub_key_1", "value_1"),
                                                                  YamlDictionary("sub_key_2", "value_2")
                                                                  ])
                                        ]
        
        FileUtil.create_file(self.file_directory, self.file_name, self.file_type, file_content)
        translator: FromYamlTraslator = FromYamlTraslator(self.file_directory + self.file_name + self.file_type.value)
        
        self.assertEqual(translator.translate(), file_content_translated)
    
    def test_dict_with_list(self):
        file_content: dict = {
                                "key_1": [
                                            {"sub_key_1_A": "value_1_A",
                                            "sub_key_2_A": "value_2_A"},
                                            {"sub_key_1_B": "value_1_B",
                                            "sub_key_2_B": "value_2_B"}
                                        ],
                                "key_2": "key_2_value",
                            }
        file_content_translated: list = [
                                            YamlDictionary("key_1", 
                                                        YamlList(
                                                                    [
                                                                        [
                                                                        YamlDictionary("sub_key_1_A", "value_1_A"),
                                                                        YamlDictionary("sub_key_2_A", "value_2_A"),
                                                                        ],
                                                                        [
                                                                        YamlDictionary("sub_key_1_B", "value_1_B"),
                                                                        YamlDictionary("sub_key_2_B", "value_2_B"),
                                                                        ]
                                                                    ]
                                                                )
                                                            ),
                                            YamlDictionary("key_2", "key_2_value")
                                        ]
        FileUtil.create_file(self.file_directory, self.file_name, self.file_type, file_content)
        translator: FromYamlTraslator = FromYamlTraslator(self.file_directory + self.file_name + self.file_type.value)
        
        self.assertEqual(translator.translate(), file_content_translated)
        
    
    def test_with_multiple_sub_dict(self):
        file_content: dict = {"key": {"sub_key": {"sub_sub_key": "value"}}}
        file_content_translated: list = [YamlDictionary("key", 
                                                        [YamlDictionary("sub_key", 
                                                                        [YamlDictionary("sub_sub_key", "value")]
                                                                        )
                                                        ]
                                                        )
                                        ]
        FileUtil.create_file(self.file_directory, self.file_name, self.file_type, file_content)
        translator: FromYamlTraslator = FromYamlTraslator(self.file_directory + self.file_name + self.file_type.value)
        
        self.assertEqual(translator.translate(), file_content_translated)
        
    