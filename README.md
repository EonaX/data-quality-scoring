# Data Quality Scoring Tool

## Presentation

This program aims at providing different data quality scores and visualization of a given dataset.

First of all, it is concerned with data completeness. It will provide:
 + a percentage of null values for each field, either globally – i.e. for the whole data set –, or locally – i.e. for a given instance of the data set;
 + a score of the data completeness according to a scoring formula with weights related to specific fields previously defined by the data provider.
 + data visualizations to get the big picture and eventually identify outliers.

Secondly, it will suggests improvements to the user.

## Functional Schema
![Functional Schema](https://github.com/EonaX/data-quality-scoring/blob/main/docs/20240808_data_quality_scoring_tool_functional_schema.png)

Inputs:
 + Scoring Formula
 + Dataset
 + Quality Rules

Scripts:
 + Local Completeness Scoring
 + Global Completeness Scoring

Outputs:
 + Global Completeness Score/Visualization
 + Local Completeness Score/Visualization
 + Improvement Suggestions
