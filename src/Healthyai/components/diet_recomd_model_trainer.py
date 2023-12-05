import pandas as pd
import numpy as np
from Healthyai.entity.config_entity import DietRecomdModelTrainerConfig
import os
from sklearn.cluster import KMeans
import joblib


class DietModelTrainer:
    def __init__(self, config: DietRecomdModelTrainerConfig):
        self.config = config
        
    def train(self):
        data = pd.read_csv(self.config.data_path, index_col=0)
        # print(data.head())
        # print(data['Calories'])
        train_data = data["Calories"]
        
        kmeans = KMeans(n_clusters=self.config.n_clusters, random_state= 42)
        kmeans.fit(np.array(train_data).reshape(-1,1))
        
        joblib.dump(kmeans,os.path.join(self.config.root_dir, self.config.model_name))
        
        