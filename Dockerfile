# these are docker commands which are very easy , so when we are performing the CICD deployment then by using the below commands  of docker it will convert our whole project modular code as docker image which we can deploy in cloud servers   
FROM python:3.8-slim-buster # here iam taking 1 python image called 3.8-slim-buster 

RUN apt update -y && apt install awscli -y  # here iam doing the apt update , and i will install aws cli 
WORKDIR /app  # here i create one app directory inside i will copy all the code of the project 

COPY . /app
RUN pip install -r requirements.txt # here i will install all the requirements then 

CMD ["python3", "app.py"] # here it will launch our app.py