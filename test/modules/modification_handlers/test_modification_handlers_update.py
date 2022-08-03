from unittest import TestCase
from yaml import dump as upload_data # type: ignore
from yaml import Dumper

from src.modules.modification_handlers.modification_handler import ModificationHandler
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList
from src.utils.file.file_utils import FileUtil


class TestModificationHandlersUpdate(TestCase):
    def setUp(self) -> None:
        self.file_path = "tmp/test_modification_handlers_update.yaml"
        FileUtil.create_file_from_path(self.file_path)
        self.modification_handler: ModificationHandler  = ModificationHandler(self.file_path)
        
    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)
        
    def test_update(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": "value"}, file, Dumper)
        self.modification_handler.load()
        
        self.assertEqual(self.modification_handler.update("key", "value_1"), [YamlDictionary("key", "value_1")])
    
    def test_update_dict(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": "value"}, file, Dumper)
        self.modification_handler.load()
        
        self.assertEqual(self.modification_handler.update("key", "value_new"), [YamlDictionary("key", "value_new")])
    
    def test_update_dict_with_dict(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": {"host": "localhost",
                                 "port": 4545}},file, Dumper)
        self.modification_handler.load()
        
        self.assertEqual(self.modification_handler.update("key.port", 4546), [YamlDictionary("key", [YamlDictionary("host", "localhost"),
                                                                                                     YamlDictionary("port", 4546)])])
    def test_update_list(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": [[{"address_1": "address_value"}, {"label_1": "label_value"} , {"speed_1": "speed_value"}]]}, file, Dumper)
        self.modification_handler.load()
        
        self.assertEqual(self.modification_handler.update("key.[].address_1", "address_value_new"), [YamlDictionary("key", 
                                                                                                    YamlList([YamlDictionary("address_1", "address_value_new"),
                                                                                                              YamlDictionary("label_1", "address_value"),
                                                                                                              YamlDictionary("speed_1", "address_value"),
                                                                                                              ]))])
    def test_update_list_with_new_item(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": [[{"address_1": "address_value"}, {"label_1": "label_value"} , {"speed_1": "speed_value"}],
                                            ]},file ,  Dumper)
        self.modification_handler.load()
        
        self.assertEqual(self.modification_handler.update("key.[]", [
                                                                    YamlDictionary("address_1", "address_value_new"),
                                                                    YamlDictionary("label_1", "address_value"),
                                                                    YamlDictionary("speed_1", "address_value"),
                                                                    ]), 
                                                                    [YamlDictionary("key", 
                                                                                    YamlList(
                                                                                        [[YamlDictionary("address_2", "address_value_new"),
                                                                                        YamlDictionary("label_2", "address_value"),
                                                                                        YamlDictionary("speed_2", "address_value"),
                                                                                        ],
                                                                                        [YamlDictionary("address_1", "address_value_new"),
                                                                                        YamlDictionary("label_1", "address_value"),
                                                                                        YamlDictionary("speed_1", "address_value"),
                                                                                        ]]
                                                                                        )
                                                                                    )
                                                                    ]
                                                                )
    