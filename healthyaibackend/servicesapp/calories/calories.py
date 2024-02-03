class CalorieCalculator:
    def __init__(self, age, weight, height, gender, physical_activity, goal):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.physical_activity = physical_activity
        self.goal = goal
        
    def calculate(self):
        activity_factors = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderately": 1.55,
            "very": 1.725,
            "extreme": 1.9
        }
        
        if self.physical_activity in activity_factors:
            factor_value = activity_factors[self.physical_activity]
        else:
            factor_value = 1  # Default value if physical activity level is not recognized
        
        if self.gender == "male":
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.gender == "female":
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        else:
            raise ValueError("Invalid gender specified")
        
        calories = round(bmr * factor_value)
        
        return calories
