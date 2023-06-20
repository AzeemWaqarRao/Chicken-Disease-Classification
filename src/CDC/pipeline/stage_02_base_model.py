from CDC.config.configuration import ConfigurationManager
from CDC.components.base_model import BaseModel
from CDC import logger


stage_name = "Base Model Preparation Stage"

class BaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            configuration_manager = ConfigurationManager()
            configuration = configuration_manager.get_base_model_config()
            base_model = BaseModel(configuration)
            base_model.get_base_model()
            base_model.update_base_model()
        except Exception as e:
            print(e)



if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = BaseModelPipeline()
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)