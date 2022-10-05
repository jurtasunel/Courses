# Statements
# Last update: 18/06/2019

#### If statement ####
x = 30

if x < 0:
    x = 0 # If x is negative, redefine x as 0.
    print("Negative value converted to Zero")

elif x == 0:
    print("Zero")

elif x > 0:
    print("Positive value")

#### For statement ####
animals = ["cats","dogs","lions","snakes"]

# For statemenet with break statement
for animal in animals:
    if len(animal) < 5: # If the length of the string animal is < 5 (the case of cats and dogs).
        print(animal,"short name animal")
    else:
        animals.insert(0,animal) # If animal lenght > 4 (the case of lions), it will insert lions in the first position over and over again.
        print(animals)
        break # Stop the otherwise infinite loop (as everytime that lions is inserted the lenth increases, repeating the loop).

# For statement with in range() function
for i in range(3,10,2):
    print(i)

for i in range(len(animals)): # i goes from 0 to the last number of the position (4 in the case of animals).
    print(i,animals[i]) # print the index and the name on that index.

# Find prime numbers. What out parentesis are "semiopen on the right"
for n in range(2,10): # try all numbers from 2 to 10. 10 is excluded.
    for x in range(2,n): # comparte n with the numbers from 2 to n (6 will be compared with 2,3,4,5,6). n is excluded.
        if n % x == 0: # if the reminder of the division of n by one of the other x (all numbers from 2 to n) is 0.
            print(n,"equals",x,"multiplied by", n // x) # That number is not prime and is the product of x and n divided by x.
            break
    else: #this will happpend when the second for exhaustes the range (2,n) and the if statement has not been true in any case.
        print(n,"is a prime number")

# Two ways of doign the same thing:
# 1. If statement with else.
for n in range(1,10):
    if n == 5:
        print("now is 5")
    else: 
        print(n)
# 2. Continue with the loop after the if becomes true
for n in range(1,10):
    if n == 5:
        print("now is 5")
        continue
    print(n)

# Pass statement
for n in range(2,10):
    pass
    print(n)
 