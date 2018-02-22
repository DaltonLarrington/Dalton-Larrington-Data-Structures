#Fibonacci Sequence Recursive 
#Programmer: Dalton Larrington
#Date:2-13-2018

import time

Start_Time = time.time()

def fib(n):
    
    if(n <= 1):
        return n

    else:
        return(fib(n-1) + fib(n-2))

input = int(input("Enter a positive number: "))

print("Fibonacci Sequence: ")

for i in range(input):
    print(i)


print("Runtime:", time.time() - Start_Time)





