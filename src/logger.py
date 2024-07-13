import logging
import os
from datetime import datetime

file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok = True) 
logs_file_path = os.path.join(logs_path, file_name)

logging.basicConfig(filename = logs_file_path, level = logging.INFO, format = ' [%(asctime)s]  %(lineno)d  %(name)s - %(levelname)s - %(message)s ')


# Only for checking if its creating directory and logging in that file
# if __name__ == "__main__":
#     logging.info("Logging has started.")