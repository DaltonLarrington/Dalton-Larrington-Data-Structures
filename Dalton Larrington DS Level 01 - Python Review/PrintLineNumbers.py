#Text File Read
#Programmer: Dalton Larrington
#Date: 1-18-18


counter = 0

infile = open("Radius.py", 'r')

for line in infile.readlines():

    print(counter, line)

    counter = counter + 1

