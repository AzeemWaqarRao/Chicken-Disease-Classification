from CDC.constants import *
from CDC.utils.helper_functions import read_yaml, create_directories
from CDC.entity.config_entity import DataIngestionConfig, BaseModelConfig

from box import ConfigBox

class ConfigurationManager:
    def __init__(
        self,
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> ConfigBox:
        config = self.config.data_ingestion
        create_directories([config.root_dir])    

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            unzip_dir = config.unzip_dir,
            local_data_file = config.local_data_file,
            source_url = config.source_URL
        )

        return data_ingestion_config
    
    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.base_model
        create_directories([config.root_dir])
        base_model_config = BaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.params.INPUT_SHAPE,
            params_batch_size = self.params.BATCH_SIZE,
            params_epochs = self.params.EPOCHS,
            params_learning_rate = self.params.LEARNING_RATE,
            params_classes = self.params.CLASSES,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS
        )
        
        return base_model_config
