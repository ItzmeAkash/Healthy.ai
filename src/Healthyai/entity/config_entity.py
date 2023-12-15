from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DietRecommendDataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir : Path
    
@dataclass(frozen=True)
class DietRecomenedDataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    
@dataclass(frozen=True)
class DietRecomdModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_name: str
    n_clusters: int
    target_column: float
    

@dataclass(frozen=True)
class FoodImageDataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass(frozen=True)
class FoodImagePreBaseModelCondfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
@dataclass(frozen=True)
class FoodTrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list
    
@dataclass(frozen=True)
class FoodEvaluationConfig:
    path_of_model : Path
    training_data : Path
    all_params : dict
    mlflow_uri : str
    params_image_size: list
    params_batch_size: int