# Rosalind CONS exercise
# Last update: 23/07/2019


# Sample Dataset.
CONS_Sample_Dataset = "C:/Users/UCD/Desktop/Python/Rosalind/CONS_Sample_Dataset.txt"

# FUNCTIONS #
# Create a function that produces a fasta dictionary with each fasta ID as key and each fasta seq as value.
def create_FASTA_dictionary_from_file(file_location):

    # Create an empty dictionary that will store the IDs of the fasta format as keys and the sequences as values.
    fasta_dict = {}

    # Open the file containing the fasta sequences.
    with open(file_location) as file:

        # Loop through the lines of the file.
        for line in file:

            # If lines don't start with a nucleotide or an ID, raise an error message.
            if not (line[0] is ">" or line[0] is "A" or line[0] is "G" or line[0] is "C" or line[0] is "T"):
                raise ("There are empty lines in the file")

            # Remove the final \n of all lines with rstrip().
            line = line.rstrip()

            # If the line starts with ">".
            if line[0] == ">":
            
                # Add the line from position 1 (the 0 is the ">") to the end as a key in the fasta dictionary, and asign a 0 value to it.
                fasta_dict[line[1:]] = 0
        
            else:

                # Create a variable to store the current last key of the fasta dictionary.
                last_key = list(fasta_dict.keys())[-1]

                # If the last key equals 0 (which means it has no sequence asigned as a value).
                if fasta_dict[last_key] == 0:

                    # The last key takes the line as its value.
                    fasta_dict[last_key] = line
            
                else:
                    # The last key is updated by adding the current line to its existing sequence.
                    fasta_dict[last_key] = fasta_dict[last_key] + line
    
    return(fasta_dict)

# Store the output of the function.
fasta_dict = create_FASTA_dictionary_from_file(CONS_Sample_Dataset)

# Create four lists for store the counts of each letter.
A = [0]*8
C = [0]*8
G = [0]*8
T = [0]*8

# Loop through the keys in the fasta dictionary.
for key in fasta_dict:

    # Loop through the length of each sequence.
    for i in range(len(fasta_dict[key])):

        # Update each list count by adding 1 on the corresponding positon.
        if fasta_dict[key][i] == "A":
            A[i] = A[i] + 1
        elif fasta_dict[key][i] == "C":
            C[i] = C[i] + 1
        elif fasta_dict[key][i] == "G":
            G[i] = G[i] + 1
        elif fasta_dict[key][i] == "T":
            T[i] = T[i] + 1

# Create a string to store the consensus sequence.
consensus = ""

# Loop through the conts lists by zipping them, so each iteration will check the same position in all lists.
for i in zip(A,C,G,T):

    # If the highest value is in the 0 index of the zipped (A, C, G, T) (meaning the first value of the A count):
    if max(i) == i[0]:

        # Add an A to the consensus sequence.
        consensus = consensus + "A"
    
    # Index 1 means the highest value is in the C count, index 2 is G and index 3 is T.
    elif max(i) == i[1]:
        consensus = consensus + "C"
    elif max(i) == i[2]:
        consensus = consensus + "G"
    elif max(i) == i[3]:
        consensus = consensus + "T"

# Sample Output
print(consensus)
print(A)
print(C)
print(G)
print(T)
        