from ctypes import Union

from src.modules.translators.to_yaml_translator import ToYamlTranslator


class Synchroniser:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._to_yaml_translator: ToYamlTranslator = ToYamlTranslator(file_path)
    
    def synchronise(self, content_to_synchronise: list) -> bool:
        pass