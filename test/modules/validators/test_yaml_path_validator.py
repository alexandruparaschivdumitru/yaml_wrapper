from unittest import TestCase

from src.modules.validators.yaml_object_path_validator import YamlObjectPathValidator

class TestYamlPathValidator(TestCase):
    def setUp(self) -> None:
        self.validator: YamlObjectPathValidator = YamlObjectPathValidator()
        
    def test_validator_valid_string(self):
        string_to_validate: str = "first_value.second_value"
        
        self.assertTrue(self.validator.validate(string_to_validate))
        
    def test_validator_not_valid_string(self):
        string_not_valid_to_validate: str = "first_value.second_value..third_value"
        
        self.assertFalse(self.validator.validate(string_not_valid_to_validate))
        
    def test_string_empty_string(self):
        string_empty: str = ""
        
        self.assertTrue(self.validator.validate(string_empty))
        
    def test_string_with_list(self):
        string_with_list: str = "first_value.[].second_value"
        
        self.assertTrue(self.validator.validate(string_with_list))
    
    def test_string_with_multiple_list(self):
        string_with_multiple_list: str = "first_value.[].[].second_value.[]"
        
        self.assertTrue(self.validator.validate(string_with_multiple_list))
    
    def test_string_with_wrong_list(self):
        string_with_wrong_list: str = "first_value.[].second_value.[wrong]"
        
        self.assertFalse(self.validator.validate(string_with_wrong_list))