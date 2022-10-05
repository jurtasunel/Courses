# Rosalind PROT exercise
# Last update: 23/07/2019


# Sample Dataset.
s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

# Create a codon dictionary for with ID as codons and values as aminoacids.
codon_dict = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V", "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V","UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V", "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V", "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A", "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A", "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A", "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A", "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D", "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D", "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E", "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E", "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G", "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G", "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G", "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}

# Create a string to store the protein sequence
p = ""

# Loop through the length of s in steps of three (each iteration will be a complete codon).
for i in range (0, len(s), 3):

    # If each triplet is in the codon dictionary.
    if s[i:i + 3] in codon_dict:

        # Add the dictionary value (Aa) of the triplet to the string p.
        p = p + (codon_dict[s[i:i + 3]])

# Sample Output.
print(p)