# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:29:14 2023

@author: user
"""
#assignment-hypothesis testing-cutlets
import pandas as pd
df=pd.read_csv("D:\\Data science\\Cutlets.csv")
df

unit1=df['Unit A']
unit2=df['Unit B']

df['Unit A'].hist()
df['Unit B'].hist()
#mean
df['Unit A'].mean()
df['Unit B'].mean()
# standard deviation
df['Unit A'].std()
df['Unit B'].std()

from scipy import stats
zcalc,pvalue=stats.ttest_ind(unit1,unit2)
zcalc
pvalue
alpha=0.05
if pvalue < alpha:
    print("H0 is rejected and H1 is accepted")
if pvalue > alpha:
        print("H1 is rejected and H0 is accepted")
#H1 is rejected and H0 is accepted
#=========================================================
#assignment-hypothesis testing-LabTat

import pandas as pd
from scipy.stats import f_oneway
data=pd.read_csv("D:\\Data science\\LabTAT.csv")
data

statistic,p_value=f_oneway(data['Laboratory 1'],data['Laboratory 2'],data['Laboratory 3'],data['Laboratory 4'])
statistic
pvalue
alpha=0.05

if pvalue < alpha:
    print("H0 is rejected and H1 is accepted")
if pvalue > alpha:
        print("H1 is rejected and H0 is accepted")
#H1 is rejected and H0 is accepted
#=============================================================
#assignment-hypothesis testing-BuyerRatio
import numpy as np
from scipy.stats import chi2_contingency
observed_values=np.array([[50,142,131,70],[435,1532,1356,750]])
chi2,p_val,dof,expected_values=stats.chi2_contingency(observed_values)


print(chi2)
print(p_val)
print(dof)
print("expected values table:",expected_values)

alpha=0.05
if p_val < alpha:
    print("H0 is rejected and H1 is accepted")
if p_val > alpha:
        print("H1 is rejected and H0 is accepted")
#H1 is rejected and H0 is accepted
#================================================================
#assignment-hypothesis testing-Costomer+OrderForm

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import chi2_contingency

data=pd.read_csv("D:\\Data science\\Costomer+OrderForm.csv")
data

data.Phillippines.value_counts()

data.Indonesia.value_counts()

data.Malta.value_counts()

data.India.value_counts()

obs=np.array([[271,267,269,280],[29,33,31,20]])
obs

chi2_contingency(obs)
