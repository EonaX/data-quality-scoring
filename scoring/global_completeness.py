#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:49:31 2024

@author: maximeb
"""
from data.parameters import common_fields
from data.load import apidae_data
count = {}

for n in common_fields:
    count[n] = 0

for n in apidae_data['objetsTouristiques']:
    s = set.intersection(common_fields, set(list(n.keys())))
    for m in s:
        count[m]= count[m] + 1
        
# percent

for n in count:
    count[n] = count[n]/len(apidae_data['objetsTouristiques'])*100