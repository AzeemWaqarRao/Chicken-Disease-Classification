from CDC import logger
from CDC.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from CDC.pipeline.stage_02_base_model import BaseModelPipeline
from CDC.pipeline.stage_03_callbacks import CallbacksPipeline
import os




if __name__ == "__main__":

    stage_name = "Data Ingestation Stage"
    
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)

    stage = "Base Model Preparation Stage"
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = BaseModelPipeline()
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)

    stage_name = "Callbacks Preparation Stage"
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = CallbacksPipeline()
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)