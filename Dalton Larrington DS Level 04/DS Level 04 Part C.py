#Dynamic Programing
#Dalton Larrington
#2-19-18

import time

Start_Time = time.time()

n = 100
key = [1,1]

for i in range(n):
    key.append(0)

def fib(x):
    
    if key[x] == 0:
        key[x] = fib(x-1) + fib(x-2)        
    return key[x]

print(fib(n))
print("Runtime:", time.time() - Start_Time)
