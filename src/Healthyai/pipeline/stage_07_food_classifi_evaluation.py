from Healthyai import logger
from Healthyai.config.configuration import ConfigurationManager
from Healthyai.components.food_model_evaluation import FoodModelEvaluation
# Model Training for the Food image classification
STAGE_NAME = "Food Classification Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_food_evaludation_config()
        evaluation = FoodModelEvaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx============x")
    except Exception as e:
        raise e

