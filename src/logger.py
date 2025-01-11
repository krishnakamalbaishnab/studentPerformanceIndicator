# Importing necessary modules for logging and working with date/time and file paths
import logging
import os
from datetime import datetime

# Generating a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating the logs directory path in the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Creating the logs directory if it does not already exist
os.makedirs(logs_path, exist_ok=True)

# Defining the complete path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging settings, including the log file path, format, and log level
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
