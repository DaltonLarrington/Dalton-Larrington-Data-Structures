#The Collatz Conjecture
#Programmer: Dalton Larrington
#Date: 2-10-18

counter = 0

def main(number):

    

    #If the number is even
    if number % 2 == 0:

        final = number // 2  #Adding 1 to this sequence makes the program run forever???
    
    else:
        
        #If the number is odd
        final = 3 * number + 1

    return final

    print(final)

#Ask the user for a positive integer
userInput = int(input("Enter a positive number: "))
print("The sequence is: \n" + str(userInput))

#Print the sequence
New_Sequence = main(userInput)

while New_Sequence != 1:
    New_Sequence = main(New_Sequence)
    print(New_Sequence)





