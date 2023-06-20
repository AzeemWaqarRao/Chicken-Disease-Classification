from CDC.config.configuration import ConfigurationManager
from CDC.components.data_ingestion import DataIngestion
from CDC import logger

stage_name = "Data Ingestation Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            configuration_manager = ConfigurationManager()
            configuration = configuration_manager.get_data_ingestion_config()
            data_ingestion = DataIngestion(configuration)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            print(e)



if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<<< STAGE: {stage_name} started >>>>>>>>>>>")
        obj = DataIngestionPipeline
        obj.main()
        logger.info(f"<<<<<<<<< STAGE: {stage_name} completed >>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)