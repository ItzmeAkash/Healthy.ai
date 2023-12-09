from Healthyai.entity.config_entity import FoodImageDataIngestionConfig
import os
from Healthyai import logger
import gdown
import zipfile

# Food Image Classififcation Downloading and Extarcting the data from the google drive
class FoodDataIngestion:
    def __init__(self, config: FoodImageDataIngestionConfig):
        self.config = config
        
    
    def download_data(self) -> str:
        """
        Fetch data from the Url
        """
        try:
            dataset_url =  self.config.source_URL
            zip_download_dir  = self.config.local_data_file
            os.makedirs("artifacts/food_image_classification/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            
            
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)
            
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e
    
    def extract_zip_file(self):
        """
        Zip_file_path: str
        Extract the zip file into the data directory
        Function retruns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)