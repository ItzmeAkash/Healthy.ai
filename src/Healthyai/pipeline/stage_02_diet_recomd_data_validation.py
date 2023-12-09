from Healthyai.config.configuration import ConfigurationManager
from Healthyai.components.diet_recomd_data_validation import DataValidation
from Healthyai import logger

# Pipeline of the Data Validation for Diet Recommendaation 

STAGE_NAME = "Diet Recomendation Data Validation Stage"


class DietRecomendationDataValidatePipeline:
    def __init__(self):
        pass
    
    def main(self):
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config_diet_recommednation()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
            
            
            
            
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DietRecomendationDataValidatePipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx============x")
    except Exception as e:
        raise e
        

            
