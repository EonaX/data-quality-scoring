#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:06:59 2024

@author: maximeb
"""
from main import cwd, apidae_schemas, apidae_data
from data.analysis import *
from data.load import open_data
from visualize import *
import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 1000px;
}
</style>
""",
    unsafe_allow_html=True,
)

st.title('Data Quality App')

st.header("Load Data and Schema Files")

# Upload area

file_location = st.radio("Upload data and schema from:", ['this server', 'your local computer'])

# Choice between local or server files uploading

if file_location == 'your local computer':
    
    # Choice 1
    
    col1, col2 = st.columns(2)
    with col1:
        apidae_data = st.file_uploader(label='dataset')
    with col2:
        apidae_schemas = st.file_uploader(label='schemas')
    
elif file_location == 'this server':
    
    # Choice 2
    
    # if st.button('Load files'):
        apidae_data = open_data(path='data/datasets/vaut_le_detour.json')
        apidae_schemas = open_data(path='data/schemas/apiObjetsTouristiquesResultat.schema')


st.header("Data Quality Dashboard")

# Report area

if apidae_data and apidae_schemas:
    
    if file_location == 'your local computer':
        apidae_data = open_data(streamlit_uploaded_file=apidae_data)
        apidae_schemas = open_data(streamlit_uploaded_file=apidae_schemas)
    
    # Calculation
    
    intersection_properties = get_intersection_properties(apidae_schemas)
    completeness_percent = get_completeness_percent(apidae_data, intersection_properties)
    total_score = get_total_score(completeness_percent)
    
    # Display
    
    completeness_bar = plot_completeness_bar(completeness_percent, title = 'Data Completeness Bar Graph')
    total_score_gauge = plot_total_score_gauge(total_score)
    
    col1, col2 = st.columns([5,2])
    with col1:
        
        # Plot
        
        st.plotly_chart(completeness_bar, use_container_width=True, theme='streamlit')
    
    with col2:
        
        # KPI/Score
        
        st.plotly_chart(total_score_gauge, use_container_width=True, theme='streamlit')
else:
    
    # Other instructions
    
    st.write('Upload data and schema first.')