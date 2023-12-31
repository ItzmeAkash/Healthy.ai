from Healthyai.config.configuration import ConfigurationManager
from Healthyai.components.diet_recomd_data_ingestion import DataIngestion
from Healthyai import logger

# Pipeline of the Data Ingestion for Diet Recommendaation 

STAGE_NAME = "Diet Recomendation Data Ingestion Stage"


# Diet Recommendation Data Ingestion Pipeline

class DietRecomendationDataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config_diet_recommednation()
        data_ingestion =DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()
        



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DietRecomendationDataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e    
        