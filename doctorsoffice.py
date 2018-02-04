#Doctor's Office
#Programmer: Dalton Larrington
#Date: 1-31-18

# Originally I had trouble with finding the correct methods in which the simulation will run from.
# As we went along, I saw how abstract a simulation can be.
# While creating multiple patients, I found it difficult for the simulation to run multiple patients.
# For multiple patients I tried finding the most abstract way of doing so.
# Althought I failed in creating multiple patients,
# I found that the method does allow the simulation to print the patients treatment time.
# The simulation does run through, but it does not move the patient from waitingRoom to triageRoom effectivley.
# It rather moves the patient from waitingRoom, sends the patient to examRoom, counts down the treatmentTime,
# and then pops the patient out of the stack and ends the simulation.

import time

import random

names = ["joey", "bobby", "sueann", "loretta", "grant", "jenny", "billy",\
         "cletus", "tucker", "hunter", "bubba", "gunner", "rose", "amy",\
         "charlette", "duke", "ricky", "bo", "luke", "jessie", "tex"]

waitingRoom = []

triageRoom = []

examRoom = []

examRoomSize = 6

doctors = 6

def main():

    """Add multiple patients"""
    for x in range (len(names)):
        
        print(x)       
    
    """Time limits"""
    currentTime = 0
    
    p = Patient()

    waitingRoom.append(p)

    while True:
        
        print (waitingRoom)

        print(triageRoom)

        print(examRoom)
        
        currentTime = currentTime + 1

"""Take the 0th patient into the triageRoom"""
        if waitingRoom[0]:

            callNurse()

"""If there is a 0th patient in triageRoom, then append them to examRoom"""
        if triageRoom[0]:

            examRoom.append(triageRoom.pop(0))

        if examRoom[0].treatmentTime == 0:
        
            examRoom.pop(0)

        time.sleep(1)        

"""Move patient from waiting room to triage room"""
def callNurse():

    triageRoom.append(waitingRoom.pop(0))
    
    sorted(triageRoom, key = lambda patient: patient.triageNumber)

"""Append the doctor to an exam room from the list of 6"""
def doctor():

    examRoom.append(triageRoom.pop())

    doctors = doctors - 1
    
"""Create the patient object to have a triageNumber, a name, and a treatmentTime"""
class Patient:

    def __init__(self):
        
        self.triageNumber = random.randint(0, 100)
        
        self.name = names[random.randint(0, len(names)-1)]\
        + " " + names[random.randint(0, len(names)-1)]
        
        self.arrivalTime = 0
        
        self.treatmentTime = random.randrange(15, 20)

main()


        

    

        

        

        

    

    
    

        

    
    




        

         
