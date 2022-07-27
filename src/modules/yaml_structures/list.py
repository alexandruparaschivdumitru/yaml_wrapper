from dataclasses import dataclass
from typing import Union, List

from src.modules.yaml_structures.dictionary import Dictionary

@dataclass
class YamlList:
    values: Union[List["Dictionary"], List["YamlList"]]