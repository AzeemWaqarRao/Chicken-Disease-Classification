from CDC import logger
from CDC.pipeline.stage_01_data_ingestion import DataIngestionPipeline




if __name__ == "__main__":

    stage_name = "Data Ingestation Stage"
    
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)