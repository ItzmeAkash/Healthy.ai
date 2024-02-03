import os
import pandas as pd
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
