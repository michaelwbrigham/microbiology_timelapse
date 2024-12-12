import streamlit as st
import pandas as pd
import numpy as np


with st.sidebar:
    st.subheader(":material/description:  Set up time lapse", divider="green")
    st.subheader(":material/videocam:  Image", divider="green")
    st.subheader(":material/movie:  View", divider="blue")

run_name = st.session_state.user_input['run_name']

st.title("View timelapse")
st.subheader(run_name)
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
