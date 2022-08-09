from unittest import TestCase
from yaml import dump as upload_data  # type: ignore
from yaml import Dumper
from src.modules.modification_handlers.exceptions.filter_not_found_exception import FilterNotFoundException
from src.modules.modification_handlers.exceptions.not_valid_filter_exception import NotValidFilterException
from src.modules.modification_handlers.exceptions.not_valid_remove_exception import NotValidRemoveException

from src.modules.modification_handlers.modification_handler import ModificationHandler
from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList
from src.utils.file.file_utils import FileUtil


class TestModificationHandlersRemove(TestCase):
    def setUp(self) -> None:
        self.file_path = "tmp/test_modification_handlers_remove.yaml"
        FileUtil.create_file_from_path(self.file_path)
        self.modification_handler: ModificationHandler = ModificationHandler(
            self.file_path)

    def tearDown(self) -> None:
        FileUtil.delete_file(self.file_path)

    def test_remove(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": "value"}, file, Dumper)
        self.modification_handler.load()

        self.assertEqual(self.modification_handler.remove("key"), [])

    def test_not_valid_remove(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": [[{"address_1": "address_value"}, {"label_1": "label_value"}, {"speed_1": "speed_value"}],
                                 [{"address_2": "address_value"}, {"label_2": "label_value"}, {"speed_2": "speed_value"}]]}, file, Dumper)
        self.modification_handler.load()

        with self.assertRaises(NotValidRemoveException):
            self.modification_handler.remove("key.[].address_2"),

    def test_remove_item_from_list(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": {"sub_key": [1, 2, 3],
                                "second_sub_key": [1, 2, 3]
                                }
                        }, file, Dumper)

        self.modification_handler.load()

        self.assertEqual(self.modification_handler.remove("key.sub_key"), [YamlDictionary("key",
                                                                                          [
                                                                                              YamlDictionary("second_sub_key", YamlList([1, 2, 3]))])])

    def test_remove_dict(self) -> None:
        with open(self.file_path, "w") as file:
            upload_data({"key": "value"}, file, Dumper)
        self.modification_handler.load()

        self.assertEqual(self.modification_handler.remove("key"), [])

    def test_remore_key_not_existent(self):
        with open(self.file_path, "w") as file:
            upload_data({"key": {"address_1": "address_value", "addres_2": "address_2_value"}}, 
                        file, 
                        Dumper)

        self.modification_handler.load()

        with self.assertRaises(FilterNotFoundException):
            self.modification_handler.remove("key_not_valid")
