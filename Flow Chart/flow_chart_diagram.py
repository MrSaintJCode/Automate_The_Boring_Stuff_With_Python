# Didn't needed to be coded but I wanted to test 
# my knowledge on if and else statements before
# getting into the course
import time as tm
YESanswers = ['Yes', 'yes', 'y', 'Y', 'Yea', 'yea', 'Yeah', 'yeah']
NOanswers = ['No', 'no', 'n', 'N', 'Nea', 'nea', 'Nope', 'nope']


def isRaining(answer):
    if answer in YESanswers:
        print(f"\n Oh no, it's raining!")
    elif answer in NOanswers:
        goOut()
    else:
        invalid()

def umbrella(answer):
    if answer in NOanswers:
        print("\n Lets wait a while for it to clear up\n")
        tm.sleep(10)  #Sleeping for 10 seconds
        start()
    elif answer in YESanswers:
        goOut()
    else:
        invalid()
        

def goOut():
    print("\n Awesome ! You can finally got out!")
    exit()

def start():
    print("To exit press CTRL+D")
    answer = input("\n Is it currently raining?\n")
    isRaining(answer)
    answer = input("\n Do you have an umbrella?\n")
    umbrella(answer)

def invalid():
    print("\n Invalid Input... Exiting")
    exit()

start()

