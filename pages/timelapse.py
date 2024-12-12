import streamlit as st
import pandas as pd
import numpy as np
import time
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

run_name = st.session_state.user_input['run_name']
run_notes = st.session_state.user_input['run_notes']
hrs_till_finish = st.session_state.user_input['hours_till_finish']
imaging_interval = st.session_state.user_input['imaging_interval'] 
imaging_time_lst = st.session_state.user_input['imaging_time_lst']
run_directory = st.session_state.user_input['run_directory']

timelapse_running = st.session_state['timelapse_running']
timelapse_running = True

# sidebar
with st.sidebar:
    st.subheader(":material/description: Set up time lapse", divider="green")
    st.subheader(":material/videocam: Image", divider="orange")
    st.subheader(":material/movie: View", divider="grey")

if run_name == "":

    @st.dialog("Run error")
    def run_input_error():
        st.text(f"Either there's an error with the input data by the user, or the page was refreshed.")
        st.page_link("pages/set_up.py", label="Set up run", icon=":material/description:")
    
    run_input_error()

Path(f"{run_directory}/{run_name}/images").mkdir(parents=True, exist_ok=True)

# layout
st.title('Timelapse')

message_area = st.empty()
with message_area:
    st.warning('Timelapse in progress', icon="⚠️")

st.divider()

time_lapse_errors = [] 
proceed_to_viewer = False

col1, col2 = st.columns([1,2])

with col1:
    my_bar = st.progress(0, text="Imaging progress")
    last_taken_container = st.empty()
    hrs_to_go_container = st.empty()
    st.divider()
    cancel_button_area = st.empty()
    st.button("Cancel timelapse", icon=":material/close:", disabled = not timelapse_running)
    viewer_page_area = st.empty()
with col2:
    preview_image = st.empty()

with viewer_page_area:
    st.page_link("pages/viewer.py", label="View timelapse", icon=":material/movie:", disabled=True)

for hr_time in imaging_time_lst:
    current_time = datetime.now().strftime('%H:%M:%S')
    upcoming_time = (datetime.now() + timedelta(hours=imaging_interval)).strftime('%H:%M:%S')

    my_bar.progress(hr_time/hrs_till_finish, text="Progress")
    with last_taken_container:
        st.metric(
            label="Image last taken at",
            value=f'{current_time}',
            delta_color="off"
        )
    with hrs_to_go_container:
        st.metric(
            label="Image next taken at",
            value=f'{upcoming_time}'
        )

    with open(f'{run_directory}/{run_name}/images/{run_name}_{hr_time}hrs.txt', 'w') as f:
        f.write(f"Image created at {hr_time} hrs for run_name.")

    preview_image_i = Image.open("bacteria.jpeg")

    with preview_image:
        preview_image = st.image(preview_image_i, use_container_width=True,caption=f"Previous image for {run_name}.")

    time.sleep(imaging_interval*60**2)

time.sleep(1)

currentDateAndTime = datetime.now()

preview_image_i = Image.open("bacteria.jpeg")

with preview_image:
    preview_image = st.image(preview_image_i, use_container_width=True, caption=f"Previous image for {run_name}.")

current_time = datetime.now().strftime('%H:%M:%S')
upcoming_time = (datetime.now() + timedelta(hours=imaging_interval)).strftime('%H:%M:%S')
my_bar.empty()
with my_bar:
        st.metric(
            label="Progress",
            value=f'Done'
        )
with last_taken_container:
        st.metric(
            label="Image last taken at",
            value=f'{current_time}',
            delta_color="off"
        )
with hrs_to_go_container:
    st.metric(
        label="Image next taken at",
        value=f'N/A'
    )

message_area.empty()
with message_area:
    st.warning('Proccessing in progress', icon="⚠️")
    
time.sleep(5)

timelapse_running = False

message_area.empty()
with message_area:
    st.success('Timelapse done and video created')

with viewer_page_area:
    st.page_link("pages/viewer.py", label="View timelapse", icon=":material/movie:", disabled=False)


