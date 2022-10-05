# Rosalind GC exercise
# Last update: 01/07/2019


# Sample Dataset.
GC_Sample_Dataset = "C:/Users/UCD/Desktop/Python/Rosalind/GC_Sample_Dataset.txt"


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

# Create a function that calculates the gc percentage of a given sequence.
def get_gc_percentage(sequence):

    # Create a variable to store the gc count of the sequence.
    gc_count = 0

    # Loop through the nucleotides of the input sequence.
    for nt in sequence:
    
        # If a nucleotide of the sequence is a G or a C.
        if nt == "G" or nt == "C":

            # The gc count is updated by adding 1.
            gc_count = gc_count + 1
    
    # Get the gc percentage by dividing it by the lenght of the sequence and multiplying it by 100. 
    gc_percentage = gc_count / len(sequence) * 100

    return(gc_percentage)

# BODY #
# Store the output of the following function, which is a fasta dictionary.
fasta_dict = create_FASTA_dictionary_from_file(GC_Sample_Dataset)

# Create an empty dictionary that will store all pairs of FASTA IDs and their gc percentages.
gc_dict = {}

# Create a list that will store the maximum gc percentage and its ID.
gc_max_pair = ["No ID", 0]

# Loop through the keys in the fasta dictionary.
for key in fasta_dict:
    
    # Update the gc dictionary with the current key and its gc percentage.
    gc_dict[key] = get_gc_percentage(fasta_dict[key])

    # If the current gc percentage is bigger than the gc percentage on the gc maximum pair.
    if gc_dict[key] > gc_max_pair[1]:

        # The current gc percentage and its ID become the elements of the gc maximum pair.
        gc_max_pair = [key, gc_dict[key]]

# Sample Output.
print(gc_max_pair[0], gc_max_pair[1], sep="\n")

    
################
# Extra points #
################

# Function that creates a fasta list containing a list with the fasta IDs and another list with the fasta sequences (not using a dictionary).
def create_FASTA_ID_and_seq_lists_from_file(file_location):

    # Create lists to store the IDs of the fasta format and the sequences.
    id_list = []
    seq_list = []

    # Open the file containing the fasta sequences.
    with open(file_location) as file:

        # Loop through the lines of the file.
        for line in file:

            # Remove the final \n of all lines with rstrip().
            line = line.rstrip()

            # If the line starts with ">".
            if line[0] == ">":
        
                # Append the id list with the line from position 1 (the 0 is the ">") to the end.
                id_list.append(line[1:])
        
            else:
            
                # If length of id list is bigger than lenght of seq list (which means there is an "empty" ID).
                if len(id_list) > len(seq_list):

                    # Append the seq list with the line.
                    seq_list.append(line)

                else:

                    # The last element of the seq list is updated by adding to it the new line.
                    last_el = len(seq_list) - 1
                    seq_list[last_el] = seq_list[last_el] + line
    
    # Create a fasta dictionary by ziping the id list and the seq list together.
    fasta_list = [id_list, seq_list]

    return(fasta_list)


