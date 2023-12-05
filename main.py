from Healthyai import logger
from Healthyai.pipeline.stage_01_diet_recomd_data_ingestion import DietRecomendationDataIngestionPipeline
from Healthyai.pipeline.stage_02_diet_recomd_data_validation import DietRecomendationDataValidatePipeline
from Healthyai.pipeline.stage_03_diet_recomd_model_trainer import DietRecomendationModelTrainingPipeline


STAGE_NAME = "Diet Recomendation Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<")
    obj = DietRecomendationDataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Diet Recomendation Data Validation Stage"

try: 
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<")
    obj = DietRecomendationDataValidatePipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx============x")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Diet Recomendation Model Trainer Stage"


try: 
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<")
    obj = DietRecomendationModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx============x")
    
except Exception as e:
    logger.exception(e)
    raise e
    
