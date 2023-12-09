# This is called the entity 
from dataclasses import dataclass # here i imported the dataclass from the dataclasses
from pathlib import Path  # here i imported path from pathlib

# here entity means DataIngestionConfig which it returns all the variables like root_dir,source_URL  and etc 
@dataclass(frozen=True) # here i declared the dataclass decorator
class DataIngestionConfig:  # here i have created a class and named as DataIngestionConfig ,and it is not a python class because we need to declare the self to the variables if it is a python class, it is data class  and whenever i define the configuration fucntion , this class should my return function , the below are the varaible it do return 
    root_dir: Path    # these are variable which i have declared inside the class 
    source_URL: str
    local_data_file: Path
    unzip_dir: Path