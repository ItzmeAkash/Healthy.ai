from Healthyai.config.configuration import ConfigurationManager
from Healthyai.components.diet_recomd_model_trainer import DietModelTrainer
from Healthyai import logger
import warnings
warnings.filterwarnings('ignore')



STAGE_NAME = "Diet Recomendation Model Trainer Stage"


class DietRecomendationModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        
        config = ConfigurationManager()
        model_trainer_config = config.diet_recommend_model_trainer_config()
        model_trainer_config = DietModelTrainer(config = model_trainer_config)
        model_trainer_config.train()
        
              


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DietRecomendationModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx============x")
    except Exception as e:
        raise e
        

        
