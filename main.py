import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = {'run_name': str, 'run_directory': str, 'run_notes': str, 'hours_till_finish': float, 'imaging_interval': float, 'imaging_time_lst': list}

set_up = st.Page("pages/set_up.py", title="Set up run", default=True)
timelapse = st.Page("pages/timelapse.py",  title="Timelapse")
view = st.Page("pages/viewer.py",  title="View")

pg = st.navigation([set_up, timelapse, view], position='hidden')

pg.run()
