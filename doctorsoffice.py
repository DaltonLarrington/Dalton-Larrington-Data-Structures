#Doctor's Office
#Programmer: Dalton Larrington
#Date: 1-31-18

import time
import random

names = ["joey", "bobby", "sueann", "loretta", "grant", "jenny", "billy",\
         "cletus", "tucker", "hunter", "bubba", "gunner", "rose", "amy",\
         "charlette", "duke", "ricky", "bo", "luke", "jessie"]

waitingRoom = []

triageRoom = []

examRoom = []

examRoomSize = 6

doctors = 6

def main():

    #Add multiple patients
    
    #Time limits

    currentTime = 0
    p = Patient()

    waitingRoom.append(p)

    while True:
        
        print (waitingRoom)
        print(triageRoom)
        print(examRoom)

        currentTime = currentTime + 1

        if waitingRoom[1]:

            x.callNurse()

            examRoom[0].treatmentTime = examRoom[0].treatmentTime - 1

        if examRoom[0].treatmentTime == 0:
            
            print(examRoom[0].treatmentTime)

            examRoom.pop(0)

        time.sleep(1)


        

"""move patient from waiting room to triage room"""
def callNurse():

    triageRoom.append(waitingRoom.pop(0))
    
    sorted(triageRoom, key = lambda patient: patient.triageNumber)

def doctor():

    examRoom.append(triageRoom.pop())

    #doctors = doctors - 1
    

class Patient:

    def __init__(self):
        
        self.triageNumber = random.randint(0, 100)
        
        self.name = names[random.randint(0, len(names)-1)]\
        + " " + names[random.randint(0, len(names)-1)]
        
        self.arrivalTime = 0
        
        self.treatmentTime = random.randrange(15, 20)

main()


        

    

        

        

        

    

    
    

        

    
    




        

         
