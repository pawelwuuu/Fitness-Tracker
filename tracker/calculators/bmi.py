from .base import BaseCalculator

class BMICalculator(BaseCalculator):
    def __init__(self, weight, height):
        self.weight = self.validate_positive_number(weight, "Weight")
        self.height = self.validate_positive_number(height, "Height")
    
    def calculate(self):
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2), 2)