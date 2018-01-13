# Factorials of 10
# Programmer: Dalton Larrington
# Date: 1-12-18

def factorial (n):
    if n == 1:
        return 1

    else:
        print (n)
        return (n * factorial(n-1))

print(factorial(10))

    
