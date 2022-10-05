# Rosalind RNA exercise
# Last update: 21/06/2019


# Sample dataset.
t = "GATGGAACTTGACTACGTAAATT"

# As strings are immutable, create a list (which is mutable) with the input string t.
u_list = list(t)

# Loop through the indices in t.
for i in range(len(t)):

    # If a position of t is a T.
    if t[i] == "T":

        # Change that position in the u list for a U.
        u_list[i] = "U"
    
    # Maintain the other positions as they are by changing nothing using the pass statement.
    else: pass

# Convert the u list to a string and specify the separation mark between the elments.
u = "".join(u_list)

# Sample output.
print(u)

################
# Extra points #
# ##############

# Use the replace() method, specifiyin old element, new elment, and how many times that has to be done.
t_replaced = t.replace("T", "U")
print(t_replaced)


