import random
import sys
import time

def getAnswer(Number):
    if Number == 1:
        return "It is certain"
    elif Number == 2:
        return "It is decidely so"
    elif Number == 3:
        return "Yes"
    elif Number == 4:
        return "Try Again"
    elif Number == 5:
        return "Ask Again Later"
    elif Number == 6:
        return "Concentrate and Ask Again"
    elif Number == 7:
        return "My Reply is No"
    elif Number == 8:
        return "Doesn't Look Likely"
    elif Number == 9:
        return "Very Doubtful"

rand = random.randint(1,9)
fortune = getAnswer(rand)
question = input("What would you like to know: ")
print("")
print("The Magical Orb Has Been Rubbed")
time.sleep(2)
print("")
print("You Start Sweating with Fear")
time.sleep(1)
print("")
print("The Orb Slowly Shows it's Answer")
print("""
      __             __
   .-'.'     .-.     '.'-.
 .'.((      ( ^ `>     )).'.
/`'- \'._____\ (_____.'/ -'`
|-''`.'------' '------'.`''-|
|.-'`.'.'.`/ | | \`.'.'.`'-.|
 \ .' . /  | | | |  \ . '. /
  '._. :  _|_| |_|_  : ._.'
     ````` /T"Y"T\ `````
          / | | | 
         `'`'`'`'`'`
   """)
time.sleep(4)
print(f"-----> {fortune} <-----")
print("")

