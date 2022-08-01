from src.modules.translators.from_yaml_traslator import FromYamlTraslator


class Initialiser:
    def __init__(self, file_path: str, from_yaml_traslator: FromYamlTraslator) -> None:
        self._file_path: str = file_path
    
    def initialise(self) -> list:
        pass