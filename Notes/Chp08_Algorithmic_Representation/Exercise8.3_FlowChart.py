# MANUAL WORK
# n = int(input("Input an integer, n: "))       #factorials for negative integers do not exist
# count = 0 
# product = 1


# if n <0: 
#    print(f"There is no factorial for {n}")

# elif n>0: 
#     while count<n:         #Let's say n is 5 and count is 4. The value of count will become 5 below so I used the correct relational operator 
#         count += 1
#         product = count * product
#     print(f"The values of n and n! are {n} and {product} respectively.")       #print has to be indented so that Python takes the last elif 

# elif n==0:
#     print(f"The values of n and n! are {n} and 1 respectively.")


# USING RECURSIVE FUNCTION


def factorial_calculate(n): 
    if n == 0: 
        return 1 
    
    else: 
        return n * factorial_calculate(n-1)
        

n = int(input("Give me a positive integer."))
if n<0:
    print(f"{n} cannot be a factorial.")
else: 
    print(f"The values of n and n! are {n} and {factorial_calculate(n)} respectively.")









