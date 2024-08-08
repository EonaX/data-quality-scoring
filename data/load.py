#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:47:01 2024

@author: maximeb
"""

import json
import requests

# with Postman

with open('datasets/vaut_le_detour.json') as f:
    apidae_data = json.load(f)

#%% Download the schemas

r = requests.get('https://github.com/apidae-tourisme/apidae-sit-schemas/raw/main/v002/api/output/apiObjetsTouristiquesResultat.schema')

with open(r'schemas/apiObjetsTouristiquesResultat.schema', 'wb') as f:
    f.write(r.content)

with open('schemas/apiObjetsTouristiquesResultat.schema') as f:
    apidae_schemas = json.load(f)