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

st.title('Data Quality App')

st.header("Load Data and Schema")

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
    
    if st.button('Load files'):
        apidae_data = open_data(path='data/datasets/vaut_le_detour.json')
        apidae_schemas = open_data(path='data/schemas/apiObjetsTouristiquesResultat.schema')


st.header("Plotting")

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
    
    fig = plot_completeness_bar(completeness_percent)
    
    col1, col2 = st.columns([5,2])
    with col1:
        
        # Plot
        
        st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    
    with col2:
        
        # KPI/Score
        
        st.metric(label = "Total Score", value = total_score)
else:
    
    # Other instructions
    
    st.write('Upload data and schema first.')