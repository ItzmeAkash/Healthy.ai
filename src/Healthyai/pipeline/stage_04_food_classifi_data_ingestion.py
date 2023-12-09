from Healthyai import logger
from Healthyai.config.configuration import ConfigurationManager
from Healthyai.components.food_data_ingestion import FoodDataIngestion


# Pipeline for the Food image classification
STAGE_NAME = "Food Classification Data Ingestion"

class FoodDataIngeestionPipeLine:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        food_image_data_ingestion = config.get_food_data_ingestion()
        food_image_data_ingestion = FoodDataIngestion(config=food_image_data_ingestion)
        food_image_data_ingestion.download_data()
        food_image_data_ingestion.extract_zip_file()




if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = FoodDataIngeestionPipeLine()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx============x")
    except Exception as e:
        raise e
    
        
        
                