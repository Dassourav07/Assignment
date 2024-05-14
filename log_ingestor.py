import logging
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime

class LogIngestor:
    def __init__(self, log_file_path, log_level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        
        formatter = logging.Formatter('%(message)s')
        
        file_handler = RotatingFileHandler(log_file_path, maxBytes=10*1024*1024, backupCount=5)
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)

    
    def log_message(self, level, log_string, source):
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        log_data = {
            "level": level,
            "log_string": log_string,
            "timestamp": timestamp,
            "metadata": {
                "source": source
            }
        }
        self.logger.log(level, log_data)

# Example usage:
log_ingestor = LogIngestor('log1.log')
log_ingestor.log_message(logging.INFO, "Inside the Search API", "log1.log")                          



log_ingestor = LogIngestor('log2.log')
log_ingestor.log_message(logging.INFO, "Inside the Search API", "log2.log")    

log_ingestor = LogIngestor('log3.log')
log_ingestor.log_message(logging.INFO, "Inside the Search API", "log3.log")                          


log_ingestor = LogIngestor('log4.log')
log_ingestor.log_message(logging.INFO, "Inside the Search API", "log4.log")                          


log_ingestor = LogIngestor('log5.log')
log_ingestor.log_message(logging.INFO, "Inside the Search API", "log5.log")                          

log_ingestor = LogIngestor('log6.log')
log_ingestor.log_message(logging.INFO, "Inside the Search API", "log6.log")                          

log_ingestor = LogIngestor('log7.log')
log_ingestor.log_message(logging.INFO, "Inside the Search API", "log7.log")                          


log_ingestor = LogIngestor('log8.log')
log_ingestor.log_message(logging.INFO, "Inside the Search API", "log8.log")                          
