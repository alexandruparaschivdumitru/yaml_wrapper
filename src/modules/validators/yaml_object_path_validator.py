from typing import Any, List
from typing import Callable

from src.modules.validators.abstracts.validator import Validator

class YamlObjectPathValidator(Validator):
    def __init__(self) -> None:
       pass
   
    def validate(self, value: str) -> bool:
        values_splitted: List[str] = value.split(".")
        if len(values_splitted) > 1 and values_splitted[0] != "":
            for value_splitted in values_splitted:
                if  (len(value_splitted) == 0) or (value_splitted[0] == "[" and value_splitted[-1] == "]" and len(value_splitted) > 2): 
                        return False
                
        return True