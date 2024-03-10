# End to End Wine Quality Prediction with MLops

## Problem Statement
Description:
This datasets is related to red variants of the Portuguese "Vinho Verde" wine.The dataset describes the amount of various chemicals present in wine and their effect on it's quality. The datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).Your task is to predict the quality of wine using the given data.

A simple yet challenging project, to anticipate the quality of wine.
The complexity arises due to the fact that the dataset has fewer samples, & is highly imbalanced.
Can you overcome these obstacles & build a good predictive model to classify them?

This data frame contains the following columns:

Input variables (based on physicochemical tests):\
1 - fixed acidity\
2 - volatile acidity\
3 - citric acid\
4 - residual sugar\
5 - chlorides\
6 - free sulfur dioxide\
7 - total sulfur dioxide\
8 - density\
9 - pH\
10 - sulphates\
11 - alcohol\
Output variable (based on sensory data):\
12 - quality (score between 0 and 10)


## Approach 


### Data Ingestion:

In the data ingestion stage, I, as the developer, first ensure that the necessary libraries are imported for component updates. The DataIngestion class is then defined to handle the ingestion process based on the provided configuration. Within this class, two main methods are implemented:

download_file: This method downloads the data from a specified URL using the urllib library and saves it locally. It checks if the file already exists and logs its size accordingly.

extract_zip_file: Here, the downloaded zip file is extracted into a designated directory using the zipfile library. This ensures that the data is ready for further processing.

### Data Validation:

In the data validation stage, I create the DataValidation component to ensure the integrity and completeness of the ingested data. The class DataValidation contains the following key method:

validate_all_columns: This method reads the unzipped data and compares its columns against a predefined schema. If all columns match the schema, it returns a validation status of True; otherwise, it returns False. The status is then written into a text file for reference.

### Data Transformation:

In this stage, I focus on transforming the data to make it suitable for modeling. The DataTransformation component, primarily featuring the train_test_spliting method, handles this process.

train_test_spliting: Using train_test_split from sklearn, the method splits the data into training and testing sets. It saves these splits as CSV files for future use.

### Model Training:

Moving forward, in the model training stage, I develop the ModelTrainer component to train a predictive model using the prepared data. The class ModelTrainer incorporates:

train: This method reads the training and testing data, separates the features and target variable, and initializes an ElasticNet model. The model is trained on the training data and saved using joblib.

### Model Evaluation:

Lastly, in the model evaluation stage, I assess the performance of the trained model. The ModelEvaluation component, with the method log_into_mlflow, handles this evaluation:

log_into_mlflow: Using mlflow, the method loads the test dataset and the trained model, makes predictions, and calculates evaluation metrics such as RMSE, MAE, and R2. These metrics are logged and saved, and the trained model is registered with mlflow for further tracking and deployment.


## WorkFlows

1. Update config.yam1
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the [main.py](http://main.py/)
9. Update the [app.py](http://app.py/)




# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/mahendra867/random_datasets/raw/main/winequality-data.zip
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/mahendra867/ProjectML_with_MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=mahendra867 \
MLFLOW_TRACKING_PASSWORD=85969b2c9b582440861229562a757d53c3cbb020 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/mahendra867/ProjectML_with_MLFlow.mlflow

export MLFLOW_TRACKING_USERNAME=mahendra867

export MLFLOW_TRACKING_PASSWORD=85969b2c9b582440861229562a757d53c3cbb020

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 683781347713.dkr.ecr.us-east-1.amazonaws.com/projml

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


