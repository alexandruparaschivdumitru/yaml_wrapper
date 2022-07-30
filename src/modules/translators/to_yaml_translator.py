from io import TextIOWrapper
from yaml import dump as upload_data # type: ignore
from yaml import Dumper
from yaml import YAMLError

from src.modules.translators.exceptions.writing_yaml_exception import WritingYamlException


class ToYamlTranslator:
    """Translator from the format of Yaml wrapper, to the format of yaml library.
    """
    def __init__(self , file: TextIOWrapper) -> None:
        self._file: TextIOWrapper = file
        
    def __del__(self):
        self._file.close()
        
        
    def translate(self, content_to_translate: list) -> dict:
        """Translates the content of the YamlWrapper to the format of yaml library.

        Returns:
            dict: Content translated in the format accepted by yaml library.
        """
        pass
    
    def _write_to_file(self, content_to_write: dict) -> None:
        try:
            upload_data(content_to_write, self._file, Dumper)
        except YAMLError:
            raise WritingYamlException("Error writing the content to the yaml file.")
    
    