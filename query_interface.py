

import streamlit as st
from datetime import datetime

class LogQueryInterface:
    def __init__(self, log_files):
        self.log_files = log_files
    
    def search_logs(self, filters):
        result_logs = []
        for log_file in self.log_files:
            with open(log_file, 'r') as file:
                logs = file.readlines()
                for log in logs:
                    try:
                        log_data = eval(log)  # Evaluate log string as Python dictionary
                        if self._apply_filters(log_data, filters):
                            result_logs.append(log_data)
                    except Exception as e:
                        st.error(f"Error parsing log in file {log_file}: {e}")
                        continue
        return result_logs
    
    def _apply_filters(self, log_data, filters):
        for key, value in filters.items():
            if key == "level" and log_data.get("level") != value:
                return False
            elif key == "log_string" and value not in log_data.get("log_string"):
                return False
            elif key == "timestamp":
                timestamp = datetime.strptime(log_data.get("timestamp"), "%Y-%m-%dT%H:%M:%SZ")
                if not value[0] <= timestamp <= value[1]:
                    return False
            elif key == "source" and log_data.get("metadata").get("source") != value:
                return False
        return True

# Initialize LogQueryInterface with log files
query_interface = LogQueryInterface([
    'log1.log', 'log2.log', 'log3.log', 'log4.log', 'log5.log', 
    'log6.log', 'log7.log', 'log8.log'
])

# Streamlit app
st.title('Log Query Interface')

search_query = st.text_input('Enter your search query:')
level_filter = st.selectbox('Select log level:', ['', 'INFO', 'ERROR', 'DEBUG', 'WARNING'])
start_date = st.date_input('Start date:')
end_date = st.date_input('End date:')

if st.button('Search'):
    filters = {}
    if search_query:
        filters['log_string'] = search_query
    if level_filter:
        filters['level'] = level_filter
    if start_date and end_date:
        filters['timestamp'] = [datetime.combine(start_date, datetime.min.time()), datetime.combine(end_date, datetime.max.time())]
    
    result_logs = query_interface.search_logs(filters)
    
    if result_logs:
        st.write('Matching logs:')
        for log in result_logs:
            st.json(log)
    else:
        st.write('No logs found for the given query.')


