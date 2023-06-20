from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    unzip_dir : Path
    local_data_file : Path
