from abc import ABC, abstractmethod
from django.core.exceptions import ValidationError

class BaseCalculator(ABC):
    @abstractmethod
    def calculate(self):
        pass
    
    def validate_positive_number(self, value, field_name):
        if value <= 0:
            raise ValidationError(f"{field_name} must be a positive number")
        return value