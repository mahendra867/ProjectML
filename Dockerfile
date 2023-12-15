# these are docker commands which are very easy , so when we are performing the CICD deployment then by using the below commands  of docker it will convert our whole project modular code as docker image which we can deploy in cloud servers   
FROM python:3.8-slim-buster  

RUN apt update -y && apt install awscli -y  
WORKDIR /app  
COPY . /app
RUN pip install -r requirements.txt 

CMD ["python3", "app.py"] 