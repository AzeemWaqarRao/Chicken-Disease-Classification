from CDC.config.configuration import ConfigurationManager
from CDC.components.training import Training
from CDC.components.callbacks import CallBacks
from CDC import logger
import os


stage_name = "Training Stage"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            callbacks_config = config.get_callbacks_config()
            callbacks = CallBacks(config=callbacks_config)
            callback_list = callbacks.get_tb_ckpt_callbacks()

            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(
                callback_list=callback_list
            )
            
        except Exception as e:
            raise e



if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)