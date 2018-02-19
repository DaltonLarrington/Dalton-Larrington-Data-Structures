
n = 10
key = [1,1]

for i in range(n):
    key.append(0)

def fib(x):
    
    if key[x] == 0:
        key[x] = fib(x-1) + fib(x-2)        
    return key[x]

print(fib(n))
