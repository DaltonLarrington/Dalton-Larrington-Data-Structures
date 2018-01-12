counter = 0

infile = open("Radius.py", 'r')

for line in infile.readlines():
    print(counter, line)
    counter = counter + 1
