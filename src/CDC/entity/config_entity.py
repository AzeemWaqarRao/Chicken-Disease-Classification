from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    unzip_dir : Path
    local_data_file : Path



@dataclass(frozen=True)
class BaseModelConfig:
    root_dir : Path 
    base_model_path : Path
    updated_base_model_path : Path
    params_image_size : list
    params_learning_rate : float
    params_include_top : bool
    params_weights : str
    params_classes : int
    params_batch_size : int
    params_epochs : int

@dataclass(frozen=True)
class CallbacksConfig:
    root_dir : Path 
    tensorboard_root_log_dir : Path
    checkpoint_model_filepath : Path

    