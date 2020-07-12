# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:29:51 2020

@author: Mumes
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Mumes/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 500 ,False, path, 15)

df.to_csv(r'C:/Users/Mumes/Documents/ds_salary_proj/glassdoor_jobs.csv', index= False)