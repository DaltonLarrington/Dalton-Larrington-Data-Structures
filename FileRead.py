# File Read
# Programmer: Dalton Larrington
# Date: 1-12-18

counter = 0

infile = open("Radius.py", 'r')

lines = "Number of lines: "

for line in infile.readlines():
    
    print(lines, counter, line)
    
    counter = counter + 1
   
    
