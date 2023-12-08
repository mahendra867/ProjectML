from src.PROJECTML import logger # although i have src folder when you click the explorar we can see that src but iam directly calling this mlproject_with_mlflow because i have initlizied my login functionality inside the __init__.py constructor thats why i dont need to call this src seperatly  you can call src folder by like this from src.mlproject_with_mlflow import logger , but if we want to ingore a folder like this to import that src folder , we can mention that inside the __init__.py constructor to ignore of calling the src folder 


logger.info('welcome to our custom logging1')