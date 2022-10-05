import numpy as np
import pandas as pd
from pandas import DataFrame 
import seaborn as sns

# Read in the csv.
data = pd.read_csv("weather.csv", index_col="date")
print(data)

# Get the std deviation of all columns.
std = data.std(axis = 0, skipna = True)
print(std)

# Get stats summary with missing values
original_stats = data.describe()
print(original_stats)
print(data.median())

# Fill the missing values with the mean of each column.
data["mean_temp"].fillna(value = data["mean_temp"].mean(), inplace = True)
data["max_temp"].fillna(value = data["max_temp"].mean(), inplace = True)
data["min_temp"].fillna(value = data["min_temp"].mean(), inplace = True)
data["rain"].fillna(value = data["rain"].mean(), inplace = True)
clean_stats = data.describe()
print(clean_stats)
print(data.median())

# Sort the dataframe by the rain column
print(data.head())
print(data.sort_values(by = ["rain"]))

# 4
df = DataFrame({'a':[1,2,3,4,5],'b':[2,4,6,8,10]})
print(df)

# Create afunction that substracts the mean of each column.
def sub_mean(x):

    # Store the input df as a new df.
    df = x
    # Get the means and column names of the df.
    means = df.mean()
    colnames = df.columns
    # Loop through the means indices.
    for i in range(len(means)):
        # Substract to each column their mean value.
        df[colnames[i]] = df[colnames[i]] - means[i]
    
    return(df)

print(sub_mean(df))
