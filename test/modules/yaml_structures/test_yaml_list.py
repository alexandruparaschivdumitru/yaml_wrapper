from typing import List
from unittest import TestCase

from src.modules.yaml_structures.yaml_dictionary import YamlDictionary
from src.modules.yaml_structures.yaml_list import YamlList

class TestYamlList(TestCase):
    def test_yaml_list(self):
        data_1: YamlDictionary = YamlDictionary("label", "Chinese_GPS")
        data_2: YamlDictionary = YamlDictionary("speed", "9600")
        data_3: YamlDictionary = YamlDictionary("address", "/dev/ttyACM0")
        data_4: YamlDictionary = YamlDictionary("label", "Kendau_GPS")
        data_5: YamlDictionary = YamlDictionary("speed", "9600")
        data_6: YamlDictionary = YamlDictionary("address", "/dev/ttyUSB0")
        list_1: YamlList = YamlList([data_1, data_2, data_3])
        list_2: YamlList = YamlList([data_4, data_5, data_6])
        
        data: YamlDictionary = YamlDictionary("serials", [list_1, list_2])
        
        self.assertIsInstance(data.value, list)
        
        
    def test_yaml_list_contain_lists(self):
        data_1: YamlDictionary = YamlDictionary("label", "Chinese_GPS")
        data_2: YamlDictionary = YamlDictionary("speed", "9600")
        data_3: YamlDictionary = YamlDictionary("address", "/dev/ttyACM0")
        data_4: YamlDictionary = YamlDictionary("label", "Kendau_GPS")
        data_5: YamlDictionary = YamlDictionary("speed", "9600")
        data_6: YamlDictionary = YamlDictionary("address", "/dev/ttyUSB0")
        list_1: YamlList = YamlList([data_1, data_2, data_3])
        list_2: YamlList = YamlList([data_4, data_5, data_6])
        
        data: YamlDictionary = YamlDictionary("serials", [list_1, list_2])
        
        self.assertIsInstance(data.value[0].values, list)   
    
# Data structures tested:
# serials:
#   - label    : Chinese_GPS
#     speed    : 9600
#     address  : "/dev/ttyACM0"

#  - label   : Kendau_GPS
#    speed   : 9600
#    address : /dev/ttyUSB0
# Converted in ADT
# ------------------------------
# data = {
#     key: serials
#     value : [
#         [{label: speed},{speed: 9600},{assdress: "h,mfhd"}],
#         [{label: speed},{speed: 9600},{assdress: "h,mfhd"}]
#     ]
# }