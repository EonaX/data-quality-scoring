#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:59:12 2024

@author: maximeb
"""

import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go


# plotly variables

def update_layout(fig, title):
    fig.update_layout(
        title = dict(text=title, 
                     font=dict(family="Poppins", 
                               size=30
                               ), 
                     automargin=False, 
                     ),
        font = dict(family="sans serif",
                    size=18,
                    )
        )
    
    fig.update_xaxes(tickangle=45
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
    return fig

# plotly indicator

def plot_total_score_gauge(total_score, title = 'Total Completeness Score'):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = total_score,
        number = {'suffix':'%'},
        gauge = {
            'bar': {'color': "#ffffff"},
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#ffffff"},
            'bordercolor': "#ffffff",
            'steps': [
            {'range': [0, 20], 'color': '#af1c17'},
            {'range': [20, 40], 'color': '#cf7673'},
            {'range': [40, 60], 'color': '#a1a38c'},
            {'range': [60, 80], 'color': '#8bd7b3'},
            {'range': [80, 100], 'color': '#17af68'}],
            
            
            }
    ))
    
    update_layout(fig, title)
    
    return fig