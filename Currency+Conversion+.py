
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# Creates numpy vector from a list to represent money (inputs) vector.
money = np.asarray([70, 100, 20, 80, 40, 70, 60, 100])

# Creates pandas dataframe with column labels(currency_label) from the numpy vector for printing.
currency_label = ["USD", "EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "HKD"]
money_df = pd.DataFrame(data=money, index=currency_label, columns=["Amounts"])
print("Inputs Vector:")
money_df.T




# In[2]:


# Sets path variable to the 'path' of the CSV file that contains the conversion rates(weights) matrix.
path = get_ipython().magic(u'pwd')

#Imports conversion rates(weights) matrix as a pandas dataframe.

conversion_rates_df = pd.read_csv(path+"/currencyConversionMatrix.csv",header=0,index_col=0)

# Creates numpy matrix from a pandas dataframe to create the conversion rates(weights) matrix.

conversion_rates = conversion_rates_df.values

# Prints conversion rates matrix.
print("Weights Matrix:")
conversion_rates_df




# In[3]:


# TODO 1.: Calculates the money totals(outputs) vector using matrix multiplication in numpy.
money_totals = None

# Converts the resulting money totals vector into a dataframe for printing.

money_totals_df = pd.DataFrame(data = money_totals, index = currency_label, columns = ["Money Totals"])
print("Outputs Vector:")
money_totals_df.T

