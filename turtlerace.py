import turtle
import time
print(turtle.screensize)

class RacingTurtle:

    def __init__(self, speed, turnDelay, name):
        
        self.name = name
        self.turt = turtle.Turtle()
        self.speed = speed
        self.turnDelay = 0.3 + turnDelay

    def getX(self):
        
        return self.turt.xcor()

    def getY(self):
        
        return self.turt.ycor()

    def forward(self):

        self.turt.forward(1)

    def turnRight(self, degrees):

        self.turt.right(degrees)
        time.sleep(self.turnDelay)

    def turnLeft(self, degrees):
    
        self.turt.left(degrees)
        time.sleep(self.turnDelay)

####################################

#turtles    
racerone = RacingTurtle(0, 0, "Racer One")
eugene = RacingTurtle(15, 0.005, "Eugene 'The Machine' Topps")
blaze = RacingTurtle(40, 1, "Blaze")
zeus = ZeusTurtle(0, -.15, "Zeus The Lightning Racer")

racers = [racerone, eugene, blaze, zeus]

eugene.turt.penup()
eugene.turt.sety( 150)
eugene.turt.pendown()



####################################

#tracks
raceTest = [100, 90, 100, -90, 100]
itrlOval = [100, -90, 100, -90, 100, 200, -90, 100, -90, 100]

def runRace(rt):    
      time.clock() #Initializes clock
      startTime = time.clock

      commandCounter = 0
      
      for distance in raceTest:

          print(distance, commandCounter)

          if commandCounter % 2 == 0:              
              runForward(distance, rt)
              
          else:
              rt.turnRight(distance)             

          commandCounter += 1
         
##      #forward 100
##      runForward(100, rt)
##
##      #right 90
##      rt.turnRight(90)
##
##      #forward 100
##      runForward(100, rt)
##
##      #left 90
##      rt.turnLeft(90)
##
##      #forward 100
##      runForward(100, rt)      
##
##      endTime = time.clock()
##
##      return endTime - startTime

          endTime = time.clock()

          return endTime - startTime

def runForward(dist, rt):
    distance = int(dist * (1 - rt.speed/100))
    
    for i in range(distance):
        rt.forward()

def reposRcers(racerlist):
    currentRacer = 0
    startpos = len(racers) * 250 - (len(racers)) * 125) * -1

    for racer in racerlist:

        racer.turt.penup()
        racer.turt.setx(startpos + (125 * currentRacer)
        racer.turt.pendown()
        currentRacer += 1

        
      
####################################

turtle.screensize(len(racers) * 250, 300)

reposRacers(racers)

for racer in racers:

    print(racer.name, runRace(racer, irtlOval))



