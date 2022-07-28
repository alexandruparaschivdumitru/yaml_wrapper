from dataclasses import dataclass
from typing import Union, List

@dataclass
class YamlDictionary:
    key: str
    value: Union[int, str, "YamlDictionary", List["YamlDictionary"]]  