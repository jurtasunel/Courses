# Rosalind SUBS exercise
# Last update: 23/07/2019


# Sample Dataset.
s = "GATATATGCATATACTT"
t = "ATAT"

# Create a list for store the positions of t in s.
p = []

# Loop through the indices of s.
for i in range(len(s)):

    # If 4 consecutive elements of s equal t:
    if s[i:i + 4] == t:

        # Append the position list with the index + 1 (because python indices start at 0, meaning that index 0 of s = position 1 of s).
        p.append(i + 1)
        

# Sample Output
print(p)
