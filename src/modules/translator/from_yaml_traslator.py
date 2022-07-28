from io import TextIOWrapper
import yaml # type: ignore


class FromYamlTraslator:
    def __init__(self , file: TextIOWrapper) -> None:
        self._file: TextIOWrapper = file
        
    def translate(self)-> dict:
        """Returns a dict in the right format for YamlWrapper, with the content of yaml file

        Returns:
            dict: Yaml file content in right format
        """
        return {}
    
    def _convert(self, data_to_convert: dict) -> dict:
        return {}
        