from abc import ABCMeta, abstractmethod
from typing import Any
from typing import Callable

class Validator(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'validate') and 
                callable(subclass.validate) or 
                NotImplemented)
    
    @abstractmethod
    def validate(self, function: Callable[[Any], bool]) -> bool:
        pass