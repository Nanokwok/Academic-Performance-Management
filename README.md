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
- Display fundamental statistics for individual or multiple students (min, max, average, standard deviation, median)
- Data storytelling page to visualize student performance and grade distribution

## Screenshots
- Main Page
![0program.jpg](screenshots%2F0program.jpg)
- Import/Remove Students
![import_file.jpg](screenshots%2Fimport_file.jpg)
- Group Students
![grouping_student.jpg](screenshots%2Fgrouping_student.jpg)
- Generate Graphs
![one_student_graph.jpg](screenshots%2Fone_student_graph.jpg)
![many_student_graph.jpg](screenshots%2Fmany_student_graph.jpg)
- Display Statistics
![statistic.jpg](screenshots%2Fstatistic.jpg)
- Data Storytelling Page
![storytelling01.jpg](screenshots%2Fdata%2Fstorytelling01.jpg)
![storytelling02.jpg](screenshots%2Fdata%2Fstorytelling02.jpg)
![storytelling03.jpg](screenshots%2Fdata%2Fstorytelling03.jpg)

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
python main.py
```

## Project Documents

- [Project Proposal](https://docs.google.com/document/d/11R-iiaoxBM3uOUnmBL-wqdtW7__TCA-o9l3oWIvOjXE/edit?usp=sharing)
- [Weekly Plan](https://github.com/Nanokwok/Academic-Performance-Management/wiki/Weekly-Plan)

## Data Sources

- [Student's Scores](https://www.kaggle.com/datasets/yapwh1208/students-score) - Kaggle dataset used in the application.