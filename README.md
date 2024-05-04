# Academic Performance Management Program
## About the project

[//]: # ([![Django CI]&#40;https://github.com/Nanokwok/Academic-Performance-Management/actions/workflows/django.yml/badge.svg&#41;]&#40;https://github.com/Nanokwok/Academic-Performance-Management/actions/workflows/django.yml&#41;)

[//]: # ([![CodeQL]&#40;https://github.com/Nanokwok/Academic-Performance-Management/actions/workflows/codeql.yml/badge.svg&#41;]&#40;https://github.com/Nanokwok/Academic-Performance-Management/actions/workflows/codeql.yml&#41;)

This repository is a tkinter-based project aimed to facilitate the management of student scores, 
offering features such as adding or removing students, 
grouping them based on test scores, generating basic graphs, and displaying fundamental statistics for individual or 
multiple students.

## Features

- Add or remove students from the list
- Group students based on test scores (students with similar scores stay together, or arrange the scores of all groups to be as similar as possible)
- Generate basic graphs for selected students (bar charts, histograms, scatter plots, box plots)
- Display fundamental statistics for individual or multiple students (min, max, average, sum)
- Data storytelling page to visualize student performance and grade distribution


## Installation

Clone the repository:
```bash
git clone https://github.com/Nanokwok/Academic-Performance-Management.git
cd Academic-Performance-Management
```

## How to run

1. Install the required packages:
```bash
pip install -r requirements.txt
```
2. Run the application:
```bash
python APM.py
```

## Project Documents

- [Project Proposal](https://docs.google.com/document/d/11R-iiaoxBM3uOUnmBL-wqdtW7__TCA-o9l3oWIvOjXE/edit?usp=sharing)
- [Weekly Plan](https://github.com/Nanokwok/Academic-Performance-Management/wiki/Weekly-Plan)

## Data Sources

- [Student's Scores](https://www.kaggle.com/datasets/yapwh1208/students-score) - Kaggle dataset used in the application.