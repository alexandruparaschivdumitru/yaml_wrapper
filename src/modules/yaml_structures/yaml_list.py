from dataclasses import dataclass
from typing import Union, List

from src.modules.yaml_structures.yaml_dictionary import YamlDictionary

@dataclass
class YamlList:
    values: Union[List["YamlDictionary"], List["YamlList"]]