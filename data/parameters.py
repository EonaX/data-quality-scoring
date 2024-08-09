#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:39:39 2024

@author: maximeb
"""

from data.load import apidae_schemas

l = []

for n in apidae_schemas['properties']['objetsTouristiques']['items']:  
    l.append(set(list(n['properties'].keys())))
    
common_fields = (set.intersection(*l))
