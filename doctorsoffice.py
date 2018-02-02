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

"""move patient from waiting room to triage room"""
def callNurse():

    triageRoom.append(waitingRoom.pop(0))
    
    sort(triageRoom, key = patient.triageNumber)
    

class patient:

    def __init__(self):
        
        self.triagenumber = random.rantInt(100)
        
        self.name = names[random.randInt(len(names)-1)]\
        + " " + names[random.randInt(len(names)-1)]
        
        self.arrivalTime = time
        
        self.treatmentTime random.rangerange(15, 20)

    def exit(self):
        #remove patient from simulation
        pass


        

    

        

        

        

    

    
    

        

    
    




        

         
