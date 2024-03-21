from src.Chicken_disease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Chicken_disease import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()  # If this line raises an error, provide more specific error handling here.
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error occurred in stage {STAGE_NAME}: {str(e)}")
    raise e
