#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:06:59 2024

@author: maximeb
"""
from main import cwd
from data.analysis import *
from data.load import open_data
from visualize import *
import streamlit as st

st.title('Data Quality App')

st.header("Load Data and Schema")

col1, col2 = st.columns(2)
with col1:
    apidae_data = st.file_uploader(label='dataset')
with col2:
    apidae_schemas = st.file_uploader(label='schemas')



st.header("Plotting")

if apidae_data and apidae_schemas:
    apidae_data = open_data(streamlit_uploaded_file=apidae_data)
    apidae_schemas = open_data(streamlit_uploaded_file=apidae_schemas)
    
    intersection_properties = get_intersection_properties(apidae_schemas)
    completeness_percent = get_completeness_percent(apidae_data, intersection_properties)
     
    # display = st.radio('Options:', ["analysis","visualization"])
    
    # if display == "visualization": 
    
    fig = plot_completeness_bar(completeness_percent)
    
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
