# Rosalind REVC exercise
# Last update: 24/06/2019


# Sample Dataset.
s = "AAAACCCGGT"

# Doing the excercise by starting to count from the LAST nucleotide of s and modifying the FIRST nt of sc:
# Create a list (mutable) with the string s.
sc_list = list(s)

# Create a variable with the last index of s. Indices go from 0 (included) to either length - 1 (included), or length (excluded).
s_last_index = len(s) - 1

# Loop through the indices of s reversed. The last i will be 0 (because -1 is excluded).
for i in range(s_last_index, -1, -1):
    
    # If a nucleotide in s is an A.
    if s[i] == "A":

        # The A will be substituted by T in the opposite position of sc relative to s.
        sc_list[s_last_index - i] = "T"
    
    # Same for the other nucleotides.
    elif s[i] == "T":
        sc_list[s_last_index - i] = "A"
    elif s[i] == "C":
        sc_list[s_last_index - i] = "G"
    elif s[i] == "G":
        sc_list[s_last_index - i] = "C"

# Join the sc_list into a string with no separation between its elements.
sc = "".join(sc_list)

# Sample Output.
print(sc)


################
# Extra points #
################

# For loops decreasing can be done with the reversed() function.
for i in reversed(range(len(s))):
    print(i)


# Doing the exercise by starting to count from the FIRST nucleotide of s:
# Create an empty list with same length than s.
sc_emptylist = [[]] * len(s)

# Loop through the indices of s. The program will start by checking the FIRST nt of s and modifying the LAST nt of sc.
for i in range(len(s)):

    # Exact same principle as when counting backwards. Doesn't matter if we go from 0 to the last index of s or vice versa. 
    if s[i] == "A":
        sc_emptylist[s_last_index - i] = "T"
    elif s[i] == "T":
        sc_emptylist[s_last_index - i] = "A"
    elif s[i] == "C":
        sc_emptylist[s_last_index - i] = "G"
    elif s[i] == "G":
        sc_emptylist[s_last_index - i] = "C"

sc_ford = "".join(sc_emptylist)
print(sc_ford)


# Doing the exercise using a dictionary:
# Create a dictionary with keys being the nt in s and the values being the complement nucleotides.
sc_dict = {"A":"T", "T":"A", "C":"G", "G":"C"}

# Create an empty list with same length of s for store the sc values. 
sc_emptylist2 = [[]] * len(s)

# Loop through the indices of s.
for i in range(len(s)):

    # If a value of s is present in the dictionary.
    if s[i] in sc_dict:

        # That s' value will be use as a key in the dictionary, and its value will be located in the opposite position of sc_emptylist2.
        sc_emptylist2[s_last_index - i] = sc_dict[s[i]]

# Join the values in sc_emptylist2 with no separation between them.
sc_emptylist2 = "".join(sc_emptylist2)
print(sc_emptylist2)

