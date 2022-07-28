from typing import List
from unittest import TestCase

from src.modules.yaml_structures.yaml_dictionary import YamlDictionary

class TestYamlDictionary(TestCase):
    def test_name(self):
        data: YamlDictionary = YamlDictionary("name", "value")
        self.assertEqual(data.key, "name")
        
    def test_value(self):
        data: YamlDictionary = YamlDictionary("name", "value")
        self.assertEqual(data.value, "value")
    
    def test_value_type_str(self):
        data: YamlDictionary = YamlDictionary("name", "value")
        self.assertIsInstance(data.value, str)
        
    def test_value_type_yaml_dictionary(self):
        data_1: YamlDictionary = YamlDictionary("name", "value")
        data: YamlDictionary = YamlDictionary("name", data_1)
        self.assertIsInstance(data.value, YamlDictionary)
    
    def test_value_type_yaml_list(self):
        data_1: YamlDictionary = YamlDictionary("name", "value")
        data_2: YamlDictionary = YamlDictionary("name_2", "value_2")
        list_data: List[YamlDictionary] = [data_1, data_2]
        data: YamlDictionary = YamlDictionary("name", list_data)
        self.assertIsInstance(data.value, list)

  
    
# Data structures tested:
# ==============================
# name: value
# ------------------------------
# Converted in ADT:
# data = {key : "name",
#         value: "value"}


# ==============================
# server:
#   host: "localhost"
#   port: 4545
# ------------------------------
# Conveted in ADT:
# data = {key: server,
#         value:[
#             {host: localhost},
#             {port: 4545}
#         ]}
