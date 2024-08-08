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

#%% data

# types and number of fields per objetsTouristiques

for n in range(len(apidae_data['objetsTouristiques'])):
    print("Objet Touristique: {apidae_data['objetsTouristiques'][n]['nom']['libelleFr']}")
    print(f"Type: {apidae_data['objetsTouristiques'][n]['type']}")
    print(f"Nombre de champs:{len(apidae_data['objetsTouristiques'][n])}\n")

#%% schemas

# types of objetsTouristiques

print("Types d'objets touristiques modélisés:\n")

for n in range(len(apidae_schemas['properties']['objetsTouristiques']['items'])):
    print(apidae_schemas['properties']['objetsTouristiques']['items'][n]['id'])

# properties per objetsTouristiques

print("Propriétés par types d'objets touristiques modélisés:\n")

for n in range(len(apidae_schemas['properties']['objetsTouristiques']['items'])):   
    
    print(apidae_schemas['properties']['objetsTouristiques']['items'][n]['id'])
    key = input('Enter [y] to display its properties, otherwise enter any other key.\n')
    
    if key == 'y':
            pprint(apidae_schemas['properties']['objetsTouristiques']['items'][n]['properties'], depth = 1)

