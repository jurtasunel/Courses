# Rosalind DNA exercise
# Last update: 21/06/2019


# Sample Dataset.
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Define the count for all bases as 0.
A = 0
C = 0
G = 0
T = 0

# Loop through the indices of s (from 0 to the length of s).
for i in range(len(s)):
    
    # If a postion equals a base, update that base count by adding 1.
    if s[i] == "A":
        A = A + 1
    elif s[i] == "C":
        C = C + 1
    elif s[i] == "G":
        G = G + 1
    elif s[i] == "T":
        T = T + 1

# Sample Output.
print(A, C, G, T)


################
# Extra points #
################

# Different ways of creating strings for giving the output:
# 1-Concatenating strings (convert the base count variables to strings is required).
output_sentence1 = "Your sequence has " + str(A) + " A, " + str(C) + " C, " + str(G) + " G and " + str(T) + " T."
print(output_sentence1)

# 2-Use the format function (allows combination of different variables).
output_sentence2 = "{} A, {} C, {} G and {} T were found in the sequence.".format(A, C, G, T)
print(output_sentence2)

# 3-Use the f before the string (combination of different variables also allowed).
output_sentence3 = f"There are {A} A, {C} C, {G} G and {T} T in your sequence."
print(output_sentence3)


# Different way of doing the exercise by creating a dictionary:
# Create a dictionary containing each base with its respective count.
bases_dict = {"A": 0, "C": 0, "G": 0, "T": 0}

# Loop through the indices of s #
for i in range(len(s)):

    # If the current base of s is within the dictionary.
    if s[i] in bases_dict:

        # That base count is update by increasing in 1.
        bases_dict[s[i]] = bases_dict[s[i]] + 1

# Sample output.
print("The count for each nucleotide in dictionary format is",bases_dict)
