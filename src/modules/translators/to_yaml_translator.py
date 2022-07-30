from io import TextIOWrapper


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
    
