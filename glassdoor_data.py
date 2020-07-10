# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:29:51 2020

@author: Mumes
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Mumes/Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs('data analyst', 10, False, path, 15)

df.head()