#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:47:50 2024

@author: maximeb
"""

from data.load import apidae_data, apidae_schemas
from pprint import pprint

list_types = []

for n in range(len(apidae_data['objetsTouristiques'])):
    list_types.append(apidae_data['objetsTouristiques'][n]['type'])
 
print(f'Unique types of objetsTouristiques:\n{set(list_types)}')

#%%

list_keys = []

for n in range(len(apidae_data['objetsTouristiques'])):
    list_keys.append(list(apidae_data['objetsTouristiques'][n].keys()))
    print("Objet Touristique: {apidae_data['objetsTouristiques'][n]['nom']['libelleFr']}")
    print(f"Type: {apidae_data['objetsTouristiques'][n]['type']}")
    print(f"Nombre de champs:{len(apidae_data['objetsTouristiques'][n])}\n")
    

print(set(list_keys))
