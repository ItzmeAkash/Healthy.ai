from Healthyai.config.configuration import ConfigurationManager
from Healthyai.components.food_training import FoodTraining
from Healthyai import logger

# Model Training for the Food image classification
STAGE_NAME = "Food Classification Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config =ConfigurationManager()
        trainig_config = config.get_food_model_training_config()
        training = FoodTraining(config=trainig_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx============x")
    except Exception as e:
        raise e