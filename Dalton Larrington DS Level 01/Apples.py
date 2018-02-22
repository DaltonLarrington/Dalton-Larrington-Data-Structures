#Apples
#Programmer: Dalton Larrington
#Date: 1-18-18

def Apples(numberlist, addNumbers, total):

     numberList = [14, 6, 9, 7, 8, 10, 3, 9]

     total = 0
     
     for i in numberList:
         
          total = i + numberList

          printLine = print("You can buy this set of apples. " + total)

          if total <= 100:

               return True          

          elif total > 100:

               return False

          print(print)




          

                    

          

    

    
