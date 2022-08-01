from typing import Any
from typing import Callable

from src.modules.validators.abstracts.validator import Validator

class YamlObjectPathValidator(Validator):
    def __init__(self) -> None:
       pass
   
    def validate(self, function: Callable[[Any], bool]) -> bool:
        pass