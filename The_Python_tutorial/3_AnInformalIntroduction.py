# Indices and special characters
# Last update: 18/06/2019

#### Strings ####
word = "Python"

# String length and indices usage.
first_word = word[0:2]  # From position 0 (included) to position 2 (excluded).
second_word = word[2:6]

print(first_word,second_word)
print(first_word,second_word,sep="") # No separation between printed variables.

print("More Pyt\nhon") # \n means next line.
print(r"More pyth\non") # r before quotes means raw data (avoid special characters).

print(len(word))

##### Lists ####
squares = [1,4,9,16,25,36]
more_squares = squares + [7**2,8**2,9**2]
print(more_squares)

more_squares[2] = 77 # List, unlike strings, are mutables (they can be modified).
print(more_squares)

more_squares.append(100) # Append a new item at the end of the list.
print(more_squares)

more_squares[2:6] = [] # Remove some values.
print(more_squares)

all_squares = [squares,more_squares] # List can contain other lists as items.
print(all_squares)

#### Fibonacci series with while statement ####
a,b = 0,1 # Simultaneous assignment.
while (a < 100):
    print(a,end=", ") # Avoid new line between values by specifying the separation wanted.
    a,b = b,a+b # As it is inside the while loop, a and b will change until the while condition becomes false.


