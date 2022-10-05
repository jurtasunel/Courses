# Rosalind HAMM exercise
# Last update: 26/06/2019


# Sample Dataset.
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

# Define the Hamming distance as 0.
dh = 0

# Loop through the indices in s (which are the same as the t indices).
for i in range(len(s)):

    # If a value of s equals the same position value in t.
    if s[i] != t[i]:

        # Update the dh by adding 1.
        dh = dh + 1

# Sample Output.
print(dh)
