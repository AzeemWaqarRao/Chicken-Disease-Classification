from CDC.config.configuration import ConfigurationManager
from CDC.components.model_evaluation import Evaluation
from CDC import logger
import os


stage_name = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            val_config = config.get_validation_config()
            evaluation = Evaluation(val_config)
            evaluation.evaluation()
            evaluation.save_score()
            

        except Exception as e:
            raise e



if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)