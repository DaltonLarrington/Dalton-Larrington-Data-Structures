#Fibonacci Sequence Non-recursive
#Programmer: Dalton Larrington
#Date: 2-13-18

import time

startTime = time.time()

def fib(n):
    
    x = 0
    y = 1

    #Will find the nth number in the range 0 to n adding z and y each time
    for i in range(0, n):
        z = x
        x = y
        y = z + y

    return x

#Prints the sequence from 0 to 100 using the range above. 100 denotes n, which is terms.
for i in range(0, 10):
    print(fib(i))

print("Runtime: ")
print(time.time() - startTime)
    
