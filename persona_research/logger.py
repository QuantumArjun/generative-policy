

import logging
import os
import datetime
from glob import glob

def create_logger():
    class ExcludeGPTResultsFilter(logging.Filter):
        def filter(self, record):
            # Return False if the record contains 'GPT API result', True otherwise
            return 'GPT API result' not in record.getMessage()

    # Create a logger
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)  # Set minimum log level

    # Current date for the filename
    current_date = datetime.datetime.now().strftime("%Y%m%d")

    # List of existing log files for today
    existing_logs = glob(f'logs/{current_date}_*.log')

    # Determine the next run number
    run_number = len(existing_logs) + 1

    # Create a unique filename
    filename = f"logs/{current_date}_{run_number}.log"

    # Create a file handler instead of a console handler
    file_handler = logging.FileHandler(filename)  # Log messages will be saved to 'my_log.log'
    file_handler.setLevel(logging.DEBUG)

    # Create a stream handler for printing logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Apply the custom filter to both handlers
    file_handler.addFilter(ExcludeGPTResultsFilter())
    console_handler.addFilter(ExcludeGPTResultsFilter())

    # Set a format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Example log messages
    logger.debug('This is a regular debug message.')
    logger.info('This message contains GPT API result and should be excluded.')

    return logger