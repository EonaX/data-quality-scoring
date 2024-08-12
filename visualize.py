#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:59:12 2024

@author: maximeb
"""

import matplotlib.pyplot as plt
import seaborn
import plotly.express as px
from plotly.offline import plot

# plotly variables
def update_layout(fig, title):
    fig.update_layout(
        title = dict(text=title, 
                     font=dict(size=50), 
                     automargin=True, 
                     ),
        font = dict(family="Courier New, monospace", 
                  size=18, 
                  color="RebeccaPurple")
        )

# plotly functions

def plot_completeness_bar(completeness, title='Data Set Completeness'):
    """
    From a dict, plots a plotly bar graph.

    Parameters
    ----------
    completeness : dict
        DESCRIPTION.

    Returns
    -------
    None.

    """
    keys = list(completeness.keys())
    values = []
    for n in completeness:
        values.append(completeness[n])
        
        dict_for_bar = {'keys': keys,
                        'values':values}
        
    fig = px.bar(dict_for_bar, x=keys, y=values,
                 title = "Data Set Completeness",
                 labels = {
                     "x":"Properties",
                     "y":"Completeness Percent"
                     })
    update_layout(fig, title)
    plot(fig)
