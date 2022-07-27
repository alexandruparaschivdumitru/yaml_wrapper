from dataclasses import dataclass
from typing import Union, List

@dataclass
class Dictionary:
    key: str
    value: Union[str, "Dictionary", List["Dictionary"]]  