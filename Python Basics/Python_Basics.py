# This Program Says Hello and Ask for your Name

def hello(name,age):
    nameLen = len(name)
    print(f"\nHello {name}")
    if nameLen >= 10:
        print(f"The length of your name is {nameLen}")
        print("That's a pretty long name ! Awesome!")
    else:
        print(f"The length of your name is {nameLen}")
    print(f"You are {age} years young!")
    print(f"You will be {str(int(age) + 1 )} in a year.")


name = input("\nWhat is your name?\n")
age = input("\nWhat is your age? \n")
hello(name,age)