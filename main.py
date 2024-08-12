#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:02:02 2024

@author: maximeb
"""

from data.load import *
from data.analysis import *
from visualize import *
import os

# Variables

cwd = os.getcwd()
apidae_data = None
apidae_schemas = None

# path_data = 'data/datasets/vaut_le_detour.json'
# path_schemas = 'data/schemas/apiObjetsTouristiquesResultat.schema'

# apidae_data = open_data(path_data)
# apidae_schemas = open_schemas(path_schemas)

# functions

# # Data analysis

# print_list_types(apidae_data)
# print_infos_data(apidae_data)

# # Schema analysis

# count_objects_per_type(apidae_schemas)
# # print_properties_per_type(apidae_schemas)
# intersection_properties = get_common_properties(apidae_schemas)

# # Data completeness

# completeness_percent = get_completeness_percent(apidae_data, intersection_properties)

# plot_completeness_bar(completeness_percent)

