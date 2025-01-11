
# Importing the sys module to interact with the Python runtime environment

import sys
from src.logger import logging
# Function to extract detailed error information from an exception

def error_message_detail(error, error_detail: sys):
    # Extracting traceback details from the exception
    _, _, exc_tb = error_detail.exc_info()
    
    # Getting the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Formatting the error message with script name, line number, and error details
    error_message = "Error occurred in script name[{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message

# Custom exception class that provides detailed error messages
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Initialize the parent Exception class with a generic error message
        super().__init__(error_message)
        
        # Generate a detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        # Return the detailed error message when the exception is converted to a string
        return self.error_message
