# Functions
# Last update: 19/06/2019

def fibonacci_jose(n): # Head of the function, wiht the name and the required parameters.
    
    # Body of the function.
    a,b = 0,1
    while a < n:
        print(a,end=", ")
        a,b = b,a+b
        if b >= n:
            print(a,end=".""\n")
            break
    # By default, function will always return a value even if is not especified. In python this value is "none"
    
print(fibonacci_jose(200)) # This doesn't bring the fib values because that is a process that occurs within the function, but not the function output
print(fibonacci_jose(0)) # As the procedure is not being executed, the value returned is none, we can see it if we print the function output.

def fib_jose(n):
    
    # Define a result variable to store values. 
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return(result)

print(fib_jose(200))

