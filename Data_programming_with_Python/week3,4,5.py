import numpy as np
from pandas import DataFrame
import seaborn as sns

### WEEK 3 ###
#1
def finite_difference(n):

    # Generate diagonal matrix of dimension n x n.
    a = np.eye(n)
    
    # Fill the matrix with 1.
    a.fill(1)
    
    # Fill the diagonal with -2.
    np.fill_diagonal(a, -2)

    # Set to zero specific values
    for i in range(n):
        for j in range(n):
            # If element is not diagonal (i, i), upper diagonal (i, i + 1)
            # or lower diagonal (i, i - 1), set it to zero
            if (i != j and i != j + 1 and i != j - 1):
                a[i, j] = 0

    return(a)

print(finite_difference(7))

#2
def matrix_multplication(n):
    
    # Get the values to fill the matrices.
    values = np.arange(start = 1, stop = n**2 + 1)
    
    # Construct the matrices.
    X = np.array(values).reshape(n,n)
    Y = np.array(values)[::-1].reshape(n,n)
    
    # Multply X and Y
    multiplMatr = X.dot(Y)
    
    return(multiplMatr)

print(matrix_multplication(4))

#3
import numpy.random as npr
def binomial_vector(s,n,p,m):
    
    # Set the seed for random numbers.
    s = npr.seed(s)

    # Sample from a binomial distribution.
    result = np.array(npr.binomial(n, p, m))

    return(result)


print(binomial_vector(99,10,0.1,10))


#4

df = DataFrame({'x':[1,2,3,4],'y':[5,6,7,8],'z':[9,10,11,12]},index=['a','b','c','d'])
print(df)
print(df.loc[df.x > 2])
	

#5
europe = DataFrame({'Capital':['Vienna','NaN','Paris','Berlin','Dublin','Oslo','Barcelona'],
'Population':[9.0,11.6,65.3,84.0,5.0,5.4,'NaN'],
'Area':['NaN',30.5,551.7,357.4,70.3,385.2,498.5]
},index=['Austria','Belgium','France','Germany','Ireland','Norway','Spain'])

print(europe)
europe["Capital"]["Belgium"] = "Brussels"
europe["Population"]["Spain"] = "46.8"
europe["Area"]["Austria"] = "83.9"

print(europe)

### WEEK 4 ###
#1
path = "/home/josemari/Desktop/AE1_data.txt"
with open(path) as file:
    
    # Remove "\n" from lines.
    items = [line.strip() for line in file]
    # Create two empty lists.
    text = []
    numbers = []

    for element in items:
        # Separate elements by spaces.
        current_line = element.split(" ")
        for i in range(len(current_line)):
            # If the element lenght is less than 2 (only the numbers up to 9).
            if len(current_line[i]) < 2:
                numbers.append(current_line[i])
            else:
                text.append(current_line[i])
numbers = list(map(int, numbers))
print(text, "\n", numbers)

#2
path = "/home/josemari/Desktop/"
data = np.loadtxt(path + "AE2_data.txt", delimiter= " ", skiprows = 1)
print(data)

#3
import pandas as pd 

data = pd.read_csv("/home/josemari/Desktop/AE3_data.txt", sep="\t", skiprows = 3, index_col = "Name")
print(data)

colnames = data.columns
print(colnames)
wantedcol = ["Calories", "Cholesterol", "Sodium", "Sugar", "Calcium"]

for col in colnames:
    if col not in wantedcol:
        del data[col]

print(data)

#4
import sys
#! {sys.executable} -m pip install wbdata
import wbdata as wbd

print(len(wbd.search_countries("land")))

#5
#! {sys.executable} -m pip install wikipedia
import wikipedia as wp

print(wp.summary(("Data Science"), sentences = 2))
data_science = wp.page("Data Science")
print(data_science.title)
links = data_science.links

counter = 0
for link in links:
    print(link)
    if "Data" in link:
        counter = counter + 1
        print(counter)
    else:
        print("false")

print(counter)

### week 5 ###

#2
# Get seaborn available data from github
seaborn_data = "https://raw.githubusercontent.com/datavizpyr/data/master/palmer_penguin_species.tsv"
penguins_df = pd.read_csv(seaborn_data, sep="\t")
# See rows and columns in dataframe.
print(penguins_df.shape)
print(penguins_df.head)

#3
# Get number of penguins that were found in the island Dream.
dream = penguins_df.loc[penguins_df["island"] == "Dream"]
print(dream.count)

#4
# Plot bill length against flipper length and highlight the species.
print(penguins_df.columns)
sns.relplot(x = "culmen_length_mm",y = "flipper_length_mm", data = penguins_df, hue = "species");

#5
#plot with sns.distplot()






