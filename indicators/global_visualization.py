#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:51:59 2024

@author: maximeb
"""
import matplotlib.pyplot as plt
from scoring.global_completeness import count


fig = plt.figure(figsize=(19.2, 10.8))
plt.bar(*zip(*count.items()))
plt.title('Presence Percentage of Common Fields in the Dataset', size=36)
plt.xlabel('Common Fields', size=24)
plt.ylabel('Percentage %', size=24)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()