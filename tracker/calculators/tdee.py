from .base import BaseCalculator

class TDEECalculator(BaseCalculator):
    ACTIVITY_LEVELS = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }
    
    def __init__(self, bmr, activity_level):
        self.bmr = self.validate_positive_number(bmr, "BMR")
        self.activity_level = activity_level.lower()
    
    def calculate(self):
        """Oblicza TDEE (Total Daily Energy Expenditure)"""
        if self.activity_level not in self.ACTIVITY_LEVELS:
            raise ValidationError(
                f"Invalid activity level. Choose from: {', '.join(self.ACTIVITY_LEVELS.keys())}"
            )
        
        multiplier = self.ACTIVITY_LEVELS[self.activity_level]
        return round(self.bmr * multiplier, 2)