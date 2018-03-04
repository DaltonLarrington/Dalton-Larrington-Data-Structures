#Binary Search
#Dalton Larrington
#3-4-2018

openFile = open("wordlist.txt", "r")

for line in openFile:

    for word in line.split():

        if "goodbye" in word:

            print(word)
    
