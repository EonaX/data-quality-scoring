#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:47:01 2024

@author: maximeb
"""

import json

def open_data(path):
    with open(path) as f:
        return json.load(f)
    
# with Postman


# with requests

# # url = "https://api.plateforme.apidae-tourisme.com/api/v002/channel/recherche/list-objets-touristiques"

# # params = {
# #     "apiKey":"f4238d9a-e5ab-43eb-ada9-3d2e0230ec19",
# #     "projectId":"29e03482-980b-4d37-b25b-dc88705a578e",
# #     "searchId":"4609b3d7-e375-47cf-8a4c-a5a20ee68abc",
# #     "count": 100
# #     }

# # r = requests.get(url, params)

#%% Download the schemas

# with requests

# # r = requests.get('https://github.com/apidae-tourisme/apidae-sit-schemas/raw/main/v002/api/output/apiObjetsTouristiquesResultat.schema')

# # with open(r'data/schemas/apiObjetsTouristiquesResultat.schema', 'wb') as f:
# #     f.write(r.content)

def open_schemas(path):

    with open('data/schemas/apiObjetsTouristiquesResultat.schema') as f:
        return json.load(f)
    
#%%

