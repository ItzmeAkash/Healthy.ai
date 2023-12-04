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
    