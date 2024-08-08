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

#%% DATA ANALYSIS

# types and number of fields per objetsTouristiques

for n in apidae_data['objetsTouristiques']:
    print("Objet Touristique:", n['nom']['libelleFr'])
    print("Type:", n['type'])
    print("Nombre de champs:", len(n), "\n")

#%% SCHEMAS ANALYSIS

# types of objetsTouristiques

print("Types d'objets touristiques modélisés:\n")

for n in apidae_schemas['properties']['objetsTouristiques']['items']:
    print('Type:', n['id'])
    print('Nombre de champs:', len(n['properties'].keys()), '\n')
    
#%% properties per objetsTouristiques

print("Propriétés par types d'objets touristiques modélisés:\n")

for n in range(len(apidae_schemas['properties']['objetsTouristiques']['items'])):   
    
    print(apidae_schemas['properties']['objetsTouristiques']['items'][n]['id'])
    key = input('Enter [y] to display its properties, otherwise enter any other key.\n')
    
    if key == 'y':
            pprint(apidae_schemas['properties']['objetsTouristiques']['items'][n]['properties'], depth = 1)

#%% shared properties between all objetsTouristiques

l = []

for n in apidae_schemas['properties']['objetsTouristiques']['items']:  
    l.append(set(list(n['properties'].keys())))
    
common_fields = (set.intersection(*l))

print('Champs communs à tous les objets touristiques:\n', common_fields)
