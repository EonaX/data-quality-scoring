#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:47:50 2024

@author: maximeb
"""

from pprint import pprint

def print_list_types(data):
    """
    Returns the set of unique types of objetsTouristiques.

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    list_types = []
    
    for n in range(len(data['objetsTouristiques'])):
        list_types.append(data['objetsTouristiques'][n]['type'])
     
    print(f'Unique types of objetsTouristiques:\n{set(list_types)}')

def print_infos_data(data):
    """
    types and number of fields per objetsTouristiques

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for n in data['objetsTouristiques']:
        print("Objet Touristique:", n['nom']['libelleFr'])
        print("Type:", n['type'])
        print("Nombre de champs:", len(n), "\n")


def count_objects_per_type(schema):
    """
    Count objetsTouristiques number per types in the schema.

    Parameters
    ----------
    schema : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print("Types d'objets touristiques modélisés:\n")

    for n in schema['properties']['objetsTouristiques']['items']:
        print('Type:', n['id'])
        print('Nombre de champs:', len(n['properties'].keys()), '\n')

def print_properties_per_type(schema):
    """
    Print properties per type of objetsTouristiques present in the schema.

    Parameters
    ----------
    schema : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    print("Propriétés par types d'objets touristiques modélisés:\n")
    
    for n in range(len(schema['properties']['objetsTouristiques']['items'])):   
        
        print(schema['properties']['objetsTouristiques']['items'][n]['id'])
        key = input('Enter [y] to display its properties, otherwise enter any other key.\n')
        
        if key == 'y':
                pprint(schema['properties']['objetsTouristiques']['items'][n]['properties'], depth = 1)

def print_common_properties(schema, print_results=False):

    """
    Returns the intersection set of properties between all objetsTouristisques types.

    Parameters
    ----------
    schema : TYPE
        DESCRIPTION.
        
    print_results : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    common_fields : TYPE
        DESCRIPTION.

    """
    l = []
    
    for n in schema['properties']['objetsTouristiques']['items']:  
        l.append(set(list(n['properties'].keys())))
        
    intersection_properties = (set.intersection(*l))
    if print_results == True:
        print('Champs communs à tous les objets touristiques:\n', intersection_properties)
    
    return intersection_properties

def get_completeness_percent(data, fields):
    """
    Returns the completeness percent of the data depending on the presence or absence of the given fields.

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    fields : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    completeness_percent = {}
    
    for n in fields:
        completeness_percent[n] = 0
    
    for n in data['objetsTouristiques']:
        s = set.intersection(fields, set(list(n.keys())))
        for m in s:
            completeness_percent[m]= completeness_percent[m] + 1
            
    # percent
    
    for n in completeness_percent:
        completeness_percent[n] = completeness_percent[n]/len(data['objetsTouristiques'])*100
        
    return completeness_percent