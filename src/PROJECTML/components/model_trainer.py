# these packages i need in order to create my Model Trainer components 
import pandas as pd
import os
from PROJECTML import logger
from sklearn.linear_model import ElasticNet # here iam importing ElasticNet from sklearn
import joblib # here iam saving the model because i want to save the data 
from PROJECTML.entity.config_entity import ModelTrainerConfig



# now here iam defining a class called model trainer inside it will take ModelTrainerConfig
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    # here iam creating a methode which it will traine the model by using train and test dataset
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path) # here it is taking the paths of train and test dataset
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)  # here iam dropping my target column in train_x
        test_x = test_data.drop([self.config.target_column], axis=1)  # here iam dropping my target column in test_X
        train_y = train_data[[self.config.target_column]]  # here iam keeping the target column in train_y
        test_y = test_data[[self.config.target_column]]  # here iam keeping the target column in test_y


        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42) # here i have created my Elastic model which it takes the alpha,l1_ratio, random state values 
        lr.fit(train_x, train_y) # here i have initiated the model training

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name)) # here are training my model iam just saving inside the folder Model_trainer which it will get create inside the artifacts

