from src.PROJECTML import logger # although i have src folder when you click the explorar we can see that src but iam directly calling this mlproject_with_mlflow because i have initlizied my login functionality inside the __init__.py constructor thats why i dont need to call this src seperatly  you can call src folder by like this from src.mlproject_with_mlflow import logger , but if we want to ingore a folder like this to import that src folder , we can mention that inside the __init__.py constructor to ignore of calling the src folder 
from src.PROJECTML.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage" 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") # my data ingestion is started
    obj = DataIngestionTrainingPipeline() # here iam initilizing this DataIngestionTrainingPipeline()
    obj.main() # here iam calling this main
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x") # then iam telling that this data ingestion stage is successfully running completed 
except Exception as e:  # if there are any errors found this will get rise 
    logger.exception(e)
    raise e
