import os
import zipfile
import gdown
from Healthyai import logger
from Healthyai.utils.common import get_size
from Healthyai.entity.config_entity import DietRecommendDataIngestionConfig



# Diet Recommendation DataIngestion
class DataIngestion:
    def __init__(self, config: DietRecommendDataIngestionConfig):
        self.config = config
        
    # Downloading the file from google drive
        
    def download_data(self) -> str:
        """
        Fetch data from the url
        """
        
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/diet_recomendation/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            
            
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)
            
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
            
        except Exception as e:
            raise e
   # Extracting the downloaded file 
    
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
        
            
            