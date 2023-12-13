from Healthyai.constants import *
from Healthyai.utils.common import read_yaml,create_directories
from Healthyai.entity.config_entity import (DietRecommendDataIngestionConfig,
                                            DietRecomenedDataValidationConfig,
                                            DietRecomdModelTrainerConfig,
                                            FoodImageDataIngestionConfig,
                                            FoodImagePreBaseModelCondfig,
                                            FoodTrainingConfig)
import os
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
        
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        
        
        create_directories([self.config.artifacts])
        
        
    #Data Ingestion related configuration for Diet Recommendation
    
    def get_data_ingestion_config_diet_recommednation(self) -> DietRecommendDataIngestionConfig:
        config = self.config.diet_recommendation_data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config  = DietRecommendDataIngestionConfig(
            root_dir=config.root_dir,
            source_URL = config.source_URL,
            local_data_file  = config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    # Validateing the all columns are presented
    def get_data_validation_config_diet_recommednation(self) ->DietRecomenedDataValidationConfig:
        config = self.config.diet_recommendation_data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DietRecomenedDataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema = schema
        )
        return data_validation_config 
    
    # model training configuration for Diet Recomendation system
    def diet_recommend_model_trainer_config(self) -> DietRecomdModelTrainerConfig:
        config = self.config.diet_recommendation_model_trainer
        params = self.params.KMeans
        schema = self.schema.COLUMNS
        
        
        create_directories([config.root_dir])
        
        
        model_trainer_config = DietRecomdModelTrainerConfig(
            root_dir=config.root_dir,
            data_path = config.data_path,
            model_name= config.model_name,
            n_clusters=params.n_clusters,
            target_column=schema.Calories
        )
        return model_trainer_config
    
    # Data Ingestion for the Food Image Classiffication
    
    def get_food_data_ingestion(self) -> FoodImageDataIngestionConfig:
       config = self.config.food_image_data_ingestion
       
       create_directories([config.root_dir])
       
       food_image_data_ingestion_config = FoodImageDataIngestionConfig(
           root_dir = config.root_dir,
           source_URL = config.source_URL,
           local_data_file = config.local_data_file,
           unzip_dir = config.unzip_dir
           
       )
       return food_image_data_ingestion_config
   
   # Preparebase model for the food image classification
    def get_prepare_base_model_config(self) -> FoodImagePreBaseModelCondfig:
        config = self.config.food_image_prepare_base_model
        
        create_directories([config.root_dir])
        
        prepare_base_model_config = FoodImagePreBaseModelCondfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.params.VGG16.IMAGE_SIZE,
            params_learning_rate = self.params.VGG16.LEARNING_RATE,
            params_include_top = self.params.VGG16.INCLUDE_TOP,
            params_weights = self.params.VGG16.WEIGHTS,
            params_classes = self.params.VGG16.CLASSES 
        )
        return prepare_base_model_config
    def get_food_model_training_config(self) -> FoodTrainingConfig:
        training = self.config.food_image_model_training
        prepare_base_model = self.config.food_image_prepare_base_model
        params = self.params.VGG16
        training_data = os.path.join(self.config.food_image_data_ingestion.unzip_dir, "food classification")
        create_directories([Path(training.root_dir)])
        
        
        training_config = FoodTrainingConfig(
            root_dir= Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path = Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        return training_config