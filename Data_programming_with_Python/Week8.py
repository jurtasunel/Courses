from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

# 1.
eb = pd.read_csv("ebola_test.csv")
print(eb)
# Get the percentage of ebola postives.
pos = eb.loc[eb["ebola"] == 1]
neg = eb.loc[eb["ebola"] == 0]
positives_perc = len(pos) / len(eb) * 100
print(positives_perc)

# 2.
# Set the cutoff and compute false and true positives and negatives.
cutoff = 0.15
false_pos = neg.loc[neg["prob"] > cutoff]
true_pos = pos.loc[pos["prob"] > cutoff]
false_neg = pos.loc[pos["prob"] <= cutoff]
true_neg = neg.loc[neg["prob"] <= cutoff]
# Calculate the FPR and FNR and print them out.
FNR = len(false_neg) / (len(false_neg) + len(true_pos))
FPR = len(false_pos) / (len(false_pos) + len(true_neg))

print("False positive rate:", FPR)
print("False negative rate:", FNR)

# 3.
import pandas as pd
eb = pd.read_csv("ebola_test.csv")

def FPR(x):

    cutoff = x
    pos = eb.loc[eb["ebola"] == 1]
    neg = eb.loc[eb["ebola"] == 0]
    
    false_pos = neg.loc[neg["prob"] > cutoff]
    true_neg = neg.loc[neg["prob"] <= cutoff]
    
    FPR = len(false_pos) / (len(false_pos) + len(true_neg))

    return(FPR)

print(FPR(0.15))

# 4.
import pandas as pd
eb = pd.read_csv("ebola_test.csv")

def FNR(x):

    cutoff = x
    pos = eb.loc[eb["ebola"] == 1]
    neg = eb.loc[eb["ebola"] == 0]
    
    false_neg = pos.loc[pos["prob"] <= cutoff]
    true_pos = pos.loc[pos["prob"] > cutoff]
    
    FNR = len(false_neg) / (len(false_neg) + len(true_pos))

    return(FNR)

print(FNR(0.15))

# 5.
import pandas as pd
import numpy as np
eb = pd.read_csv("ebola_test.csv")
cutoff_list = np.arange(0.1,0.3,0.001)
def FNR(x):
    cutoff = x
    pos = eb.loc[eb["ebola"] == 1]
    neg = eb.loc[eb["ebola"] == 0]
    false_neg = pos.loc[pos["prob"] <= cutoff]
    true_pos = pos.loc[pos["prob"] > cutoff]
    FNR = len(false_neg) / (len(false_neg) + len(true_pos))
    return(FNR)

min_cutoff = 1
min_FNR = 1
for value in cutoff_list:
    if FNR(value) < min_FNR:
        min_cutoff = value
        min_FNR = FNR(value)

print(min_cutoff)

# 6.
import pandas as pd
import numpy as np
from pandas import DataFrame
eb = pd.read_csv('ebola_test.csv')

def fpr(x):
    cutoff = x
    pos = eb.loc[eb["ebola"] == 1]
    neg = eb.loc[eb["ebola"] == 0]
    false_pos = neg.loc[neg["prob"] > cutoff]
    true_neg = neg.loc[neg["prob"] <= cutoff]
    FPR = len(false_pos) / (len(false_pos) + len(true_neg))
    return(FPR)
def fnr(x):
    cutoff = x
    pos = eb.loc[eb["ebola"] == 1]
    neg = eb.loc[eb["ebola"] == 0]
    false_neg = pos.loc[pos["prob"] <= cutoff]
    true_pos = pos.loc[pos["prob"] > cutoff]
    FNR = len(false_neg) / (len(false_neg) + len(true_pos))
    return(FNR)

# Get the unique values of the column "prob".
uniqvals = np.sort(eb.prob.unique())
# Create empty lists and append them.
FPR = []
TPR = []
for value in uniqvals:
    FPR.append(fpr(value))
    TPR.append(1 - fnr(value))

# Zip the lists and convert that to a df.
data = list(zip(FPR, TPR))
result = pd.DataFrame(data, index = uniqvals, columns = ["FPR", "TPR"])
print(result)
