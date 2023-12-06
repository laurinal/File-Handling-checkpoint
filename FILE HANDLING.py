# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:49:00 2023

@author: iyino
"""

import numpy as np
import pandas as pd 
data1 = pd.read_csv("Loan_prediction_dataset.csv") 
loan_amount = data1["LoanAmount"]
statistic = loan_amount.describe()











