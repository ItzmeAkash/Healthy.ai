from Healthyai import logger
from Healthyai.pipeline.stage_01_diet_recomd_data_ingestion import DietRecomendationDataIngestionPipeline


STAGE_NAME = "Diet Recomendation Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<")
    obj = DietRecomendationDataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e 