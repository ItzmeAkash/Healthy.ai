from Healthyai.constants import *
from Healthyai.utils.common import read_yaml,create_directories
from Healthyai.entity.config_entity import DietRecommendDataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        
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
