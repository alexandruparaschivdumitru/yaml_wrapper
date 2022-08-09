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
        
        
    def test_general_translate(self):
        content_to_write: list = [
                                YamlDictionary("key_1", "key_1_value"),
                                YamlDictionary("key_2",YamlList([[
                                                                YamlDictionary("sub_key_1", "sub_key_1_value"),
                                                                YamlDictionary("sub_key_2", "sub_key_2_value"),
                                                                YamlDictionary("sub_key_3", 1)
                                                                ]])
                                                ),
                                YamlDictionary("key_3", [YamlDictionary("sub_key_1", "sub_key_1_value"),
                                                        YamlDictionary("sub_key_2", 1)]
                                               )
                                    ]
        content_translated: dict = {'key_1': 'key_1_value',
                                   'key_2': [{'sub_key_1': 'sub_key_1_value', 
                                              'sub_key_2': 'sub_key_2_value', 
                                              'sub_key_3': 1}],
                                   'key_3': {'sub_key_1': 'sub_key_1_value', 
                                             'sub_key_2': 1}}
        
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translated = translator.translate(content_to_write)
        
        self.assertEqual(translated, content_translated)
        
    def test_correct_write_in_yaml_file(self):
        content_to_write: list = [
                                YamlDictionary("key_1", "key_1_value"),
                                YamlDictionary("key_2",YamlList([[
                                                                YamlDictionary("sub_key_1", "sub_key_1_value"),
                                                                YamlDictionary("sub_key_2", "sub_key_2_value"),
                                                                YamlDictionary("sub_key_3", 1)
                                                                ]])
                                                ),
                                YamlDictionary("key_3", [YamlDictionary("sub_key_1", "sub_key_1_value"),
                                                        YamlDictionary("sub_key_2", 1)]
                                               )
                                    ]
        content_translated: dict = {'key_1': 'key_1_value',
                                   'key_2': [{'sub_key_1': 'sub_key_1_value', 
                                              'sub_key_2': 'sub_key_2_value', 
                                              'sub_key_3': 1}],
                                   'key_3': {'sub_key_1': 'sub_key_1_value', 
                                             'sub_key_2': 1}}
        
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate(content_to_write)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, content_translated)
        
        
    def test_write_list(self):
        content_to_write: list = [YamlList([1, 2, 3, 4])]
            
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate(content_to_write)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, [1, 2, 3, 4])
    
    def test_translate_multiple_times(self):
        content_to_write: list = [YamlList([1, 2, 3, 4])]
            
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate(content_to_write)
        translator.translate(content_to_write)
        translator.translate(content_to_write)
        translator.translate(content_to_write)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, [1, 2, 3, 4])
        
    def test_dict_with_list(self):
        content_to_translate: list = [YamlDictionary("key", YamlList([
                                                                        [YamlDictionary("sub_key_1_A", "sub_key_1_A_value"),
                                                                         YamlDictionary("sub_key_2_A", "sub_key_2_A_value"),],
                                                                        [YamlDictionary("sub_key_1_B", "sub_key_1_B_value"),
                                                                         YamlDictionary("sub_key_2_B", "sub_key_2_B_value"),]
                                                                    ])
                                                    )
                                        ]
        
        content_translated: dict = {"key":[{"sub_key_1_A": "sub_key_1_A_value",
                                            "sub_key_2_A": "sub_key_2_A_value"},
                                           {"sub_key_1_B": "sub_key_1_B_value",
                                            "sub_key_2_B": "sub_key_2_B_value"}]}
    
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate(content_to_translate)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, content_translated)
        
    
    def test_dict_with_sub_dict(self):
        content_to_translate: list = [YamlDictionary("key", [YamlDictionary("sub_key_1", "sub_key_1_value"),
                                                              YamlDictionary("sub_key_2", "sub_key_2_value")
                                                              ]
                                                      )
                                       ]
        
        content_translated: dict = {"key": {"sub_key_1": "sub_key_1_value",
                                            "sub_key_2": "sub_key_2_value",}}
        
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate(content_to_translate)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, content_translated)
    
    def test_multiple_dicts(self):
        content_to_translate: list = [YamlDictionary("key_1", "key_1_value"),
                                         YamlDictionary("key_2", 2),
                                         YamlDictionary("key_3", [YamlDictionary("sub_key_1", "value_1"),
                                                                  YamlDictionary("sub_key_2", "value_2")
                                                                  ])
                                        ]
        content_translated: dict = {"key_1": "key_1_value",
                              "key_2": 2,
                              "key_3": {"sub_key_1": "value_1", "sub_key_2": "value_2"}
                              }
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate(content_to_translate)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, content_translated)
    
    def test_multi_dict_with_list(self):
        content_translated: dict = {
                                "key_1": [
                                            {"sub_key_1_A": "value_1_A",
                                            "sub_key_2_A": "value_2_A"},
                                            {"sub_key_1_B": "value_1_B",
                                            "sub_key_2_B": "value_2_B"}
                                        ],
                                "key_2": "key_2_value",
                            }
        content_to_translate: list = [
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
        
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate(content_to_translate)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, content_translated)
        
    def test_with_multiple_sub_dict(self):
        content_to_translate: list = [YamlDictionary("key", 
                                                        [YamlDictionary("sub_key", 
                                                                        [YamlDictionary("sub_sub_key", "value")]
                                                                        )
                                                        ]
                                                        )
                                        ]
        
        content_translated: list = {"key": {"sub_key": {"sub_sub_key": "value"}}}
        
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate(content_to_translate)
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, content_translated)
        
    def test_empty_file(self):
        
        translator: ToYamlTranslator = ToYamlTranslator(self.file_path)
        translator.translate([])
        
        file_read_content: dict = {}
        with open(self.file_path, "r") as file_read:
            file_read_content = download_data(file_read,Loader)
            
        self.assertEqual(file_read_content, None)