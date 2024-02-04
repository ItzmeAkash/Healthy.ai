import os
import pandas as pd
import numpy as np
import joblib
from calories.calories import CalorieCalculator

# Path to the CSV file
file_path = '../../artifacts/diet_recomendation/data_ingestion/diet_recommendation.csv'

# Load the model
model_path = '../../artifacts/diet_recomendation/model_trainer/model.joblib'
model = joblib.load(model_path)

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Create the cluster
cluster = model.labels_

# Add Cluster to the DataFrame
df['cluster'] = cluster

obj = CalorieCalculator(gender='male', weight=50, height=115, physical_activity='very', goal='loss', age=24)

calories = obj.calculate()

print("Calories:", calories)


# Function for dividing Calories
def divide_calories(calories):
    breakfast = int(0.30 * calories)
    lunch = int(0.25 * calories)
    snacks = int(0.15 * calories)
    dinner = int(0.27 * calories)
    return breakfast, lunch, snacks, dinner


# Function for Recommending each meal
def diet_recomend(calories):
    breakfast, lunch, snacks, dinner = divide_calories(calories=calories)

    # Prediction Breakfast
    breakfast_cluster = model.predict(np.array([breakfast]).reshape(-1,1)).flatten() 
    breakfast_food = df.loc[(df['Breakfast'] == 1) & (df['cluster'] == breakfast_cluster[0]), ['food_items', 'Calories']].sort_values(by='Calories').head()
    lunch_cluster = model.predict(np.array([lunch]).reshape(-1,1)).flatten()
    luch_food = df.loc[(df['Lunch'] == 1) & (df['cluster'] == lunch_cluster[0]), ['food_items', 'Calories']].sort_values(by='Calories').head()

    return luch_food



print(diet_recomend(calories=calories))

