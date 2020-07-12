# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:33:00 2020

@author: Mumes
"""

import pandas as pd

df=pd.read_csv(r'C:\Users\Mumes\Documents\ds_salary_proj\glassdoor_jobs.csv')


#salary parse

df = df[df['Salary Estimate'] !='-1']

df['hourly']= df['Salary Estimate'].apply( lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided']= df['Salary Estimate'].apply( lambda x: 1 if 'employer provided salary' in x.lower() else 0)

salary = df ['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary', ''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split ('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split ('-')[1]))
df['avg_salary'] = (df['min_salary'] + df['max_salary'] )/2 

#company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis =1 )

#state field
df['job_state'] = df['Location'].apply(lambda x: x.split (',')[1])

#age of company
df['age'] = df['Founded'].apply(lambda x: x if x<1 else 2020 - x)

#parsing of job description
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0) 
df['r_studio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower()  else 0)
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0) 
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0) 
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0) 

#df.columns
df_out = df.drop(['Revenue', 'Competitors'], axis =1)

df_out.to_csv(r'C:/Users/Mumes/Documents/ds_salary_proj/salary_data_cleaned.csv', index = False)
