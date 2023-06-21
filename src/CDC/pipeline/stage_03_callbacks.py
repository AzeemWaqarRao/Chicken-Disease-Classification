from CDC.config.configuration import ConfigurationManager
from CDC.components.callbacks import CallBacks
from CDC import logger
import os


stage_name = "Callbacks Preparation Stage"

class CallbacksPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            configuration = ConfigurationManager()
            callbacks_config = configuration.get_callbacks_config()
            callbacks = CallBacks(callbacks_config)
            callbacks_list = callbacks.get_tb_ckpt_callbacks()
        except Exception as e:
            print(e)



if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = CallbacksPipeline()
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)