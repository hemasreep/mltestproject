import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.exception import CustomException
from src.logger import logger
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig():
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path:  str=os.path.join('artifacts','test.csv')
    raw_datha_path:  str=os.path.join('artifacts','data.csv')
    

class DataIngestion():
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def dataIngestionInitiate(self):
        logger.info("enteretd into data ingestion component")
        
        try:
            df=pd.read_csv('notebook\stud.csv')
            logger.info("data readed into daatframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_datha_path,index=False,header=True)
            logger.info("train test split initiated")
            
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logger.info("train and test spilt done")
            
            return(
                self.ingestion_config.test_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    
    obj=DataIngestion()
    train_data,test_data=obj.dataIngestionInitiate()
    data_transformation=DataTransformation()
    data_transformation.initiate_data_trasnforamtion(train_data,test_data)
    
    
    
        
        
            