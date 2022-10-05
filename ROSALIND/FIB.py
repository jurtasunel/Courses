# Rosalind FIB exercise
# Last update: 24/06/2019


# Sample dataset.
n = 6
k = 5

# The number of rabbit pairs in the first two months is 1, as they get to reproduction age in month 2.
month_1 = 1
month_2 = 1

# Print message for specific cases of n.
if n <= 0:
    print("There are no rabbits before month 1.")
elif n == 1:
    print(f"The number of rabbit pairs on the first month is 1.")
elif n == 2:
    print(f"The number of rabbit pairs on the second month is still 1.")

# The following for loop will only be executed if n > 2.
elif n > 2:

    # The general formula for the rabbit pairs at any given month n is: f(n+1) = fn + f(n-1)*k, with k being the reproductive rate.
    # Loop 2 times less than n because the first two months have already been counted.
    for i in range(n - 2):

        # The pairs in the next month will be the last month's pairs plus the offspring of the mature ones.
        # The new offspring in any generation is the pairs of two months ago multiplied by k, as they matured and gave k new pairs each.
        next_month = month_2 + (month_1 * k)

        # After creating the next value of the sequence, months 1 and 2 take new values for continue the sequence.
        month_1 = month_2
        month_2 = next_month

# Sample output.
print(next_month)
print(f"The number of rabbit pairs on the {n}th month with {k} reproductive rate will be {next_month}.")

# Prin bif pyramid


