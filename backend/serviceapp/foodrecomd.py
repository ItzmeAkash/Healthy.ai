
#Diet Recommendation
class FoodRecommendation:
    PHYSICAL_ACTIVITY_FACTORS = {
        "Sedentray": 1.2,
        "LightlyActive": 1.375,
        "ModeratelyActive": 1.725,
        "ExtremelyActive": 1.9
    }

    def __init__(self, age, gender, weight, height, physical_activity, goal):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.physical_activity = physical_activity
        self.goal = goal
        
    # Calculateing calories
    def calories(self):
        factor = self.PHYSICAL_ACTIVITY_FACTORS.get(self.physical_activity, 1.2)

        bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + (5 if self.gender == 'Male' else -161)
        calories = round(bmr * factor)
        
        # Conditions for maintain loss, gain, mainatin weight
        adjustment = 500 if self.goal == 'gain' else (-500 if self.goal == 'loss' else 0)
        calories += adjustment
        
        # return the calories for each meals
        meal_portions = {
            'breakfast': int(0.30 * calories),
            'lunch': int(0.25 * calories),
            'snacks': int(0.15 * calories),
            'dinner': int(0.27 * calories)
        }

        return meal_portions


obj = FoodRecommendation(25, "Male", 55, 150, "Sedentray", "loss")
meal_portions = obj.calories()
print(meal_portions)
