from .base import BaseCalculator

class BMRCalculator(BaseCalculator):
    def __init__(self, weight, height, age, gender):
        self.weight = self.validate_positive_number(weight, "Weight")
        self.height = self.validate_positive_number(height, "Height")
        self.age = self.validate_positive_number(age, "Age")
        self.gender = gender.lower()
    
    def calculate(self):
        """Oblicza BMR (Basal Metabolic Rate) - Mifflin-St Jeor Equation"""
        if self.gender == 'male':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.gender == 'female':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        else:
            raise ValidationError("Gender must be 'male' or 'female'")
        return round(bmr, 2)