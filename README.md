# Assignment





part 1: 




This Python code defines a LogIngestor class responsible for logging messages to multiple log files with rotation. Let's break down the code step by step:
Imports:


logging: This module provides a flexible framework for emitting log messages from Python programs.
RotatingFileHandler: This handler is used to handle log file rotation, ensuring that log files don't grow indefinitely.
json: This module is used for working with JSON data.
datetime: This module is used to work with dates and times.



LogIngestor class:

log_message method: This method is used to log a message with a specified log level, log string, and source. It generates a timestamp and constructs a dictionary containing log data, including level, log string, timestamp, and source. Then it logs this data using the logger.




Example usage:

Several instances of LogIngestor are created, each initialized with a different log file path ('log1.log', 'log2.log', ..., 'log8.log'). Then, a log message is logged for each instance with a log level of logging.INFO, a log string of "Inside the Search API", and the respective log file name as the source.


This code is useful for logging messages to multiple log files with rotation, which can be helpful for managing logs in a larger application or system. It demonstrates how to use Python's built-in logging module effectively to handle logging tasks.








PART-2-------> 

This code defines a class LogQueryInterface that provides methods to search through log files based on certain filters. Let's break down the code and its functionality:


Import Statement:

The code imports the datetime module to work with timestamps.
Class


Class Definition:

It iterates over each log file in self.log_files.

For each log file, it opens the file and reads its content line by line.

Each line is treated as a log and is evaluated as a Python dictionary using eval.

It then checks if the log matches the provided filters using the _apply_filters method.

If a log matches the filters, its appended to result_logs.

If theres an exception during the evaluation of a log (likely due to malformed log lines), it prints an error message and continues to the next log.



_apply_filters Method:



It takes a log data dictionary and a set of filters.

It iterates over each filter and checks if the log data matches the filter criteria.

Filters can be based on "level", "log_string", "timestamp", or "source".

If any filter doesnt match, it returns False. Otherwise, it returns True.



