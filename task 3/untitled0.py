# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 09:57:27 2022

@author: Dell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from collections import Counter

#Function to convert tuples to dictionaries
def conversion(tup, dict):
    for x, y in tup:
        dict.setdefault(x, []).append(y)
    return dict

#Reading dataset and making a brief describtion
data=pd.read_csv("Wuzzuf_Jobs.csv")
data.describe()

#Sorting data 
data.sort_values("Title",inplace=True)

#Removing duplicates 
data.drop_duplicates(keep="first",inplace=True)

#Removing missing data
imputer = SimpleImputer(missing_values = ' ', strategy = 'mean')

#Printing jobs for each company and most demanding companies for jobs
x=data.iloc[:,:2]
C1 = Counter(x.Company)
most_companies = C1.most_common(10)
print("The most demanding companies for jobs are " )
print(most_companies)
comp_d={}
conversion(most_companies,comp_d)
print(comp_d)

#pie chart for most demanding companies for jobs
plt.pie(comp_d.values(),labels=comp_d.keys())

#Most popular job titles
C2 = Counter(x.Title)
most_titles = C2.most_common(10)
print("The most popular job titles are " )
print(most_titles)
tit_d={}
conversion(most_titles,tit_d)
print(tit_d)

#par chart of most popular job titles
plt.bar(tit_d.values(), tit_d.keys(), color ='maroon',
		width = 0.4)

#most popular areas
a=data.iloc[:,2:3]
C3 = Counter(a.Location)
most_areas = C3.most_common(10)
print("The most popular areas are " )
print(most_areas)
area_d={}
conversion(most_areas,area_d)
print(area_d)

#bar chart of most popular areas
plt.bar(area_d.keys(), area_d.values(), color ='maroon',
		width = 0.4)

#sills
s=data.iloc[:,7:8]
C4 = Counter(s.Skills)
most_skills = C4.most_common(10)
print("The most popular skills are " )
print(most_skills)
skills_d={}
conversion(most_skills,skills_d)
