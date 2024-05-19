import streamlit as st
import logging
from datetime import datetime
from query_interface import LogQueryInterface

# Initialize LogQueryInterface with log files
query_interface = LogQueryInterface([
    'log1.log', 'log2.log', 'log3.log', 'log4.log', 'log5.log', 
    'log6.log', 'log7.log', 'log8.log'
])

# Streamlit app
st.title('Log Query Interface')

# User inputs
search_query = st.text_input('Enter your search query:')
level_filter = st.selectbox('Select log level:', ['', 'INFO', 'ERROR', 'DEBUG', 'WARNING'])
start_date = st.date_input('Start date:')
end_date = st.date_input('End date:')

# Button to trigger search
if st.button('Search'):
    filters = {}
    if search_query:
        filters['log_string'] = search_query
    if level_filter:
        filters['level'] = getattr(logging, level_filter)
    if start_date and end_date:
        filters['timestamp'] = [datetime.combine(start_date, datetime.min.time()), datetime.combine(end_date, datetime.max.time())]
    
    result_logs = query_interface.search_logs(filters)
    
    if result_logs:
        st.write('Matching logs:')
        for log in result_logs:
            st.json(log)
    else:
        st.write('No logs found for the given query.')
