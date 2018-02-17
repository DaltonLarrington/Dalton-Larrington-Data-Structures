#Dynamic Fibonacci Sequence
#Programmer: Dalton Larrington
#Date: 2-17-18
#Using Memoization

import time

#Cache dictionary
fibonacci_cache = {}
Start_Time = time.time()

def fib(n):

    #If there is a value, such as n, in the cache, then return the cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    #Find the sequence
    if n == 1:
        number = 1

    elif n == 2:
        number = 1

    elif n > 2:
        number = fib(n-1) + fib(n-2)

    #Store number in the cache and return it
    fibonacci_cache[n] = number
    return number

for n in range(1, 100):
    print(fib(n))

print("Runtime:", time.time() - Start_Time)

    

    
