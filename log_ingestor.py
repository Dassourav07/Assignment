import logging
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime

class LogIngestor:
    def __init__(self, log_file_path, log_level=logging.INFO):
        self.logger = logging.getLogger(log_file_path)
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
        self.logger.log(level, json.dumps(log_data))

# Example usage for writing logs into 8 files:
log_files = ['log1.log', 'log2.log', 'log3.log', 'log4.log', 'log5.log', 'log6.log', 'log7.log', 'log8.log']
log_messages = [
    "Inside the Search API", "User authentication successful", "Data processing started", 
    "Error connecting to database", "Service initialized", "Cache cleared", 
    "API response sent", "Shutdown signal received"
]

for log_file, message in zip(log_files, log_messages):
    log_ingestor = LogIngestor(log_file)
    log_ingestor.log_message(logging.INFO, message, log_file)



