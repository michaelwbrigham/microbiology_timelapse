import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

with st.sidebar:
    st.subheader(":material/description:Set up time lapse", divider="orange")
    st.subheader(":material/videocam:  Image", divider="grey")
    st.subheader(":material/movie:  View", divider="grey")

st.title("Set up time lapse")
st.session_state.user_input['run_name'] = st.text_input("Run name", value='Default')
run_name = st.session_state.user_input['run_name']
st.session_state.user_input['run_directory'] = st.text_input("Directory", value="/home/mbrigham/Desktop/streamlit")
run_directory = st.session_state.user_input['run_directory']

with st.expander("Add notes"):
    st.session_state.user_input['run_notes']  = st.text_area("Notes", value="")
    run_notes = st.session_state.user_input['run_notes']

st.divider()

timing_col1, timing_col2 = st.columns([1, 1])

st.session_state.user_input['hours_till_finish'] = timing_col1.number_input("Time till finish (hrs)", min_value=0.001, value=0.005, step=0.001, format="%0.3f")
hrs_till_finish = st.session_state.user_input['hours_till_finish']
st.session_state.user_input['imaging_interval'] = timing_col2.number_input("Imaging interval (hrs)", min_value=0.001, value=0.001, step=0.001,format="%0.3f")
imaging_interval = st.session_state.user_input['imaging_interval'] 

st.session_state.user_input['imaging_time_lst'] = list(np.arange(0, hrs_till_finish+imaging_interval, imaging_interval))
imaging_time_lst = st.session_state.user_input['imaging_time_lst']

st.write(f"{run_name} will finish in {round(hrs_till_finish, 3)} hrs and take an image every {round(imaging_interval, 3)} hrs ({len(imaging_time_lst)} images).")

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=imaging_time_lst,
    y=np.zeros(len(imaging_time_lst)),
    mode="lines+markers+text",
    text=[f"{t} hrs" for t in imaging_time_lst],
    textposition="top center",
    marker=dict(size=12,line_color="midnightblue",color="lightskyblue")
))
fig.update_layout(
    height=100,
    showlegend=False,
    margin=dict(l=20, r=20, t=0, b=0),
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

timelapse_page_link_col1, timelapse_page_link_col2, timelapse_page_link_col3 = st.columns([1, 1, 1])

@st.dialog("Check image before run", width="large")
def check_camera():
    st.camera_input("Check image before run", label_visibility="collapsed")

if timelapse_page_link_col1.button("Check image before run"):
    check_camera()

timelapse_page_link_col3.page_link("pages/timelapse.py", label="Start time lapse", icon=":material/videocam:", disabled=False)